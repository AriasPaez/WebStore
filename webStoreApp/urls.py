from django.urls import path

from webStoreApp import views

urlpatterns = [
    path('',views.home,name="home"),
    path('services',views.services,name="services"),
    path('store',views.store,name="store"),
    path('contact',views.contact,name="contact"),
]
