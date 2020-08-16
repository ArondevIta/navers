from django.db import models
from projects.models import Projects


class Navers(models.Model):
    name = models.CharField(max_length=200)
    birthdate = models.DateField(auto_now_add=False)
    admission_date = models.DateField(auto_now_add=False)
    job_role = models.CharField(max_length=150)
    projects = models.ManyToManyField(Projects)

    def get_projects(self):
        return ', '.join([str(p) for p in self.projects.all()])

    def __str__(self):
        return self.name
