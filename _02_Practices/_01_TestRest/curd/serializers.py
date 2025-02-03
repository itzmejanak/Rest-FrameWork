from rest_framework import serializers
from .models import CurdClass

class CurdSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    roll_no = serializers.IntegerField()
    city = serializers.CharField(max_length=50)
    stats = serializers.CharField(max_length=6)

    def create(self, validated_data):
        return CurdClass.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.city = validated_data.get('city', instance.city)
        instance.stats = validated_data.get('stats', instance.stats)
        instance.save()
        return instance

