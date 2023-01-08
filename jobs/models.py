from django.db import models
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

class Jobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveBigIntegerField()
    specialism_id = models.PositiveBigIntegerField()
    industry_id = models.PositiveBigIntegerField()
    contract_type_id = models.PositiveBigIntegerField()
    education_level_id = models.PositiveBigIntegerField()
    experience_id = models.PositiveBigIntegerField()
    jobs_title = models.TextField()
    search_and_listing = models.IntegerField()
    experience_length = models.TextField()
    experience_level = models.TextField()
    qualifications_competencies = models.TextField()
    duties_responsibilities = models.TextField()
    offered_salary = models.TextField()
    address = models.TextField()
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    gender = models.IntegerField()
    languages = models.TextField(blank=True, null=True)
    is_active = models.IntegerField()
    jobs_description = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    application_deadline = models.DateField()
    is_company_name_hidden = models.IntegerField()


    def __str__(self):
        return self.title

    
class Specialisms(models.Model):
    id = models.BigAutoField(primary_key=True)
    specialty = models.TextField()
    type = models.TextField()
    specific_specialty = models.TextField(db_collation='utf8mb4_bin')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.specialty

class Specialities(models.Model):
    id = models.BigAutoField(primary_key=True)
    specialities_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.specialities_name

class ContractTypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    contract_types_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.contract_types_name

class EducationLevels(models.Model):
    id = models.BigAutoField(primary_key=True)
    experiences_id = models.PositiveBigIntegerField()
    education_levels_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.education_levels_name
