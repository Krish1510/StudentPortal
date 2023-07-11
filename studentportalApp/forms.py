from django import forms
from . models import *
from datetime import *
from django.contrib.auth.forms import UserCreationForm


class NotesForm(forms.ModelForm):
    title=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Title'}))
    description=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Enter Description'}))
    class Meta:
        model=Notes
        fields=['title','description']
    
class DateInput(forms.DateInput):
    input_type='date'

class HomeworkForm(forms.ModelForm):
    subject=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Subject'}))
    title=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Title'}))
    description=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Enter Description'}))
    # due = forms.DateField(
    #     widget=forms.DateInput(
    #         attrs={'class': 'datepicker'},
    #         format='%d/%m/%Y',
    #     ),
    #     input_formats=['%d/%m/%Y'],
    # )
    # is_finished=forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'my-checkbox'}) )

    class Meta:
        model=HomeWork
        widgets={'due':DateInput()}
        fields=['subject','title','description','due','is_finished']


class DashboardForm(forms.Form):
    text=forms.CharField(max_length=200,label="Enter your search")


class UserRegistrationForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Email'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Passsword'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Confirm Password'}))
    class Meta:
        model=User
        fields=['username','email','password1','password2']