from django.db import models

# Create your models here.


class Component(models.Model):
    compId = models.IntegerField()
    compName = models.CharField(max_length=200)
    def __str__(self):              # __unicode__ on Python 2
        return self.compName
