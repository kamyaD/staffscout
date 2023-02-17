from django.db import models
from jobs.models import Jobs
from django_userforeignkey.models.fields import UserForeignKey
from users.models import User
# from django.contrib.auth import get_user_model
# from django.contrib.auth import get_user_model





class CandidateJobApplications(models.Model):
    id = models.BigAutoField(primary_key=True)
    # jobs =  models.ForeignKey('jobs.Jobs', models.DO_NOTHING)
    user_id = models.PositiveBigIntegerField()
    job_id = models.PositiveBigIntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    

    def __str__(self):
        return self.user_id



# User = get_user_model()
class Profiles(models.Model):
    # user = UserForeignKey(auto_user_add=True, related_name='profiles')
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    specialism_id = models.TextField(db_collation='utf8mb4_bin', blank=True)
    experiences_id = models.PositiveBigIntegerField(blank=True)
    education_levels_id = models.PositiveBigIntegerField(blank=True)
    job_title = models.TextField(blank=True, null=True)
    personal_statement = models.TextField(blank=True, null=True)
    personal = models.TextField(blank=True, null=True)
    biography = models.TextField(blank=True, null=True)
    education = models.TextField(blank=True, null=True)
    experience = models.TextField(blank=True, null=True)
    portfolio = models.TextField(blank=True, null=True)
    skills = models.TextField(blank=True, null=True)
    job_level = models.CharField(max_length=50)
    county = models.CharField(max_length=50, blank=True)
    honors = models.TextField(blank=True, null=True)
    availability_status = models.IntegerField(blank=True)
    metadata = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    city = models.CharField(max_length=215, blank=True)
    country=models.CharField(max_length=215, blank=True)
    profile_pic = models.CharField(max_length=215, blank=True)

    def __str__(self):
        return self.user.username

    
    

