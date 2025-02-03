from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserInfo
from .serializers import UserInfoSerializers

# Create your views here.
@api_view(["GET", "POST", "PUT", "PATCH", "DELETE"])
def student_api(request, id=None):
    if request.method == "GET":
        if id is not None:
            model_obj = get_object_or_404(UserInfo, id=id)
            serializer = UserInfoSerializers(model_obj)
            return Response(serializer.data)
        else:
            model_objs = UserInfo.objects.all()
            serializer = UserInfoSerializers(model_objs, many=True)
            return Response(serializer.data)

    if request.method == "POST":
        data = request.data
        serializer = UserInfoSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data Inserted Successfully"})
        return Response(serializer.errors)

    if request.method == "PUT":
        data = request.data
        id = data.get("id")
        model_obj = get_object_or_404(UserInfo, id=id)
        serializer = UserInfoSerializers(model_obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data Completely Updated"})
        return Response(serializer.errors)

    if request.method == "PATCH":
        data = request.data
        id = data.get("id")
        model_obj = get_object_or_404(UserInfo, id=id)
        serializer = UserInfoSerializers(model_obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data Overwritten in Some Fields"})
        return Response(serializer.errors)

    if request.method == "DELETE":
        model_obj = get_object_or_404(UserInfo, id=id)
        model_obj.delete()
        return Response({"msg": "Deleted Successfully"})
