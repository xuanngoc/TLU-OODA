from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction


from .models import  User, Subject

class CreateAccount(forms.Form):
    username = forms.CharField(label='username', max_length=15)
    account_type = forms.CharField(label='account_type', max_length=15)
    password = forms.CharField(label='password', max_length=10)


class CreateParticipant(forms.Form):
    participant_name = forms.CharField(label='participant_name', max_length=50)
    email = forms.CharField(label='email', max_length=20)
    phone_number = forms.CharField(label='phone_number', max_length=15)

    username = forms.CharField(label='username', max_length=20)
    #account_type = forms.CharField(label='account_type', max_length=15) // default = is_DonViDuThi
    password = forms.CharField(label='password', max_length=10)

class EditInfoParticipant(forms.Form):
    participant_name = forms.CharField(label='participant_name', max_length=50)
    email = forms.CharField(label='email', max_length=20)
    phone_number = forms.CharField(label='phone_number', max_length=15)


class CreateSubject(forms.Form):
    subject_name = forms.CharField(label='subject_name', max_length=15)

class CreateContest(forms.Form):
    contest_name = forms.CharField(label='contest_name', max_length=40)
    day_start = forms.DateField(label='day_start')
    day_end = forms.DateField(label='day_end')
    #subject = forms.ModelMultipleChoiceField(queryset=Subject.objects.all())

class CreateStudent(forms.Form):
    name = forms.CharField(label='name', max_length=40)
    birthday = forms.CharField(label='birthday', max_length=40)
    gender = forms.CharField(label='gender', max_length=40)
    identity_number = forms.CharField(label='identity_number', max_length=40)
    phone_number = forms.CharField(label='phone_number', max_length=40)

    # school = forms.CharField(label='school', max_length=40)
    # subject = forms.CharField(label='subject', max_length=40)
    #participant = forms.CharField(label='participant', max_length=40)


class CreateSchool(forms.Form):
    name = forms.CharField(label='name', max_length=100)
    address = forms.CharField(label='address', max_length=100)
    website = forms.CharField(label='website', max_length=50)
    email = forms.CharField(label='email', max_length=40)
    phone_number = forms.CharField(label='phone_number', max_length=20) 