# Generated by Django 4.2.6 on 2024-01-04 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_productcategory_alter_product_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='', unique=True, verbose_name='عنوان در url'),
        ),
    ]
