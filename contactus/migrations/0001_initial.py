# Generated by Django 5.0 on 2024-01-04 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=300, verbose_name='ایمیل')),
                ('title', models.CharField(max_length=300, verbose_name='عنوان')),
                ('full_name', models.CharField(max_length=300, verbose_name='نام و نام خانوادگی')),
                ('message', models.TextField(max_length=350, verbose_name='متن پیام')),
                ('created_at', models.DateTimeField(verbose_name='تاریخ ایجاد')),
                ('is_read_admin', models.BooleanField(default=False, verbose_name='خوانده شده توسط ادمین')),
            ],
            options={
                'verbose_name': 'تماس با ما',
                'verbose_name_plural': 'لیست تماس با ما',
            },
        ),
    ]
