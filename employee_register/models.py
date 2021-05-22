from django.db import models

# Create your models here.
# class Position(models.Model):
    
#     title = models.CharField(max_length=100)
#     def __str__(self):
#         return self.title
    

class Employee(models.Model):
    EMP_CHOICES = (
    ('Jnr Developer','Jnr Developer'),
    
    ('Accountant','Accountant'),
    ('Sales Manager','Sales Manager'),
    
)
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    position = models.CharField(choices= EMP_CHOICES, max_length=50)
