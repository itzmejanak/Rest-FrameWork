from django.shortcuts import render
from .models import studentsInfo
from .serializers import seriStudents
from rest_framework import generics
from rest_framework import mixins

# Create your views here.

## Methods whome dosen't required pk
# class GetStudents(generics.GenericAPIView, mixins.ListModelMixin):
#     queryset = studentsInfo.objects.all()
#     serializer_class = seriStudents

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

# class InsertStudents(generics.GenericAPIView, mixins.CreateModelMixin):
#     queryset = studentsInfo.objects.all()
#     serializer_class = seriStudents

#     def post(self, request, *args, **kwargs):
#         return super().create(request, *args, **kwargs)


# ## Methods to whome we need pk
# class RetriveStudents(generics.GenericAPIView, mixins.RetrieveModelMixin):
#     queryset = studentsInfo.objects.all()
#     serializer_class = seriStudents

#     def get(self, request, *args, **kwargs):
#         return super().retrieve(request, *args, **kwargs)
    
    

# class UpdateStudents(generics.GenericAPIView, mixins.UpdateModelMixin):
#     queryset = studentsInfo.objects.all() 
#     serializer_class = seriStudents

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
    
#     def patch(self, request, *args, **kwargs):
#         return self.partial_update(request, *args, **kwargs)
    

# class DeleteStudents(generics.GenericAPIView, mixins.DestroyModelMixin):
#     queryset = studentsInfo.objects.all()
#     serializer_class = seriStudents

#     def delete(self, request, *args, **kwargs):
#         return super().destroy(request, *args, **kwargs)
    

## Methods whome dosen't required pk
class GET_POST_STUDENTS(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = studentsInfo.objects.all()
    serializer_class = seriStudents

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


## Methods to whome we need pk
class RUD_STUDENTS(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = studentsInfo.objects.all()
    serializer_class = seriStudents

    def get(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)