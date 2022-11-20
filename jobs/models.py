from django.db import models
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight




class Jobs(models.Model):
    title = models.CharField("Name", max_length=240)
    qualification = models.CharField("Qualification", max_length=300)
    duties = models.CharField("Duties", max_length=500)
    salary = models.CharField("Salary", max_length=240)
    address = models.CharField("Adress", max_length=240)
    country = models.CharField("Country", max_length=240)
    city = models.CharField("City", max_length=240)
    email = models.EmailField()
    gender = models.CharField("Gender", max_length=240)
    language = models.CharField("Language", max_length=240)
    is_active = models.BooleanField("Is Active", max_length=240)
    description = models.CharField("Description", max_length=1000)
    deadline = models.CharField("Deadline", max_length=240)
    experience_length = models.CharField("Experience", max_length=240)
    experience_level = models.CharField("Experience Level", max_length=240)
    created = models.DateField(auto_now_add=True)
    owner = models.ForeignKey('auth.User',  on_delete=models.CASCADE)
    highlighted = models.TextField()
    

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