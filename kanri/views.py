from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, 
    CreateView, 
    DeleteView, 
    DetailView
)
from .models import Traders, Product_List
from .forms import TraderForm, PostForms
from django.db.models import Q



class ProductListView(ListView):
    '''一覧'''
    model = Product_List
    template_name = 'kanri/list.html'


class NewPostView(CreateView):
    '''商品登録'''
    model = Product_List
    form_class = PostForms
    template_name = "kanri/product-form.html"
    success_url = reverse_lazy('kanri:product-form')

class NewTraderView(CreateView):
    '''業者登録'''
    model = Traders
    form_class = TraderForm
    template_name = "kanri/trader-form.html"
    success_url = reverse_lazy('kanri:list')

class DeleteProductView(DeleteView):
    '''削除'''
    model = Product_List
    success_url = reverse_lazy('kanri:list')
    template_name = 'kanri/delete.html'


class DetailProductView(DetailView):
    '''詳細'''
    model = Product_List
    template_name = "kanri/detail.html"
    context_object_name = 'item'