from django.contrib import admin
from .models import Service, ImageService
# Register your models here.

class AdminService(admin.ModelAdmin):
    readonly_fields=('data_creation','data_update')

admin.site.register(Service,AdminService)
admin.site.register(ImageService)