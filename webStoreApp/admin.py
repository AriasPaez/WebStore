from django.contrib import admin
from .models import CategoryArticle, Article, ImageArticle, ColorArticle, BrandArticle
# Register your models here.

class CategoryArticleAdmin(admin.ModelAdmin):
    list_display=(
        'name', 
        'description'
        )


class ArticleAdmin(admin.ModelAdmin):
    list_display=(
        'name', 
        'purchase_price', 
        'sale_price',
        'stock',
        'data_creation',
        'data_update'        
        )
    filter_horizontal = ("fk_category",'fk_brand','fk_color')
    readonly_fields=('data_creation','data_update')


class BrandArticleAdmin(admin.ModelAdmin):
    list_display=(
        'name', 
        'description'
    )

class ColorArticleAdmin(admin.ModelAdmin):
    list_display=(
        'name', 
        'description',
        'colored_name'
    )
    fields=(
        'name', 
        'description',
        'color_code'
    )

class ImageArticleAdmin(admin.ModelAdmin):
    list_display=(
        'name', 
        'fk_Article',
        'url_image'
        )

admin.site.register(CategoryArticle, CategoryArticleAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(ImageArticle, ImageArticleAdmin)
admin.site.register(ColorArticle, ColorArticleAdmin)
admin.site.register(BrandArticle, BrandArticleAdmin)