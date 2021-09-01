from django.db import models

# Create your models here.


class ContactDetail(models.Model):
    name=models.CharField(default='',max_length=50,null=True,blank=True)
    email=models.EmailField(default='',max_length=50,null=False,blank=False)
    subject=models.CharField(max_length=200)
    message=models.TextField()

    def __str__(self):
        return self.name