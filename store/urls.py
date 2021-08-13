from django.urls import path
from .views import index

app_name = 'shop'

urlpatterns = [
    path('',index.Index.product_list,name='product_list'),
    path('<slug:category_slug>/',index.Index.product_list,name='product_list_by_category'),
    path('<int:id>/<slug:slug>/',index.Index.product_detail,name='product_detail'),
]