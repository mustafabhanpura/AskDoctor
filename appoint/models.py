from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class SignUp(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,default=None)
    first_name=models.CharField(max_length=50,blank=True)
    last_name=models.CharField(max_length=50,blank=True)
    contact=models.CharField(max_length=10,help_text='Enter the mobile number only')
    date_of_birth=models.DateField(null=True,blank=True)
    time_of_reg=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.first_name+' '+self.last_name

class Patient(models.Model):
    patient=models.ForeignKey(SignUp,on_delete=models.CASCADE)
    reply=models.TextField(max_length=400)
    report_image=models.FileField(upload_to="report/")
    medicine = models.CharField(max_length=100)
    answer = models.TextField(max_length=400)

    def __str__(self):
        return self.reply
