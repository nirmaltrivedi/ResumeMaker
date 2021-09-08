from .models import *
from django.forms import ModelForm
from django import forms


class ContactForm(ModelForm):

    class Meta:
        model = ContactDetail
        fields = '__all__'

class PersonalForm(ModelForm):

    class Meta:
        model = PersonalDetail
        fields = '__all__'
