from django.db import models
from django_mysql.models import JSONField

# Create your models here.
class User(models.Model):
    create=models.DateTimeField(auto_now_add=True)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=10,default='123456')
    add_by_uaer=models.CharField(max_length=100)


    class Meta:
        db_table='user'
        verbose_name='用户信息表'


class Apilist(models.Model):
    urlid=models.ForeignKey(on_delete=models.CASCADE,auto_created=True)
    apiurl=models.URLField(verbose_name=None)
    apiname=models.CharField(max_length=100)
    apimethod=models.CharField(choices=('POST','GET'))
    createtime=models.DateTimeField(auto_now_add=True)
    updatetime=models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table='Apilist'
        verbose_name='api基础信息表'

class Apiparater(models.Model):
    paraters=models.CharField(max_length=500,default=None)
    bodydata=JSONField()
    add_time=models.DateTimeField(auto_now_add=True)
    updatetime=models.DateTimeField(auto_now_add=True)
    result=JSONField()
    urlid=models.ForeignKey(to=Apilist)

    class Meta:
        db_table='Apiparater'
        verbose_name='api参数表'






























