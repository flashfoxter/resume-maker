from django.db import models
from django.contrib.auth.models import User


class Resume(models.Model):
    Developer= 'FR'
    Android_Developer = 'SO'
    IOS_Developer = 'JR'
    Frontend_Developer = 'SR'
    Data_Scientist = 'GR'
    Software_Developer = 'SW'
    YEAR_IN_SCHOOL_CHOICES = [
        (Developer, 'Developer'),
        (Android_Developer, 'Android_Developer'),
        (IOS_Developer, ' IOS_Developer'),
        (Frontend_Developer, 'Frontend_Developer'),
        (Data_Scientist, 'Data_Scientist'),
        (Software_Developer, 'Software_Developer')
    ]
    present_role= models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=Developer,
    )
    previous_role= models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=Data_Scientist,
    )
    
    first_name=models.CharField(max_length=100,default=True)
    last_name=models.CharField(max_length=100,default=True)
    mobile= models.IntegerField(default="91")
    mail= models.EmailField(max_length=25,default=True)
    linkedin = models.URLField(default="------")
    github=models.URLField(default="------")
    facebook=models.URLField(default="------")
    hobies=models.TextField(default="cricket")
    skills=models.TextField(max_length=280,default=True)
    present_company=models.CharField(max_length=100,default=True)
    your_intro = models.TextField(default=True)
    previous_company = models.CharField(max_length=100,default=True)  
    present_work = models.TextField(default=True)
    present_start= models.CharField(max_length=20,default='Jan, 2020')
    present_end= models.CharField(max_length=20,default='Present')
    previous_start= models.CharField(max_length=20,default='Jan, 2020')
    previous_end = models.CharField(max_length=20,default='Feb, 2020')
    previous_work = models.TextField(default=True)
    permanent_address = models.CharField(max_length=50,default = True)
    highest_qualification = models.CharField(max_length=50,default = 'BTECH')
    graduation_year = models.CharField(max_length=50,default = '2017-2021')
    institute_name= models.CharField(max_length=50,default = 'IIIT Gwalior')
    graduation_achievements = models.TextField(default=True)


    date= models.DateTimeField(auto_now_add=True)

