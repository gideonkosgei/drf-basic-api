from rest_framework import serializers
from basic_api.models import DRFPost, DRFUser


class DRFPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = DRFPost
        fields = '__all__'
   
    

class DRFUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = DRFUser
        fields = '__all__'        