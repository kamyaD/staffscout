from rest_framework import serializers
from .models import Employer

class EmployerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employer 
        fields = ['pk', 'first_name', 'last_name', 'phone', 'email', 'created']