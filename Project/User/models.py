from django.db import models
from Guest.models import *
from Hospital.models import *

# Create your models here.
class tbl_emergencyrequest(models.Model):
    content=models.CharField(max_length=5000)
    major=models.CharField(max_length=50)
    user=models.ForeignKey(tbl_userregistration,on_delete=models.CASCADE)
    status=models.IntegerField(default=0)

class tbl_psychiatristappointment(models.Model):
    user=models.ForeignKey(tbl_userregistration,on_delete=models.CASCADE)
    token=models.ForeignKey(tbl_pyschiatristtoken,on_delete=models.CASCADE)
    booking_to_date=models.CharField(max_length=50)
    status=models.IntegerField(default=0)
    offline_status=models.CharField(max_length=50)

class tbl_psychologistappointment(models.Model):
    user=models.ForeignKey(tbl_userregistration,on_delete=models.CASCADE)
    token=models.ForeignKey(tbl_pyschologisttoken,on_delete=models.CASCADE)
    booking_to_date=models.CharField(max_length=50)
    status=models.IntegerField(default=0)
    offline_status=models.CharField(max_length=50)

class cchat(models.Model):
    content=models.CharField(max_length=500)
    date=models.DateTimeField(auto_now_add=True)
    to_user=models.ForeignKey(tbl_userregistration,on_delete=models.SET_NULL,null=True,related_name="to_user")
    from_user=models.ForeignKey(tbl_userregistration,on_delete=models.SET_NULL,null=True,related_name="from_user")
    to_cid=models.ForeignKey(tbl_pyschiatrist,on_delete=models.SET_NULL,null=True,related_name="to_cid")
    from_cid=models.ForeignKey(tbl_pyschiatrist,on_delete=models.SET_NULL,null=True,related_name="from_cid")

class lchat(models.Model):
    content=models.CharField(max_length=500)
    date=models.DateTimeField(auto_now_add=True)
    to_user1=models.ForeignKey(tbl_userregistration,on_delete=models.SET_NULL,null=True,related_name="to_user1")
    from_user1=models.ForeignKey(tbl_userregistration,on_delete=models.SET_NULL,null=True,related_name="from_user1")
    to_lid=models.ForeignKey(tbl_pyschologist,on_delete=models.SET_NULL,null=True,related_name="to_lid")
    from_lid=models.ForeignKey(tbl_pyschologist,on_delete=models.SET_NULL,null=True,related_name="from_lid")

class tbl_complaint(models.Model):
    content=models.CharField(max_length=5000)
    date=models.DateField(auto_now_add=True)
    user=models.ForeignKey(tbl_userregistration,on_delete=models.CASCADE)
    status=models.IntegerField(default=0)
    reply=models.CharField(max_length=5000,default="Not yet viewed")

