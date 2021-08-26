from .models import *
from django.forms import ModelForm
from django import forms

class contact(ModelForm):
    class Meta:
        model = Contact_Detail
        fields = ["name", "email","subject","message"]