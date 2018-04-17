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
# Create your views here.
#@login_required(login_url='/login/')



def home_page(request):
    return render(request,'appoint/base_login.html')

@login_required(login_url='appoint:login_doctor')
def dashboard_doctor(request):
    return HttpResponse('<h2>Logged In Successfully Doctor<h2>')


def dashboard_patient(request):
    if request.user.is_authenticated:
       return render(request, 'appoint/dashboard_patient.html')



def query_p(request):
    patient_1=SignUp.objects.get(user=request.user)
    if request.method == 'POST':

        name=patient_1
        query=request.POST.get('query')
        report_image = request.FILES.get('document')
        form=Patient.objects.create(patient=name,reply=query,report_image=report_image)
        form.save()
        return redirect('/appoint/dashboard/patient')

    return render(request, 'appoint/patient_query.html')


def patient_query(request):
    patient_1=SignUp.objects.get(user=request.user)
    if request.method == 'POST' and request.FILES['document']:
        # document = request.FILES['document']
        # fs = FileSystemStorage()
        # filename = fs.save(document.name, document)
        # query_form = Query(request.POST)
        # if query_form.is_valid():
        #     query = query_form.save(commit=False)
        #     reply = query.POST.get('query')
        #     query.reply = reply
        #     query.patient = request.user
        #     query.save()
        query_form = Query(request.POST, request.FILES)
        if query_form.is_valid():
            query = query_form.save(commit=False)
            query.patient = patient_1
            query.report_image = request.FILES.get('document')
            query.reply = request.POST.get('query')
            query.save() 
        return redirect('/appoint/dashboard/patient')
    else:    
        return render(request, 'appoint/patient_query.html')


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
           # user.set_username(username)
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


def display_doctor(request):
    dict = {}
    patient = SignUp.objects.all()
    for x in SignUp.objects.all():
        rep = Patient.objects.filter(patient=x)
        dict[x]=rep

    return render(request, 'appoint/detail.html', {'dict': dict})


def display_query(request):
    sign=SignUp.objects.all().filter(user=request.user)
    query=Patient.objects.all().filter(patient=sign[0])
    return render(request,'appoint/patient.html',{'query':query})
def reply(request,name_id):
    rep=Patient.objects.get(pk=name_id)
    return render(request,'appoint/doctor_view.html',{'rep':rep})