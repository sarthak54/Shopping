from django.shortcuts import render,get_object_or_404
from store.models.category import Category
from store.models.product import Product
from django.views import View
from cart.forms import CartAddProductForm

class Index(View):
    def product_list(request,category_slug=None):
        category = None
        categories = Category.objects.all()
        products = Product.objects.filter(avalible=True)
        if category_slug:
            category = get_object_or_404(Category,slug=category_slug)
            products = products.filter(category=category)
        return render(request,'index.html',{'category':category,'categories':categories,'products':products})

    def product_detail(request,id,slug):
        product = get_object_or_404(Product,id=id,slug=slug,avalible=True)
        cart_product_form = CartAddProductForm()
        print(product)
        return render(request,'productdetail.html',{'product':product,'cart_product_form':cart_product_form})




