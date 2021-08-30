from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.forms import inlineformset_factory

# Create your views here.


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


# def contact_us(request):
#     form = ContactForm()
#     if request.method == "GET":
#         print("hello peter")
#         form = ContactForm(request.GET)
#         print(request.GET)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Your message successfully sent to site admin')
#             return redirect('/')
#
#     context = {'form':form}
#     return render(request,'app1/index.html',context)


def personal(request):
    return render(request,'app1/personal.html')