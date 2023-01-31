from django.db import models
from .data import SPECIALISM,SALES_RETAIL, SUSPPLY_CHAIN_TRANSPORT_LOGISTICS,ENGINEERING_DESIGN
from .data import MARKETING,MEDIA_COMMUNICATION_AND_WRITING, SPECIALISM, ENGINEERING_CONSTRUCTION_PLANNING, ENERGY_MINING
from .data import CUSTOMER_SERVICE,ART_FASHION_DESIGN,ENTERTAINMENT, SCIENCE_LAB_PROFESSIONALS, BANKING_INVESTMENT_MANAGEMENT
from .data import IT_PROGRAMMING,MANUFACTURING, OFFICE_ADMIN, RESTAURANT_HOSPITALITY
from jobs.models import Jobs


class Candidate(models.Model):
    # id=models.IntegerField()
    first_name = models.CharField("First Name", max_length=240)
    last_name = models.CharField("last Name", max_length=240)
    phone = models.CharField("Phone", max_length=240)
    email = models.EmailField()
    specialism=models.CharField(max_length=240,choices=SPECIALISM, null=False)
    sales_retail = models.CharField(max_length=240,choices=SALES_RETAIL, null=True)
    marketing = models.CharField(max_length=240,choices=MARKETING , null=True)
    media_communication = models.CharField(max_length=240,choices=MEDIA_COMMUNICATION_AND_WRITING, null=True)
    customer_service = models.CharField(max_length=240,choices=CUSTOMER_SERVICE, null=True)
    art_fashion_and_design = models.CharField(max_length=240,choices=ART_FASHION_DESIGN, null=True)
    entertainment = models.CharField(max_length=240,choices=ENTERTAINMENT, null=True)
    it_programming = models.CharField(max_length=240,choices=IT_PROGRAMMING, null=True)
    manufacturing = models.CharField(max_length=240,choices=MANUFACTURING, null=True)
    supply_chain_transport_logistics = models.CharField(max_length=240,choices=SUSPPLY_CHAIN_TRANSPORT_LOGISTICS, null=True)
    manufacturing = models.CharField(max_length=240,choices=MANUFACTURING, null=True)
    engineering_design = models.CharField(max_length=240,choices=ENGINEERING_DESIGN, null=True)
    engineering_construction_planning = models.CharField(max_length=240,choices=ENGINEERING_CONSTRUCTION_PLANNING, null=True)
    energy_mining = models.CharField(max_length=240,choices=ENERGY_MINING, null=True)
    science_lab_professionals = models.CharField(max_length=240,choices=SCIENCE_LAB_PROFESSIONALS, null=True) 
    finance_accounting_auditing = models.CharField(max_length=240,choices=SCIENCE_LAB_PROFESSIONALS, null=True) 
    banking_investment_management = models.CharField(max_length=240,choices=BANKING_INVESTMENT_MANAGEMENT, null=True) 
    office_admin = models.CharField(max_length=240,choices=OFFICE_ADMIN, null=True) 
    restaurant_hospitality = models.CharField(max_length=240,choices=RESTAURANT_HOSPITALITY, null=True) 
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.first_name


class CandidateJobApplications(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveBigIntegerField()
    job_id = models.PositiveBigIntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    # jobs_id = models.ForeignKey('jobs.Jobs',related_name='jobs_interested', on_delete=models.CASCADE)
    # owner = models.ForeignKey('users.User', related_name='jobs_interested', on_delete=models.CASCADE)

    def __str__(self):
        return self.user_id

    
    
    



