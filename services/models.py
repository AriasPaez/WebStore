from django.db import models

# Create your models here.
class Service(models.Model):
    name=models.CharField(max_length=50,null=False)
    description=models.CharField(max_length=200,null=True,blank=True)
    image = models.ImageField(upload_to='service',default='../static/services/service_default.png', null=True)
    data_creation=models.DateTimeField(auto_now_add=True)
    data_update=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='Sevicio'
        verbose_name_plural='Servicios'
    
    def __str__(self):
        return self.name