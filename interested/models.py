from django.db import models

# Create your models here.

class Interested(models.Model):

     full_name = models.CharField(max_length=50, blank=True, null=True)
     student_code = models.CharField(max_length=50, blank=True, null=True)
     email = models.CharField(max_length=50, blank=True, null=True)
     category = models.CharField(max_length=50, blank=True, null=True)