from django.contrib import admin
from .models import Product, Orders, UpdateOrder
# Register your models here.
class PostAdmin( admin.ModelAdmin ):
    list_display = ['product_name']
    search_fields = ['product_id']


admin.site.register(Orders)
admin.site.register(UpdateOrder)

@admin.register(Product)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('tinyInject.js',)