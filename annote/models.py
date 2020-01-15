from django.db import models

# Create your models here.
class AnnoteModel(models.Model):
    image = models.ImageField(upload_to="media/",null=True)
    filename = models.CharField(max_length=50,default="image.jpg")
    LisenceNumber = models.CharField(max_length=30,null=True)
    company = models.CharField(max_length=50,null=True)
    carmodel = models.CharField(max_length=50,null=True)
    xcoordinate = models.IntegerField(default=0)
    ycoordinate = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    shape = models.CharField(max_length=30,default="rect")
