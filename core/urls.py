from django.urls import path
from core.views import *
urlpatterns = [
    path('',home,name='home_page'),
    path('products',product,name='products_page'),
    path('about',about,name='about_page'),
    path('contact',contact,name='contact_page'),
    path('gallery',gallery,name='gallery_page'),
    path('service',service,name='service_page'),
]