from unicodedata import category
from django.shortcuts import render
from .models import Category, Menu
from home.views import rev

# Create your views here.
def menu(request): 
    r=rev(request)
#     category = request.GET.get('category')
     
#     if category == None:
#             menus = Menu.objects.all()
#     else:
#             menus = Menu.objects.filter(category__name = category)

    
    categories = Category.objects.all()
    menus = Menu.objects.all()
    context = {'categories': categories, 'menus': menus }
    return render(request,"menu.html", context)