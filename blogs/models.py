from django.db import models
from django.utils.text import slugify


# Create your models here.

class Karbaran(models.Model):
    name = models.CharField(max_length=50)
    family = models.CharField(max_length=50)
    age = models.IntegerField()
    activation = models.BooleanField()


class ProductCategory(models.Model):
    title = models.CharField(max_length=300, verbose_name="عنوان")
    url = models.CharField(max_length=300, verbose_name="عنوان در url")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

class ProductInformation(models.Model):
    color = models.CharField(max_length=100, verbose_name="رنگ")
    size = models.CharField(max_length=100, verbose_name="اندازه")



    def __str__(self):
        return f"{self.color}-----{self.size}"

    class Meta:
        verbose_name = "اطلاعات تکمیلی"
        verbose_name_plural = "لیست اطلاعات تکمیلی"


class ProductTag(models.Model):
    tag = models.CharField(max_length=200, verbose_name="عنوان تگ")

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = "تگ محصول"
        verbose_name_plural = "تگ محصولات"
class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, null=True, blank=True, verbose_name="دسته بندی")
    info = models.OneToOneField(ProductInformation, on_delete=models.CASCADE, null=True, blank=True,verbose_name='اطلاعات تکمیلی')
    tags = models.ManyToManyField(ProductTag, verbose_name="تگ محصول")
    title = models.CharField(max_length=50, verbose_name="نام محصول")
    price = models.IntegerField(verbose_name="قیمت")
    description = models.CharField(max_length=50, verbose_name="توضیحات")
    activation = models.BooleanField(verbose_name="موجود/غیر موجود")
    slug = models.SlugField(default="", null=False, db_index=True, unique=True, verbose_name="عنوان در url")


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    def __str__(self):
        return f'{self.title}---{self.price}'
    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"
