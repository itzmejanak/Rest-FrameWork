from rest_framework import serializers

class Modelserilizer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    roll_no = serializers.IntegerField()
    student_class = serializers.CharField(max_length=20)
    age = serializers.IntegerField()