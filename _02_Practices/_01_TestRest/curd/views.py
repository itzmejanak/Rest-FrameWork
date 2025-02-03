from django.shortcuts import render
from .models import CurdClass
from .serializers import CurdSerializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import io
# Create your views here.
@csrf_exempt

# Retrive data
def studend_api(request):
    if request.method == "GET":
        jc_data = request.body
        stream_data = io.BytesIO(jc_data)
        py_data = JSONParser().parse(stream_data)
        id = py_data.get('id')

        if id != None:
            c_data = CurdClass.objects.get(id=id)
            n_data = CurdSerializers(c_data)
            j_data = JSONRenderer().render(n_data.data)
        else:
            c_data = CurdClass.objects.all()
            n_data = CurdSerializers(c_data, many=True)
            j_data = JSONRenderer().render(n_data.data)

        return HttpResponse(j_data, content_type='application/json')
    
    # Create/Insert Data
    if request.method == "POST":
        jc_data = request.body
        stream_data = io.BytesIO(jc_data)
        py_data = JSONParser().parse(stream_data)

        seri = CurdSerializers(data = py_data)
        if seri.is_valid():
            seri.save()
            res = {"msg": "Successfuly Added"}
            j_data = JSONRenderer().render(res)
            return HttpResponse(j_data, content_type="application/json")
    

    # Update 
    if request.method == "PUT":
        jc_data = request.body
        stream_data = io.BytesIO(jc_data)
        py_data = JSONParser().parse(stream_data)

        name = py_data.get('name')
        ins = CurdClass.objects.get(name = name)
        n_data = CurdSerializers(ins, data=py_data, partial=True)

        if n_data.is_valid():
            n_data.save()
            res = {"msg": "Successfuly Updated"}
            j_data = JSONRenderer().render(res)
            return HttpResponse(j_data, content_type="application/json")
        
    
        # Update 
    if request.method == "DELETE":
        jc_data = request.body
        stream_data = io.BytesIO(jc_data)
        py_data = JSONParser().parse(stream_data)

        name = py_data.get('name')
        ins = CurdClass.objects.get(name = name)
        rows_count, details = ins.delete()
        if rows_count == 1:
            res = {"msg": "Successfuly Deleted"}
            j_data = JSONRenderer().render(res)
            return HttpResponse(j_data, content_type="application/json")

