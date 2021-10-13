from django.db import models

# Create your models here.
class Product(models.Model):
    product_id =models.AutoField
    product_name = models.CharField(max_length=50)
    categogy = models.CharField(max_length=50, default="")
    subcategogy = models.TextField()
    price = models.IntegerField(default=0)
    desc = models.TextField()
    pub_date = models.DateField()
    image = models.ImageField(null=True)
    main =models.CharField(max_length=500)
    cpu = models.CharField(max_length=500)
    ram = models.CharField(max_length=500)
    cardhinh = models.CharField(max_length=500)
    hdd = models.CharField(max_length=500)
    monitor = models.CharField(max_length=500)
    madeby = models.CharField(max_length=500)




    def __str__(self):
        return self.product_name

class Orders(models.Model):
    orderid = models.AutoField(primary_key=True)
    itemsjson = models.CharField(max_length=5000)
    name = models.CharField(max_length=90)
    amount = models.IntegerField(default=0)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=50)

class UpdateOrder(models.Model):
    update_id = models.AutoField(primary_key=True)
    orderid = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."