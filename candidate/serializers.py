from rest_framework import serializers
from .models import Candidate

class CandidateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Candidate 
        fields = ['pk', 'first_name', 'last_name', 'phone', 'email', 'created']