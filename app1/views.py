from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.forms import inlineformset_factory
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request,'app1/index.html')

def contact(request):
    form = contact()
    if request.POST:
        form = contact(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message successfully sent to site admin')
            return redirect('home')

    context = {'form':form}
    return render(request,'app1/home.html',context)

def personal(request):
    return render(request,'app1/personal.html')