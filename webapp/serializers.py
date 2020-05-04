from rest_framework import serializers
from webapp.models import Test

class Testserializers(serializers.ModelSerializer):
    class Meta:
        model=Test
        fields=('id','username','password')

