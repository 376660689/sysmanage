from django.db import models

# Create your models here.

class cmdb(models.Model):
    property_id = models.AutoField(primary_key=True)
    property_name = models.CharField(max_length=64)
    property_num = models.CharField(max_length=32)	
