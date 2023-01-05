from rest_framework import serializers
from .models import Jobs

class JobsSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')
    # interested_candidates = serializers.ReadOnlyField(source='interested_candidates.email')
    class Meta:
        model = Jobs 
        fields = ['id', 'user_id', 'specialism_id', 'industry_id', 'contract_type_id', 'education_level_id', 'experience_id','jobs_title', 'search_and_listing', 'experience_length','experience_level','qualifications_competencies','duties_responsibilities','offered_salary','address','country','city','email','gender','languages','is_active','jobs_description','created_at','updated_at','application_deadline','is_company_name_hidden' ]

