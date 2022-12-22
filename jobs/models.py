from django.db import models
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

JOB_LEVEL_CHOICES = (
    ('Intern', 'Entern/Fellow Level'),
    ('Entry', 'Entry Level'),
    ('Junior manager', 'Junior Manager'),
    ('Experienced', 'Experienced Professional'),
    ('Mid-Level', 'Mid Level Manager'),
    ('Specialist', 'Specialist/Highly Skilled Professional'),
    ('General', 'General/Senior Manager'),
    ('Derector', 'Derector/Executive')
)

LANGUAGE_CHOICES = (
    ('english', 'English'),
    ('kiswahili', 'Kiswahili'),
    ('french', 'French')
)

class Jobs(models.Model):
    title = models.CharField("Title", max_length=215)
    qualification = models.TextField("Qualification")
    duties = models.TextField("Duties", max_length=500)
    salary = models.IntegerField()
    address = models.CharField("Adress", max_length=215)
    country = models.CharField("Country", max_length=240)
    city = models.CharField("City", max_length=240)
    email = models.EmailField()
    gender = models.CharField("Gender", max_length=240)
    language = models.CharField("Language", max_length=240, choices=LANGUAGE_CHOICES)
    is_active = models.BooleanField("Is Active", max_length=240)
    description = models.TextField("Description", max_length=1000)
    deadline = models.DateField()
    experience_length = models.CharField("Experience", max_length=240)
    experience_level = models.CharField("Experience Level", max_length=240)
    created = models.DateField(auto_now_add=True)
    # owner = models.ForeignKey('users.User',  on_delete=models.CASCADE)
    # interested_candidate= models.ForeignKey('candidate.Candidate',  on_delete=models.CASCADE)
    job_level=models.CharField(max_length=240,choices=JOB_LEVEL_CHOICES)
    owner = models.ForeignKey('users.User', related_name='jobs', on_delete=models.CASCADE)
    
    
    
    




    

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