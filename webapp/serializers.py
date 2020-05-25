from rest_framework import serializers
from webapp.models import User,Apilist,Apiparater

class Userserializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('id','username','password')

class Apilistserializers(serializers.ModelSerializer):
    class Meta:
        model=Apilist
        fields=('urlid','urlname','apiurl')

class Apiparaterserializers(serializers.ModelSerializer):
    model=Apiparater
    fields=('paraters','bodydata','urlid')





