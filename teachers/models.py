from django.db import models

class Teacher(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birth_date = models.DateField("birth date")
