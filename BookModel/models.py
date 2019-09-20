from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class BookModel(models.Model):
    name=models.CharField(null=True,blank=True,max_length=200)
    coursename=models.CharField(null=True,blank=True,max_length=20)
    feedback=models.CharField(null=True,blank=True,max_length=2000)
    def __str__(self):
        return self.name