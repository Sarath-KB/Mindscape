from django.db import models
from User.models import tbl_psychologistappointment
from Hospital.models import tbl_pyschiatrist

# Create your models here.
class tbl_refer(models.Model):
    referappointment=models.ForeignKey(tbl_psychologistappointment,on_delete=models.CASCADE)
    psychiatrist=models.ForeignKey(tbl_pyschiatrist,on_delete=models.CASCADE)