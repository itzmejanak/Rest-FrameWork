from django.shortcuts import render
from .serializers import RegisterSerilizer
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import io
# Create your views here.
@csrf_exempt
def RegisterUser(request):
    if request.method == "POST":
        streamble_data = request.body
        streamed_data = io.BytesIO(streamble_data)
        parsed_data = JSONParser().parse(streamed_data)
        seri = RegisterSerilizer(data = parsed_data)
        if seri.is_valid():
            seri.save()
            res = {"msg": "Successfuly Registered"}
            j_data = JSONRenderer().render(res)
            return HttpResponse(j_data, content_type="application/json")
        j_data = JSONRenderer().render(seri.errors)
        return HttpResponse(j_data, content_type="application/json")




