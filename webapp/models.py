from django.db import models

# Create your models here.
class Test(models.Model):
    create=models.DateTimeField(auto_now_add=True)
    username=models.CharField(max_length=100,default='ls')
    password=models.CharField(max_length=100,default='tool')


    class Meta:
        ordering=('create',)


class User(models.Model):
    url = models.CharField(max_length=100)
    username_login = models.CharField(max_length=200)
