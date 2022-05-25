from email.policy import default
from socket import NI_NUMERICHOST
from tkinter import CASCADE
from django.db import models
from django.db.models.fields import DateField
from django.utils import timezone

# Create your models here.

#ORGANIZER MODEL
class Organizer(models.Model):
    summercamp_id=models.CharField(primary_key=True, max_length=20)
    password=models.CharField(max_length=45,null=False)
    campname=models.CharField(max_length=50,null=False)
    ownername=models.CharField(max_length=40, null=False)
    campemailid=models.CharField(null=False, max_length=60)
    campmobileno=models.IntegerField(null=False)
    campaddress=models.CharField(max_length=100,null=False)
    description=models.TextField(null=False)

#FEEDBACK MODEL
class Feedback(models.Model):
    feedback_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=45,null=False)
    email=models.CharField(max_length=45, null=False)
    campname=models.CharField(max_length=100, null=False)
    date=models.DateField(default=timezone.now)
    feedbacktext=models.TextField(null=False)
    ratings=models.IntegerField(null=False)

#PROGRAM_DETAILS MODEL
class Program_details(models.Model):
    summercamp_id=models.CharField(max_length=20,null=False)
    program_id=models.AutoField(primary_key=True)
    programname=models.CharField(max_length=100,null=True)
    duration=models.CharField(max_length=20,null=False)
    fees=models.CharField(max_length=30,null=False)
    startdate=models.DateField(null=False)
    enddate=models.DateField(null=False)
    description=models.TextField(null=False)
    agegroup=models.CharField(null=False, max_length=15)

#JOB_DESCRIPTION MODEL
class Job_description(models.Model):
    summercamp_id=models.CharField(max_length=20,null=False)
    jobid=models.CharField(max_length=30,null=False,primary_key=True)
    postname=models.CharField(max_length=30,null=False)
    noofseats=models.IntegerField(null=False)
    lastdateofapply=models.DateField(null=False)
    postdate=models.DateField(null=False)
    description=models.TextField(null=False)

#CITY_EVENTS MODEL
class Cityevents(models.Model):
    event_id=models.AutoField(primary_key=True)
    eventname=models.CharField(max_length=100,null=False)
    date=models.DateField(null=False)
    city=models.CharField(max_length=50,null=False)
    venueaddress=models.TextField(null=False)
    description=models.TextField(null=False)
    eventpic=models.ImageField(max_length=255,upload_to="summercamp/event_pic",default="")

#CONTACTUS MODEL
class Contactus(models.Model):
    name=models.CharField(max_length=45,null=False)
    email=models.CharField(max_length=45,null=True)
    phone=models.IntegerField(null=False)
    question=models.TextField(null=False)
    date=models.DateField(default=timezone.now)




