from django.db import models

class Traders(models.Model):
    trader_name = models.CharField(verbose_name='業者名',max_length=50)

    class Meta:
        verbose_name_plural= '業者'
    def __str__(self):
        return self.trader_name
class Product_List(models.Model):
    
    created_at = models.DateTimeField(verbose_name='登録日', auto_now_add=True)
    trader = models.ForeignKey(Traders, verbose_name='業者名',on_delete=models.CASCADE)
    product = models.CharField(verbose_name='商品名',max_length=50)
    barcode = models.PositiveIntegerField(verbose_name='バーコド',blank=True,null=True)
    enter_price = models.PositiveIntegerField(verbose_name='入値',blank=True,null=True)
    selling_price = models.PositiveIntegerField(verbose_name='売値',blank=False,null=False)
    remarks = models.CharField(verbose_name='備考',max_length=100,blank=True,null=True)

    class Meta:
        verbose_name_plural = '商品管理'
        def __str__(self):
            return self.product 
