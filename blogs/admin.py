from django.contrib import admin
from . import models

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'activation']
    list_editable = ['price', 'activation']
    # readonly_fields = ['slug', 'description']
    prepopulated_fields = {'slug': ['title',]}
    list_filter = ['price', 'activation']

class ProductInfoAdmin(admin.ModelAdmin):
    # pass
    list_display = ['color', 'size']
    list_editable = ['size']


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'url']
    list_editable = ['url']

class ProductTagAdmin(admin.ModelAdmin):
    list_display = ['tag']

admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.ProductCategory, ProductCategoryAdmin)
admin.site.register(models.ProductInformation, ProductInfoAdmin)
admin.site.register(models.ProductTag, ProductTagAdmin)
