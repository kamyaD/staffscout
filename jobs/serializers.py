from rest_framework import serializers
from .models import Jobs

class JobsSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # interested_candidates = serializers.ReadOnlyField(source='interested_candidates.email')
    

    class Meta:
        model = Jobs 
        fields = ['pk', 'title', 'qualification','duties', 'salary', 'address', 'country','city', 'email','gender','language','is_active','description','deadline','experience_length','experience_level','job_level','owner','owner_id', 'created']

