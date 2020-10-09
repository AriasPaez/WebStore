from django.urls import path

from webStoreApp import views

urlpatterns = [
    path('',views.home,name="Home"),
    path('services',views.services,name="Services"),
    path('store',views.store,name="Store"),
    path('contact',views.contact,name="Contact"),
]