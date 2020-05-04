from rest_framework import serializers
from webapp.models import Test

class Testserializers(serializers.ModelSerializer):
    class Meta:
        model=Test
        fields=('id','username','password')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']
