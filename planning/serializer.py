from rest_framework import serializers
from .models import Status

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        
        fields = ['work_order_no']
 
 
class BomSerializer(serializers.ModelSerializer):
    class Meta:
        feilds='__all__'