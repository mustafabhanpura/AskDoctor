from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect,render_to_response
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.template import RequestContext
from .models import SignUp, Patient
from .forms import Sign, Profile, Query
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.
#@login_required(login_url='/login/')



def home_page(request):
    return render(request,'appoint/base_login.html')


def logout_view(request):
    logout(request)
    return redirect('/appoint/login/patient/')


def about_us(request):
    return render(request, 'appoint/about_us.html')


@login_required(login_url='appoint:login_user')
def dashboard_patient(request):
    sign=SignUp.objects.get(user=request.user)
    return render(request, 'appoint/dashboard_patient.html',{'user':sign})


@login_required(login_url='appoint:login_user')
def query_p(request):
    patient_1 = SignUp.objects.get(user=request.user)
    if request.method == 'POST':
        name=patient_1
        query=request.POST.get('query')
        report_image = request.FILES.get('document')
        form=Patient.objects.create(patient=name,reply=query,report_image=report_image)
        form.save()
        return redirect('/appoint/dashboard/patient')
    return render(request, 'appoint/patient_query.html')

def none(request):
    return render(request,'appoint/none.html')


@login_required(login_url='appoint:login_user')
def reply_status(request):
    x = SignUp.objects.get(user=request.user)
    patient = Patient.objects.get(patient=x)

    if patient :
        pat = Patient.objects.get(patient=x)
        return render(request, 'appoint/check_status.html', {'patient':pat,'x':x})
    else:
        return render(request,'appoint/none.html')
        

def select_login(request):
    return render(request, 'appoint/select.html')


def index(request):
    if request.method=='POST':
        user_form=Sign(request.POST)
        profile_1=Profile(request.POST)

        if user_form.is_valid() and profile_1.is_valid():
            user=user_form.save(commit=False)
            username=user_form.cleaned_data['username']
            password=user_form.cleaned_data['password']
            user.set_password(password)
            user.save()
            profile_1=profile_1.save(commit=False)
            profile_1.user=user
            profile_1.save()
            login(request, authenticate(username=username, password=password))
            return redirect('/appoint/dashboard/patient')
    else:
            user_form=Sign()
            profile_1=Profile()
    return render(request,'appoint/patient_register.html',{'user_form':user_form,'profile_1':profile_1})


def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                patient_id=user.id
                login(request, user)
                return redirect('/appoint/dashboard/patient/')
    return render(request,'appoint/login_patient.html')


def login_doctor(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST.get('name')
        password = request.POST.get('pswd')
        if username=="doctor" and password=="myclinic" :
            return redirect('/appoint/dashboard/doctor/')
    return render(request,'appoint/login_doctor.html')


#@login_required(login_url='/appoint/login/doctor/')
def display_doctor(request):
    dict = {}
    patient = SignUp.objects.all()
    for x in SignUp.objects.all():
        rep = Patient.objects.filter(patient=x)
        dict[x]=rep

    return render(request, 'appoint/detail.html', {'dict': dict})


def reply_profile(request,name_id):
    sign=SignUp.objects.get(id=name_id)
    return render(request,'appoint/patient_profile.html',{'sign':sign})

def reply_query(request,name_id):
    doc=Patient.objects.get(id = name_id)
    if request.method == 'POST':
        doc.answer=request.POST.get('answer')
        doc.medicine = request.POST.get('medicine')
        doc.save()
        return redirect('/appoint/dashboard/doctor/')
    else:
        query=Patient.objects.get(id=name_id)
        return render(request,'appoint/patient_problem.html',{'query':query})



def clear(request):
    sign=SignUp.objects.get(user=request.user)
    Patient.objects.filter(patient=sign).delete()
    # pat.reply=''
    # pat.answer=''
    # pat.report_image=''
    # pat.save()
    #pat.delete()
    return redirect('/appoint/dashboard/patient/')