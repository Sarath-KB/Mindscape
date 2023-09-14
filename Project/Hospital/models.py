from django.db import models

from Guest.models import tbl_newhospital
# Create your models here.
class tbl_pyschiatrist(models.Model):
    name=models.CharField(max_length=50)
    contact=models.CharField(max_length=10)
    email=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    address=models.CharField(max_length=500)
    place=models.ForeignKey("Admin.tbl_place",on_delete=models.CASCADE)
    hospital=models.ForeignKey(tbl_newhospital,on_delete=models.CASCADE)
    photo=models.FileField(upload_to='PsychiatristPhoto/')
    password=models.CharField(max_length=100)

class tbl_pyschologist(models.Model):
    name=models.CharField(max_length=50)
    contact=models.CharField(max_length=10)
    email=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    address=models.CharField(max_length=500)
    place=models.ForeignKey("Admin.tbl_place",on_delete=models.CASCADE)
    hospital=models.ForeignKey(tbl_newhospital,on_delete=models.CASCADE)
    photo=models.FileField(upload_to='PsychologistPhoto/')
    password=models.CharField(max_length=100)

class tbl_availablepyschiatrist(models.Model):
    psychiatrist=models.ForeignKey(tbl_pyschiatrist,on_delete=models.CASCADE)
    date=models.DateField()
    from_time=models.CharField(max_length=50)
    to_time=models.CharField(max_length=50)

class tbl_availablepsychologist(models.Model):
    psychologist=models.ForeignKey(tbl_pyschologist,on_delete=models.CASCADE)
    date=models.DateField()
    from_time=models.CharField(max_length=50)
    to_time=models.CharField(max_length=50)

class tbl_pyschiatristtoken(models.Model):
    availability=models.ForeignKey(tbl_availablepyschiatrist,on_delete=models.CASCADE)
    token_no=models.IntegerField()
    status=models.IntegerField(default=0)

class tbl_pyschologisttoken(models.Model):
    availability=models.ForeignKey(tbl_availablepsychologist,on_delete=models.CASCADE)
    token_no=models.IntegerField()
    status=models.IntegerField(default=0)