from rest_framework import serializers
from .models import Jobs,Specialisms,Specialities,ContractTypes,EducationLevels
from candidate.models import CandidateJobApplications

class JobsSerializer(serializers.ModelSerializer):
    jobs_interested = serializers.PrimaryKeyRelatedField(many=True, queryset=CandidateJobApplications.objects.all())
    
    class Meta:
        model = Jobs 
        fields = ['id', 'user_id', 'specialism_id', 'industry_id', 'contract_type_id', 'education_level_id', 'experience_id','jobs_title', 'search_and_listing', 'experience_length','experience_level','qualifications_competencies','duties_responsibilities','offered_salary','address','country','city','email','gender','languages','is_active','jobs_description','created_at','updated_at','application_deadline','is_company_name_hidden', 'jobs_interested' ]

class SpecialismsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Specialisms
        fields = ['id','specialty','type','specific_specialty','created_at','updated_at','deleted_at']

class SpecialitiesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Specialities
        fields = ['id','specialities_name','created_at','updated_at']


class ContractTypesSerialiers(serializers.ModelSerializer):

    class Meta:
        model = ContractTypes
        fields = ['id', 'contract_types_name', 'created_at', 'updated_at']

class EducationLevelsSerialiers(serializers.ModelSerializer):

    class Meta:
        model = EducationLevels
        fields = ['id','experiences_id','education_levels_name','created_at','updated_at']