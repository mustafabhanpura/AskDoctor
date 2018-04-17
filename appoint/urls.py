from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
app_name='appoint'


urlpatterns = [
   path('',views.home_page,name='home_page'),
   path('select/',views.select_login,name='select'),
   path('login/patient/',views.login_user ,name='login_user'),
   path('login/doctor/',views.login_doctor ,name='login_doctor'),
   path('dashboard/patient/query/',views.query_p,name='patient_query'),
   path('dashboard/doctor/',views.dashboard_doctor,name='dashboard-d'),
   path('dashboard/patient/',views.dashboard_patient,name='dashboard-p'),
   path('register/',views.index,name='index'),
   path('display/',views.display_query,name='query'),
   path('detail/', views.display_doctor, name='doc'),
   path('detail/<int:name_id>',views.reply,name='id')
]