from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import profile

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model=User

        fields=['username','email','password1','password2']


class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField(required=False)
    
    class Meta:
        model=User

        fields=['username','email']#,'First','Last']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model=profile

        fields=['image']