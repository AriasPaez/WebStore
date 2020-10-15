from django.shortcuts import render,HttpResponse
from .models import Service, ImageService
# Create your views here.
def services(request):
    services = Service.objects.all()
    image_services = ImageService.objects.all()
    context={
        'services':services,
        'image_services':image_services
    }
    return render(request, 'services/services.html',context)