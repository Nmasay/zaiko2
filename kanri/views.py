from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, 
    CreateView, 
    DeleteView, 
    DetailView,
    UpdateView
)
from .models import Traders, Product_List
from .forms import TraderForm, PostForms
from django.db.models import Q



class ProductListView(ListView):
    '''一覧'''
    model = Product_List
    context_object_name = 'products'
    template_name = 'kanri/list.html'
    
    def get_queryset(self):
        q_word = self.request.GET.get('query')
        if q_word:
            object_list = Product_List.objects.filter(
                Q(product__icontains = q_word)|
                Q(trader__trader_name__icontains = q_word)|
                Q(barcode__icontains = q_word)
            ).order_by('-created_at')
        else:
            object_list = Product_List.objects.all().order_by('-created_at')
        return object_list     

class TraderListView(ListView):
    '''業者一覧'''
    model = Traders
    context_object_name = 'traders'
    template_name = 'kanri/trader-list.html'

class DeleteTraderView(DeleteView):
    '''業者削除'''
    model = Traders
    success_url = reverse_lazy('kanri:list')
    template_name = 'kanri/trader-delete.html'

class NewPostView(CreateView):
    '''商品登録'''
    model = Product_List
    form_class = PostForms
    template_name = "kanri/product-form.html"
    success_url = reverse_lazy('kanri:product-form')

class DeleteProductView(DeleteView):
    '''削除'''
    model = Product_List
    success_url = reverse_lazy('kanri:list')
    template_name = 'kanri/delete.html'

class NewTraderView(CreateView):
    '''業者登録'''
    model = Traders
    form_class = TraderForm
    template_name = "kanri/trader-form.html"
    success_url = reverse_lazy('kanri:list')

class UpdateProductView(UpdateView):
    '''更新'''
    model = Product_List
    form_class = PostForms
    template_name = "kanri/product-form.html"
    success_url = reverse_lazy('kanri:list')

class DetailProductView(DetailView):
    '''詳細'''
    model = Product_List
    template_name = "kanri/detail.html"
    context_object_name = 'item'