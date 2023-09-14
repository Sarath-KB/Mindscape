from django.db import models
from Admin.models import *
from User.models import *
# Create your models here.

class tbl_rescueinfo(models.Model):
    hospital=models.ForeignKey(tbl_newhospital,on_delete=models.CASCADE)
    rescue=models.ForeignKey(tbl_rescueteam,on_delete=models.CASCADE)
    emergency=models.ForeignKey(tbl_emergencyrequest,on_delete=models.CASCADE)


class tbl_rescueinfounknown(models.Model):
    hospital=models.ForeignKey(tbl_newhospital,on_delete=models.CASCADE)
    rescue=models.ForeignKey(tbl_rescueteam,on_delete=models.CASCADE)
    emergency=models.ForeignKey(tbl_unknownemergency,on_delete=models.CASCADE)


