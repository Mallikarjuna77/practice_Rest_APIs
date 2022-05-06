from .models import Dept, Admin
from rest_framework import serializers

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model=Admin
        fields='__all__'

class DeptSerializer(serializers.ModelSerializer):
    class Meta:
        model=Dept
        fields='__all__'

