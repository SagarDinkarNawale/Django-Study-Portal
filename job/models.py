from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class Job(models.Model):
    bookname=models.CharField(max_length=200)
    authername=models.CharField(max_length=200)
    publication=models.CharField(max_length=200)
    classname=models.CharField(max_length=200)
    departmentname=models.CharField(max_length=200)
    bookimage=models.ImageField(upload_to='images/', default='images/ds.jpg')
 
    def __str__(self):
        return self.bookname

# class BookDemo(models.Model):
#     def getone(self,**kwargs):
#         try:
#             return self.get(kwargs)
#         except ObjectDoesNotExist:
#             return None
    
# class MyModel(models.Model):
#     temp=BookDemo()
    
    