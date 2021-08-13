from django.contrib import admin
from .models.category import Category
from .models.product import Product

# Register your models here.

class AdminCategory(admin.ModelAdmin):
    list_display =['name','slug']
    prepopulated_fields = {'slug' : ('name',)}

class AdminProduct(admin.ModelAdmin):
    list_display = ['name','slug','image','description','price','avalible','created','updated']
    list_filter = ['avalible','created','updated']
    list_editable = ['price','avalible']
    prepopulated_fields = {'slug' : ('name',)}


admin.site.register(Category,AdminCategory)
admin.site.register(Product,AdminProduct)
