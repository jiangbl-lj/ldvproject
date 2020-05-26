from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.parsers import JSONParser


from rest_framework.views import APIView

from webapp.models import User
from webapp.serializers import Apilistserializers, Userserializers,Apiparaterserializers
from requests import request




# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = Userserializers

def user(request):
    if request.method=='Get':
        user_obj=User.objects.all()
        serializer=Userserializers(user_obj,many=True)
        return JsonResponse(serializer.data,save=False)
    elif request.method=='Post':
        data=JSONParser.parse(request)
        serializer=Userserializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=300)
        return JsonResponse(serializer.data, status=200)


def getapilists():
    url='http://qa2.roadefend.com/webng/v2/api-docs'
    res.=request('GET',url=url)



