from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .serializers import Modelserilizer
from .models import ModelData
from rest_framework.renderers import JSONRenderer


# Create your views here.
def ConvertData(request):
    c_data = ModelData.objects.all()
    seri = Modelserilizer(c_data, many=True)
    
    # j_data = json.dumps(seri.data)
    # return HttpResponse(j_data, content_type="application/json")

    j_data = JSONRenderer().render(seri.data)
    # return HttpResponse(j_data, content_type="application/json")
    return JsonResponse(seri.data, safe=False)


# Create your views here.
def EachData(request, pk):
    c_data = ModelData.objects.get(id=pk)
    seri = Modelserilizer(c_data)


    j_data = JSONRenderer().render(seri.data)
    return JsonResponse(seri.data)

    # return HttpResponse(j_data, content_type="application/json")
