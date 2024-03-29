from django.db import models


# Create your models here.

class People(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False)
    school = models.CharField(max_length=20, blank=False, null=False)
    email = models.EmailField()

    def __str__(self):
        return self.name
