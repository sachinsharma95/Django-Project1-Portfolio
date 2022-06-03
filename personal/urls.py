from unicodedata import name
from django.urls import path
from . import views
#url config kar rhe hai

urlpatterns = [

    # this is for home page
    path('', views.say_hello, name='index'),
    #this is for contact page 
    path('#contact/' ,views.contact,name= '#contact'),
    



    ]
