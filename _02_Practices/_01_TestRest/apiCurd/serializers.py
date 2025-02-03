from rest_framework import serializers
from .models import UserInfo
# Your serializers class here
class UserInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'
        

