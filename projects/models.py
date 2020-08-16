from django.db import models


class Projects(models.Model):
    name = models.CharField(max_length=150)
    # navers = models.ManyToManyField(Navers)
    #
    # def get_navers(self):
    #     return ', '.join([str(n) for n in self.navers.all()])

    def __str__(self):
        return self.name
