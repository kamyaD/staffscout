from rest_framework import serializers
from .models import Candidate

class CandidateSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Candidate 
        fields = ['pk', 'first_name', 'last_name', 'phone', 'email', 'created', 'specialism', 'sales_retail', 'marketing', 'media_communication', 'customer_service', 'art_fashion_and_design','entertainment', 'it_programming', 'manufacturing', 'supply_chain_transport_logistics','manufacturing', 'engineering_design','engineering_construction_planning', 'energy_mining','science_lab_professionals','finance_accounting_auditing','banking_investment_management', 'office_admin', 'restaurant_hospitality']

    
class CreateCandidateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Candidate 
        fields = ['first_name', 'last_name', 'phone', 'email', 'specialism', 'sales_retail', 'marketing', 'media_communication', 'customer_service', 'art_fashion_and_design','entertainment', 'it_programming', 'manufacturing', 'supply_chain_transport_logistics','manufacturing', 'engineering_design','engineering_construction_planning', 'energy_mining','science_lab_professionals','finance_accounting_auditing','banking_investment_management', 'office_admin', 'restaurant_hospitality']