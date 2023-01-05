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


# JOB_LEVEL_CHOICES = (
#     ('Intern', 'Entern/Fellow Level'),
#     ('Entry', 'Entry Level'),
#     ('Junior manager', 'Junior Manager'),
#     ('Experienced', 'Experienced Professional'),
#     ('Mid-Level', 'Mid Level Manager'),
#     ('Specialist', 'Specialist/Highly Skilled Professional'),
#     ('General', 'General/Senior Manager'),
#     ('Derector', 'Derector/Executive')
# )

# LANGUAGE_CHOICES = (
#     ('english', 'English'),
#     ('kiswahili', 'Kiswahili'),
#     ('french', 'French')
# )

# JOBS_INTERESTED_TITTLE = ()

# class Jobs(models.Model):
#     title = models.CharField("Title", max_length=215)
#     qualification = models.TextField("Qualification")
#     duties = models.TextField("Duties", max_length=500)
#     salary = models.IntegerField()
#     address = models.CharField("Adress", max_length=215)
#     country = models.CharField("Country", max_length=240)
#     city = models.CharField("City", max_length=240)
#     email = models.EmailField()
#     gender = models.CharField("Gender", max_length=240)
#     language = models.CharField("Language", max_length=240, choices=LANGUAGE_CHOICES)
#     is_active = models.BooleanField("Is Active", max_length=240)
#     description = models.TextField("Description", max_length=1000)
#     deadline = models.DateField()
#     experience_length = models.CharField("Experience", max_length=240)
#     experience_level = models.CharField("Experience Level", max_length=240)
#     created = models.DateField(auto_now_add=True)
#     job_level=models.CharField(max_length=240,choices=JOB_LEVEL_CHOICES)
#     owner = models.ForeignKey('users.User', related_name='jobs', on_delete=models.CASCADE)
    # interested_candidates =  models.ForeignKey('candidate.Candidate', related_name='jobs_interested', on_delete=models.CASCADE)
    
    
    
    




    

    def __str__(self):
        return self.title

    
    # def save(self, *args, **kwargs):
    #     """
    #     Use the `pygments` library to create a highlighted HTML
    #     representation of the code snippet.
    #     """
    #     lexer = get_lexer_by_name(self.language)
    #     linenos = 'table' if self.linenos else False
    #     options = {'title': self.title} if self.title else {}
    #     formatter = HtmlFormatter(style=self.style, linenos=linenos,
    #                             full=True, **options)
    #     self.highlighted = highlight(self.code, lexer, formatter)
    #     super().save(*args, **kwargs)