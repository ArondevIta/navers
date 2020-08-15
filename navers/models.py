from django.db import models


class Navers(models.Model):
    name = models.CharField(max_length=200)
    birthdate = models.DateField(auto_now_add=False)
    admission_date = models.DateField(auto_now_add=False)
    job_role = models.CharField(max_length=150)

    def __str__(self):
        return self.name
