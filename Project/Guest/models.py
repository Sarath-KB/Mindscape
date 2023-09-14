from django.db import models
from Admin.models import *


# Create your models here.
class tbl_userregistration(models.Model):
    name=models.CharField(max_length=50)
    contact=models.CharField(max_length=10)
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=50)
    place=models.ForeignKey("Admin.tbl_place",on_delete=models.CASCADE)
    photo=models.FileField(upload_to='UserPhoto/')
    password=models.CharField(max_length=100)
    doj=models.DateField(auto_now_add=True)


class tbl_newhospital(models.Model):
    name=models.CharField(max_length=50)
    contact=models.CharField(max_length=10)
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=50)
    place=models.ForeignKey("Admin.tbl_place",on_delete=models.CASCADE)
    logo=models.FileField(upload_to='HospitalLogo/')
    proof=models.FileField(upload_to='HospitalLogo/')
    password=models.CharField(max_length=100)
    hospitaltype=models.ForeignKey("Admin.tbl_hospitaltype",on_delete=models.CASCADE)
    status=models.IntegerField(default=0)


class tbl_unknownemergency(models.Model):
    place=models.ForeignKey("Admin.tbl_place",on_delete=models.CASCADE)
    content=models.CharField(max_length=5000)
    major=models.CharField(max_length=50)
    status=models.IntegerField(default=0)
    