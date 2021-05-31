from django.db import models

# Create your models here.

class Web(models.Model):
    hrefvalue=models.CharField(max_length=400,null=True)
    linkname=models.CharField(max_length=60,null=True)