from django.contrib import admin
from .models import Product, Orders, UpdateOrder
# Register your models here.
class PostAdmin( admin.ModelAdmin ):
    list_display = ['product_name']
    search_fields = ['product_id']

admin.site.register(Product, PostAdmin)
admin.site.register(Orders)
admin.site.register(UpdateOrder)
