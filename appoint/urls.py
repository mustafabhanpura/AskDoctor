from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
app_name='appoint'


urlpatterns = [
   path('',views.select_login,name='select'),
   path('login/patient/',views.login_user ,name='login_user'),
   path('login/doctor/',views.login_doctor ,name='login_doctor'),
   path('dashboard/patient/query/',views.query_p,name='patient_query'),
   path('dashboard/doctor/',views.display_doctor,name='dashboard-d'),
   path('dashboard/patient/',views.dashboard_patient,name='dashboard-p'),
   path('dashboard/patient/AboutUs',views.about_us,name='about_us'),
   path('dashboard/patient/logout',views.logout_view,name='logout_view'),
   path('dashboard/patient/status',views.reply_status,name='reply_status'),
   path('register/',views.index,name='index'),
   path('detail/', views.display_doctor, name='doc'),
   path('dashboard/doctor/profile/<int:name_id>',views.reply_profile,name='id_profile'),
   path('dashboard/doctor/query/<int:name_id>',views.reply_query,name='id_query'),
   path('dashoard/clear/',views.clear,name='clear'),
   path('dashboard/patient/none/',views.none,name='none'),
]