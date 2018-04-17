# Generated by Django 2.0.1 on 2018-04-01 13:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=50)),
                ('contact', models.CharField(help_text='Enter the mobile number only', max_length=10)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('time_of_reg', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
