import json

from django.shortcuts import render
from .models import Product, Orders, UpdateOrder
from math import ceil
from django.http import HttpResponse



# Create your views here.

def index(request):
    # products = Product.objects.all()
    # print(products)
    allProds = []
    catprods = Product.objects.values('categogy', 'id')
    cats = {item['categogy'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(categogy=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    # n = len(products)
    # nSlides = n // 4 + ceil((n / 4) - (n // 4))
    # # params ={'no_of_slides':nSlides, 'range': range(1,nSlides),'product':products}
    # allProds = [[products, range(1, nSlides), nSlides], [products, range(1, nSlides), nSlides]]

    params = {'allProds': allProds}
    return render(request, 'shop/index.html', params)

def productView(request, myid):
   product = Product.objects.filter(id = myid)

   return render(request, 'shop/productView.html', {'product':product[0]})

def tracker(request):
    if request.method == "POST":
        orderid = request.POST.get('orderid', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(orderid=orderid, email=email)
            if len(order) > 0:
                update = UpdateOrder.objects.filter(orderid=orderid)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps({"status": "success", "updates": updates, "itemsjson": order[0].itemsjson},
                                          default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"No.item"}')
        except Exception as e:
            return HttpResponse('{"status":"error"}')

    return render(request, 'shop/tracker.html')

def checkout(request):
    if request.method == 'POST':
        itemsjson = request.POST.get('itemsjson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amount', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        address = request.POST.get('address', '') + " " + request.POST.get('address2', '')
        zip_code = request.POST.get('zip_code', '')
        state = request.POST.get('state', '')
        city = request.POST.get('city', '')
        order = Orders(itemsjson=itemsjson, name=name, email=email, phone=phone, address=address, zip_code=zip_code, state=state, city=city, amount=amount)
        order.save()
        update = UpdateOrder(orderid = order.orderid, update_desc="The order has been place")
        update.save()
        thank =True
        id = order.orderid
        return render(request,'shop/checkOut.html', {'thank':thank, 'id':id})

    return render(request, 'shop/checkOut.html')

def searchMatch(query, item):
    if query in item.product_name.lower() or query in item.categogy.lower():
        return True
    else:
        return False


def search(request):
    query= request.GET.get('search')
    allProds = []
    catprods = Product.objects.values('categogy', 'product_name')
    cats = {item['categogy'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(categogy=cat)
        prod=[item for item in prodtemp if searchMatch(query, item)]
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod)!= 0:
            allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds, "msg":""}
    if len(allProds)==0 or len(query)<4:
        params={'msg':"Please make sure to enter relevant search query"}
    return render(request, 'shop/search.html', params)
