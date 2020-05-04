from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from webapp.serializers import Test
from webapp.serializers import Testserializers
from requests import request



# Create your views here.
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
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.data,status=400)


