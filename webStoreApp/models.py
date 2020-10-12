from django.db import models

# Create your models here.
class Item(models.Model):
    name=models.CharField(max_length=50,null=False)
    brand=models.CharField(max_length=50,null=False)
    price=models.IntegerField(null=False)
    image = models.ImageField(upload_to='store')
    created=models.DateTimeField(auto_now_add=True)
