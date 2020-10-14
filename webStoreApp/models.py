from django.db import models
from django.utils.html import format_html
# Create your models here.
class CategoryArticle(models.Model):
    name=models.CharField(max_length=100,null=False, verbose_name='nombre')
    description=models.CharField(max_length=200,null=True,blank=True, verbose_name='descripción')

    class Meta:
        verbose_name='Categoría'
        verbose_name_plural='Categorías'

    def __str__(self):
        return self.name

class BrandArticle(models.Model):
    name=models.CharField(max_length=100,null=False, verbose_name='nombre')
    description=models.CharField(max_length=200,null=True,blank=True, verbose_name='descripción')

    class Meta:
        verbose_name='Marca'
        verbose_name_plural='Marcas'

    def __str__(self):
        return self.name

class ColorArticle(models.Model):
    name=models.CharField(max_length=100,null=False, verbose_name='nombre')
    color_code = models.CharField(max_length=6,null=False, default='ffff', verbose_name='color')
    description=models.CharField(max_length=200,null=True,blank=True, verbose_name='descripción')

    def colored_name(self):
        return format_html(
            '<span style="background-color:#{};display: inline-block;height: 10px;width: 10px;border-radius: 50%;"></span>',
            self.color_code,
        )        
    
    class Meta:
        verbose_name='color'
        verbose_name_plural='colores'

    def __str__(self):
        return self.name

class Article(models.Model):
    name=models.CharField(max_length=100,null=False, verbose_name='nombre')
    description=models.CharField(max_length=200,null=True,blank=True, verbose_name='descripción')
    purchase_price=models.IntegerField(null=False, verbose_name='precio de compra')
    sale_price=models.IntegerField(null=False, verbose_name='precio de venta')
    stock=models.IntegerField(null=False, verbose_name='cantidad')
    data_creation=models.DateTimeField(auto_now_add=True, verbose_name='fecha de creación')
    data_update=models.DateTimeField(auto_now_add=True, verbose_name='ultima modificación')
    fk_category=models.ManyToManyField(CategoryArticle, verbose_name='categoría')
    fk_brand=models.ManyToManyField(BrandArticle, verbose_name='marca')
    fk_color=models.ManyToManyField(ColorArticle, verbose_name='color')

    class Meta:
        verbose_name='Artículo'
        verbose_name_plural='Artículos'
    
    def __str__(self):
        return self.name
    
class ImageArticle(models.Model):
    fk_Article=models.ForeignKey(Article,on_delete=models.CASCADE, verbose_name='artículo')
    name=models.CharField(max_length=100, verbose_name='nombre')
    url_image = models.ImageField(upload_to='store',default='../static/webStoreApp/default_item.png', verbose_name='imagen')
    description=models.CharField(max_length=100,null=True,blank=True, verbose_name='descripción')

    class Meta:
        verbose_name='Imagen'
        verbose_name_plural='Imágenes'
    
    def __str__(self):
        return self.name

