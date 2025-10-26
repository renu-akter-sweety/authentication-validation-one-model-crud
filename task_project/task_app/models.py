from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class userinfomodel(AbstractUser):
    USER_type=[
        ('User','User'),
        ('Admin','Admin'),

    ]
    
    user_type=models.CharField(max_length=100, null=True,choices=USER_type)
    fullname=models.CharField(max_length=100,null=True)

class taskmodel(models.Model):
    task_status=[
        ('NotStarted','NotStarted'),
        ('Inprogress','Inprogress'),
        ('completed','completed'),

    ]
    task_name=models.CharField(max_length=100,null=True)
    task_description=models.TextField(null=True)  
    task_status=models.CharField(choices=task_status,null=True,max_length=100)   
    deadline=models.DateField(null=True)
    created_by=models.ForeignKey(userinfomodel,max_length=100, on_delete=models.CASCADE,null=True) 