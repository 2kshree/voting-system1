from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import number1,User,voteringlist

class reg_page(UserCreationForm):
    
    username=forms.CharField(widget=forms.TextInput(attrs={'size': '22',"placeholder":"Enter Your Name"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'size': '22',"placeholder": "Enter Your Password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'size': '22',"placeholder": "Enter Your Confirm Password"}))

    class Meta:
        model=User
        fields=['username','password1','password2']

class num(forms.ModelForm):
    aadhaar = forms.IntegerField(widget=forms.TextInput(attrs={'size': '22',"placeholder": "Enter Your Aadhaar Number","width":"100%"}))
    class Meta:
        model=number1
        fields=['aadhaar']

class Voteing(forms.ModelForm):
    class Meta:
        model=voteringlist
        fields='__all__'