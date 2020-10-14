from django.db import models

# Create your models here.
class Service(models.Model):
    name=models.CharField(max_length=50,null=False)
    description=models.CharField(max_length=200,null=True,blank=True)
    data_creation=models.DateTimeField(auto_now_add=True)
    data_update=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='Sevicio'
        verbose_name_plural='Servicios'
    
    def __str__(self):
        return self.name

class ImageService(models.Model):
    fk_service=models.ForeignKey(Service,on_delete=models.CASCADE, verbose_name='servicio')
    name=models.CharField(max_length=100, verbose_name='nombre')
    url_image = models.ImageField(upload_to='store',default='../static/services/service_default.png', verbose_name='imagen')
    description=models.CharField(max_length=100,null=True,blank=True, verbose_name='descripción')

    class Meta:
        verbose_name='Imagen'
        verbose_name_plural='Imágenes'
    
    def __str__(self):
        return self.name