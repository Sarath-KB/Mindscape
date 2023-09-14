from django.db import models
from User.models import tbl_psychiatristappointment
# Create your models here.
class tbl_prescription(models.Model):
    appointment=models.ForeignKey(tbl_psychiatristappointment,on_delete=models.CASCADE)
    medicine=models.CharField(max_length=5000)