from django.db import models
from django.utils import timezone

# Create your models here.

##contact model##

class Contact(models.Model):
    name=models.CharField(max_length=50,null=False)
    email=models.EmailField(max_length=50,null=False)
    query=models.TextField(default="")
    phone=models.CharField(max_length=13,null=False)
    date=models.DateField(default=timezone.now)

    ## feeedback model ##

class Feedback(models.Model):
    name=models.CharField(max_length=50,null=False)
    email=models.EmailField(max_length=50,null=False,primary_key=True)
    remarks=models.TextField(default="")
    rating=models.TextField(max_length=5,null=False)
    date=models.DateField(default=timezone.now)

## user ##

class User(models.Model):
    name=models.CharField(max_length=50,null=False)
    email=models.EmailField(max_length=50,null=False,primary_key=True)
    password=models.CharField(max_length=50,null=False)
    phone=models.CharField(max_length=13,null=False)
    profile_pic=models.FileField(upload_to="user_pic/",default="")
    date=models.DateField(default=timezone.now)

## SportCourse ##

class SportCourse(models.Model):
    sports_name=models.CharField(max_length=50,null=False)
    duration=models.CharField(max_length=100,null=False)
    charge=models.CharField(max_length=50,null=False)
    description=models.TextField(null=False)
    sport_pic=models.FileField(upload_to="sport_pic/",default="")
    
## Coach ##

class Coach(models.Model):
    name=models.CharField(max_length=50,null=False)
    email=models.EmailField(max_length=50,null=False,primary_key=True)
    phone=models.CharField(max_length=13,null=False)
    age=models.CharField(max_length=50,null=False)
    experience=models.CharField(max_length=50,null=False)
    sport_name=models.CharField(max_length=50,null=False)
    profile_pic=models.FileField(upload_to="coach_pic/",default="")
    date=models.DateField(default=timezone.now)

## admission ##

gender =(
    ('male', 'Male'),
    ('female', 'Female'),
   
)
class AdmissionForm(models.Model):
    course_name=models.CharField(max_length=60)
    user_email=models.EmailField(max_length=60,primary_key=True)
    full_name=models.CharField(max_length=60)
    date_of_birth=models.CharField(max_length=10)
    phone=models.CharField(max_length=13)
    gender=models.CharField(max_length=6,choices=gender)
    address=models.TextField(default="")
    admission_status=models.CharField(max_length=10,default="pending")
    pic_name=models.FileField(upload_to="admission_pic/")
    date=models.DateField(default=timezone.now)

class Notice(models.Model):
    notice_content=models.CharField(max_length=255)
    date=models.DateField(default=timezone.now)
