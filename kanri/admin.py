from django.contrib import admin
from .models import Product_List, Traders

class TradersListAdmin(admin.ModelAdmin):
    fields = ['trader_name']
admin.site.register(Traders,TradersListAdmin)    

class ProductListAdmin(admin.ModelAdmin):
    fieldsets = [ 
        ('業者　商品名', {'fields':['trader']}),
        (None,{'fields':['product']}),
        (None,{'fields':['barcode']}),
        ('入値　売値',{'fields':['enter_price']}),
        (None,{'fields':['selling_price']}),
        ('備考',{'fields':['remarks']}),
    ]
# Register your models here.
admin.site.register(Product_List,ProductListAdmin)