from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=15)
    information = models.TextField()
    safety = models.IntegerField(default=0)
    entrance = models.CharField(max_length=7)

    def __str__(self):
        return self.name
