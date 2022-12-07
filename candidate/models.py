from django.db import models
from jobs.models import Jobs

class Candidate(models.Model):
    # id=models.IntegerField()
    first_name = models.CharField("First Name", max_length=240)
    last_name = models.CharField("last Name", max_length=240)
    phone = models.CharField("Phone", max_length=240)
    email = models.EmailField()
    # password = models.CharField(max_length=50)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


