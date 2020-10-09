from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request,'webStoreApp/home.html')

def services(request):
    return HttpResponse("Services")

def store(request):
    return HttpResponse("Store")

def contact(request):
    return HttpResponse("Contact")
