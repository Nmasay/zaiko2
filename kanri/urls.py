from django.urls import path
from .views import (
    ProductListView,
    NewPostView,
    NewTraderView,
    DeleteProductView,
    DetailProductView,
    UpdateProductView,
    TraderListView,
    DeleteTraderView
)    

app_name = 'kanri'
urlpatterns = [
    path('',ProductListView.as_view(), name='list'),
    path('product-form/',NewPostView.as_view(), name='product-form'),
    path('trader-form/',NewTraderView.as_view(), name='trader-form'),
    path('<int:pk>/delete/',DeleteProductView.as_view(), name='delete'),
    path('<int:pk>/',DetailProductView.as_view(), name='detail'),
    path('<int:pk>/update/',UpdateProductView.as_view(), name='update'),
    path('trader/',TraderListView.as_view(),name='trader-list'),
    path('<int:pk>/trader-delete',DeleteTraderView.as_view(),name='trader-delete')
]