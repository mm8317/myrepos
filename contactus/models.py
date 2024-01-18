from django.db import models

# Create your models here.

class ContactUs(models.Model):
    email = models.EmailField(max_length=300, verbose_name='ایمیل')
    title = models.CharField(max_length=300, verbose_name='عنوان')
    full_name = models.CharField(max_length=300, verbose_name='نام و نام خانوادگی')
    message = models.TextField(max_length=350, verbose_name='متن پیام')
    created_at = models.DateTimeField(verbose_name='تاریخ ایجاد')
    is_read_admin = models.BooleanField(verbose_name='خوانده شده توسط ادمین', default=False)



    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'لیست تماس با ما'