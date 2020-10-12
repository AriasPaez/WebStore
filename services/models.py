from django.db import models

# Create your models here.
class Service(models.Model):
    # _id=models.ObjectIdField()
    name=models.CharField(max_length=50,null=False)
    description=models.CharField(max_length=200,null=True)
    image=models.ImageField(upload_to='services')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)