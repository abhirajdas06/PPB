from statistics import mode
from django.contrib import admin
from .models import Gallery

# from .models import Gallery, Category
# Register your models here.

# admin.site.register(Category)

# class GalleryAdmin(admin.ModelAdmin):
#     exclude = ('category',)
    
admin.site.register(Gallery)


