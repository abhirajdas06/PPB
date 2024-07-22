from unicodedata import category
from django.contrib import admin
from .models import Menu, Category
# Register your models here.

admin.site.register(Category)





class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'alt')
    search_fields = ['name', 'category']
admin.site.register(Menu, MenuAdmin)
