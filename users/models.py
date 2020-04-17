from django.db import models
from cv.models import Resume

# Create your models here.
class Register(models.Model):
    username= models.CharField(max_length=100)
    email= models.EmailField(max_length=100)
    history= models.ManyToManyField(Resume, null= True, blank= True )