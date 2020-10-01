from django import forms
from .models import Traders, Product_List

class TraderForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TraderForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
    class Meta:
        model = Traders
        fields = ('trader_name',)
class PostForms(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(PostForms, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
    class Meta:
        model = Product_List
        fields = ('trader',
                  'product',
                  'barcode',
                  'enter_price',
                  'selling_price',
                  'remarks',)
        widgets = {'remarks': forms.Textarea(attrs={'cols': 25, 'rows': 4}),} 

