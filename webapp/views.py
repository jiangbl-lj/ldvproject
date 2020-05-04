from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.parsers import JSONParser

from webapp.models import User
from webapp.serializers import Test, UserSerializer
from webapp.serializers import Testserializers
from requests import request



# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def test(request):
    if request.method=='Get':
        test_obj=Test.objects.all()
        serializer=Testserializers(test_obj,many=True)
        return JsonResponse(serializer.data,save=False)
    elif request.method=='Post':
        data=JSONParser.parse(request)
        serializer=Testserializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=300)
        return JsonResponse(serializer.data, status=501)
