from django.db import models
from Guest.models import *
from Hospital.models import *

# Create your models here.

class tbl_district(models.Model):
    district_name=models.CharField(max_length=50)


class tbl_hospitaltype(models.Model):
    hospitaltype_name=models.CharField(max_length=50)


class tbl_place(models.Model):
    place_name=models.CharField(max_length=50)
    district=models.ForeignKey(tbl_district,on_delete=models.CASCADE)

class tbl_adminlogin(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
 
class tbl_rescueteam(models.Model):
    name=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    headname=models.CharField(max_length=50)
    headcontact=models.CharField(max_length=50)
    logo=models.FileField(upload_to='RescueteamLogo/')
    password=models.CharField(max_length=50)
    place=models.ForeignKey("Admin.tbl_place",on_delete=models.CASCADE)

class tbl_feedback(models.Model):
    content=models.CharField(max_length=5000)
    date=models.DateField(auto_now_add=True)
    user=models.ForeignKey(tbl_userregistration,on_delete=models.SET_NULL,null=True)
    psychiatrist=models.ForeignKey(tbl_pyschiatrist,on_delete=models.SET_NULL,null=True)
    psychologist=models.ForeignKey(tbl_pyschologist,on_delete=models.SET_NULL,null=True)
    hospital=models.ForeignKey("Guest.tbl_newhospital",on_delete=models.SET_NULL,null=True)
    status=models.IntegerField(default=0)    
