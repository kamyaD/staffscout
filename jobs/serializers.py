from rest_framework import serializers
from .models import Jobs

class JobsSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    

    class Meta:
        model = Jobs 
        fields = ['pk', 'title', 'qualification','duties', 'salary', 'address', 'country','city', 'email','gender','language','is_active','description','deadline','experience_length','experience_level','job_level', 'created']