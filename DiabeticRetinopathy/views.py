import base64

import cv2
from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

from DiabeticRetinopathy import blood_vessel_extraction

from DiabeticRetinopathy import forms


# Create your views here.
from DiabeticRetinopathy.forms import RegisterForm, LoginForm, ReportForm
from DiabeticRetinopathy.models import Report


def homeview(request):
    if request.user.is_authenticated:
        if request.method =='POST':
            form = ReportForm(request.POST, request.FILES)
            if form.is_valid():
                report = form.save(commit=False)
                report.save()
                photo = Report.objects.latest('date').photo
                return render(request,'DiabeticRetinopathy/report.html',{'photo':photo})
        form = ReportForm()
        return render(request, 'DiabeticRetinopathy/homeview.html',{'form':form})
    return render(request,'DiabeticRetinopathy/homeview.html')

def user_login(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        user_obj = form.cleaned_data.get('user_obj')
        login(request, user_obj)
        return redirect('DR:homeview')
    return render(request, 'DiabeticRetinopathy/user_login.html', {'form': form})


def user_logout(request):
    logout(request)
    return render(request,'DiabeticRetinopathy/homeview.html')

def register(request):
    if request.method == 'POST' and 'submit' in request.POST:
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            return redirect('DR:homeview')
        else:
            return HttpResponse('{}'.format(form.errors))
    form = RegisterForm()
    return render(request,'DiabeticRetinopathy/register.html',{'form':form})

