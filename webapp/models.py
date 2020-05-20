from django.db import models

# Create your models here.
class User(models.Model):
    create=models.DateTimeField(auto_now_add=True)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=10,default='123456')
    add_by_uaer=models.CharField(max_length=100)


    class Meta:
        db_table='user'
        verbose_name='用户信息表'


class Getapilist(models.Model):
    apiurl=models.URLField(verbose_name=None)
    apiname=models.CharField(max_length=100)
    apimethod=models.CharField(choices=('POST','GET'))









