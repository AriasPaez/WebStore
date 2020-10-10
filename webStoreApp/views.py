from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request,'webStoreApp/home.html')

def services(request):
    return render(request,'webStoreApp/services.html')

def store(request):
    return render(request,'webStoreApp/store.html')

def contact(request):
    return render(request,'webStoreApp/contact.html')
