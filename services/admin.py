from django.contrib import admin
from .models import Service, ImageService
# Register your models here.

class AdminService(admin.ModelAdmin):
    list_display=('name', 'data_creation', 'data_update')
    readonly_fields=('data_creation','data_update')

class AdminImageService(admin.ModelAdmin):
    list_display=('name', 'fk_service', 'url_image')

admin.site.register(Service,AdminService)
admin.site.register(ImageService, AdminImageService)