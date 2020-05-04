from django.db import models

# Create your models here.
class Test(models.Model):
    create=models.DateTimeField(auto_now_add=True)
    username=models.CharField(max_length=100,default='ls')
    password=models.CharField(max_length=100,default='tool')


    class Meta:
        ordering=('create',)



