from rest_framework import serializers
from .models import studentsInfo

class seriStudents(serializers.ModelSerializer):
    class Meta:
        model = studentsInfo
        fields = '__all__'
