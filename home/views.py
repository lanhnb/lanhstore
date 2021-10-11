from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from .forms import CommentForm, ContactForm
from django.http import HttpResponseRedirect, request
from django.http import HttpResponse, BadHeaderError
from .forms import RegistrationForm
from django.http import HttpResponseRedirect
from .models import Post, Contact

import home







# Create your views here.
def post(request, pk):
    post = get_object_or_404( Post, pk=pk )
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm( request.POST, author=request.user, post=post )
        if form.is_valid():
            form.save()
            return HttpResponseRedirect( request.path )
    return render( request, "pages/post.html", {"post": post, "form": form} )

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, "pages/contact.html")



def successView(request):
    return HttpResponse('Success! Thank you for your message.')


def error(request):
    return render(request, 'pages/error.html')


def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'pages/register.html', {'form': form})
