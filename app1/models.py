from django.db import models

# Create your models here.


class ContactDetail(models.Model):
    name=models.CharField(default='',max_length=50,null=True,blank=False)
    email=models.EmailField(default='',max_length=50,null=False,blank=False)
    subject=models.CharField(max_length=200)
    message=models.TextField()

    def __str__(self):
        return self.name

class PersonalDetail(models.Model):
    firstname=models.CharField(default='',max_length=20,null=False,blank=False)
    midname=models.CharField(default='',max_length=20,null=False,blank=False)
    lastname=models.CharField(default='',max_length=20,null=False,blank=False)
    email=models.EmailField(max_length=100,null=False,blank=False)
    contact_no=models.PositiveIntegerField(null=True,blank=True)
    city=models.CharField(max_length=50,null=True,blank=True)
    state=models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return self.firstname

class EducationDetail(models.Model):
    degree = models.CharField(max_length=500,blank=False)
    institution = models.CharField(max_length=500,blank=False)
    started = models.DateField(blank=False)
    completed = models.DateField(blank=False)
    score = models.FloatField(blank=True)
    rank = models.CharField(max_length=500,blank=True)

    def __str__(self):
        return self.degree