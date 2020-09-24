from django.shortcuts import render
from django.views.generic import ListView
from .models import Product_List
from django.db.models import Q



class ProductListView(ListView):
    '''一覧'''
    model = Product_List
    template_name = 'kanri/list.html'

