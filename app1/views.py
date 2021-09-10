from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.forms import inlineformset_factory


def home(request):
    form = ContactForm()
    if request.method == "POST":
        print("hello peter")
        form = ContactForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request,'app1/index.html', context)


def personal(request):
    form = PersonalForm()
    if request.method == "POST":
        print("hello peter")
        form = PersonalForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request,'app1/personal.html', context)


def education(request):
    return render(request,'app1/education.html')