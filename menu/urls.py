from xml.dom.minidom import Document
from django.urls import path
from menu import views


urlpatterns = [
    path('', views.menu,name="menu"),       
]
