import base64
from fastai.vision import *


from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect



# Create your views here.
from DiabeticRetinopathy.forms import RegisterForm, LoginForm, ReportForm
from DiabeticRetinopathy.models import Report
from .render import Render




def homeview(request):
    global load_learner
    if not request.user.is_authenticated:
        if request.method == 'POST' and 'register' in request.POST:
            registerform = RegisterForm(request.POST)
            if registerform.is_valid():
                user = registerform.save()
                new_user = authenticate(email=registerform.cleaned_data['email'],
                                        password=registerform.cleaned_data['password1'],
                                        )
                login(request, new_user)
                return redirect('DR:homeview')
            else:
                return HttpResponse('{}'.format(registerform.errors))
        elif request.method == 'POST' and 'login' in request.POST:
            loginform = LoginForm(request.POST)
            if loginform.is_valid():
                user_obj = loginform.cleaned_data.get('user_obj')
                login(request, user_obj)
                return redirect('DR:homeview')
        else:
            loginform = LoginForm()
            registerform = RegisterForm()
            return render(request,'DiabeticRetinopathy/login.html',{'loginform': loginform, 'registerform':registerform})
    else:
        if request.method == 'POST':
            if 'upload' in request.POST:
                reportform = ReportForm(request.POST, request.FILES)
                if reportform.is_valid():
                    report = reportform.save()
                    photo = Report.objects.latest('date').photo
                    learn = load_learner('')
                    category = learn.predict(open_image(photo.path))[0]
                    request.session['category'] = category.__int__()
                    return render(request,'DiabeticRetinopathy/report.html',{'photo':photo,'category':category})
            if 'Download' in request.POST:
                report = Report.objects.latest('date')
                params = {
                'first_name'    : report.first_name,
                'last_name'     : report.last_name,
                'age'           : report.age,
                'gender'        : report.gender,
                'photo'         : report.photo,
                'date1'         : report.date,
                'category'      : request.session.get('category')
                }
                return Render.render('DiabeticRetinopathy/pdf.html', params)
        reportform = ReportForm()
        return render(request,'DiabeticRetinopathy/upload.html',{'reportform':reportform})


    # if request.user.is_authenticated:
    #     if request.method =='POST':
    #         if 'Download' in request.POST:
    #             report = Report.objects.latest('date')
    #             params = {
    #                 'first_name'    : report.first_name,
    #                 'last_name'     : report.last_name,
    #                 'age'           : report.age,
    #                 'photo'         : report.photo,
    #                 'date1'         : report.date,
    #                 'category'      : request.session.get('category')
    #             }
    #             return Render.render('DiabeticRetinopathy/pdf.html', params)
    #         form = ReportForm(request.POST, request.FILES)
    #         if form.is_valid():
    #             report = form.save(commit=False)
    #             report.save()
    #             photo = Report.objects.latest('date').photo
    #             learn = load_learner('')
    #             category = learn.predict(open_image(photo.path))[0]
    #             print(type(category))
    #             request.session['category'] = category.__int__()
    #
    #             learn = load_learner('')
    #             category = learn.predict(open_image(photo.path))[0]
    #             return render(request,'DiabeticRetinopathy/report.html',{'photo':photo,'category':category})
    #     form = ReportForm()
    #     return render(request, 'DiabeticRetinopathy/homeview.html',{'form':form})
    # return render(request,'DiabeticRetinopathy/homeview.html')

# def user_login(request):
#     form = LoginForm(request.POST or None)
#     if form.is_valid():
#         user_obj = form.cleaned_data.get('user_obj')
#         login(request, user_obj)
#         return redirect('DR:homeview')
#     return render(request, 'DiabeticRetinopathy/user_login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('DR:homeview')

# def register(request):
#     if request.method == 'POST' and 'submit' in request.POST:
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#
#             return redirect('DR:homeview')
#         else:
#             return HttpResponse('{}'.format(form.errors))
#     form = RegisterForm()
#     return render(request,'DiabeticRetinopathy/register.html',{'form':form})
#

def teamview(request):
    return render(request,'DiabeticRetinopathy/team.html')