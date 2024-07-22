from pickle import NONE

from django.shortcuts import render
from .models import Gallery
from home.views import rev

# Create your views here.




def gallery(request):
    r=rev(request)
 
     
     
     
    # category = request.GET.get('cat')

    # if category == NONE:
    #     pass
       
    #     # gallery = Gallery.objects.all()

    # else:
    #     # print("if loop is working")
    #     # print(category)
        
        
    #     gallery = []
        
    #     catgal = Gallery.objects.values('category')
    #     # print(catgal)
    #     cats = {item['category'] for item in catgal}
    #     # print(cats)
    #     for cat in cats:
    #         galimg = Gallery.objects.filter(category=cat)
    #         # print(galimg)
    #         gallery = galimg
    #         # print(gallery)
    
    # categories = Category.objects.all 'categories': categories,
    gallery = Gallery.objects.all()
    context = { 'gallery': gallery}
    return render(request,"gallery.html", context)