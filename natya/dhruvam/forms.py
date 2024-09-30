from django import forms
from .models import *
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django.forms import modelformset_factory
from django.utils import timezone
from .models import *

class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':' ','placeholder':'Enter Confirm Password'}),label='Confirm Password')


    class Meta:
        model =Register
        fields = ['username', 'email', 'phone',  'password','image',]
        
        help_texts = {
            'username': None
            }

        widgets = {
            "username" : forms.TextInput(attrs={'class':' name','placeholder':'Enter your Username'}),
            "email" : forms.EmailInput(attrs={'class':' email','placeholder':'Enter your Email'}),
            "password" : forms.PasswordInput(attrs={'class':' ','placeholder':'Enter Password'}),
            "confirm_password" : forms.PasswordInput(attrs={'class':' ','placeholder':'Enter Confirm Password'}),
            "phone" : forms.TextInput(attrs={'class':'','maxlength':'10','placeholder':'Enter your Phone number'}),
            'image': forms.ClearableFileInput(attrs={'multiple': False}),
            }
        
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise ValidationError('Passwords do not match')

        return cleaned_data




class GuruRegistrationForm(forms.ModelForm):
  
    image = forms.ImageField(
        widget=forms.FileInput(attrs={'class': 'form-control-file'}),
        label="Upload Guru Image",
    )
    DANCE_STYLE_CHOICES = [
        ('', 'Select Dance Style'),
        ('bharatanatyam', 'Bharatanatyam'),
        ('kathak', 'Kathak'),
        ('kuchipudi', 'Kuchipudi'),
        ('odissi', 'Odissi'),
        ('mohiniyattam', 'Mohiniyattam'),
    ]
    
    dance_style = forms.ChoiceField(
        choices=DANCE_STYLE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control text-dark'}),
        label="Select Dance Style",
    )
    dance_specialization = forms.ChoiceField(
        choices=Register.SPECIALIZATIONS,
        widget= forms.Select(attrs={'class':'select-with-icon text-dark'}),
    )


    class Meta:
        model = Register
        fields = ['username', 'email', 'password', 'phone', 'image', 'experience', 'dance_style', 'dance_specialization', 'profile_information']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}),
            'phone': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Enter your phone'}),
            'experience': forms.Textarea(attrs={'class': 'form-control ta', 'placeholder': 'Enter your experience'}),
            'profile_information': forms.Textarea(attrs={'class': 'form-control ta', 'placeholder': 'Enter your profile information'}),
        }


class LoginForm(forms.ModelForm):
    class Meta:
        model =Register
        fields = ['username', 'password']

        widgets ={

            "username" :  forms.TextInput(attrs={'class':' name','placeholder':'Enter your Username'}),
            "password" : forms.PasswordInput(attrs={'class':' ','placeholder':'Enter Password'}),
        }
        
        help_texts = {
            'username': None
            }
        
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['email', 'phone', 'image']
        widgets = {
            "email": forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Email'}),
            "phone": forms.TextInput(attrs={'class': 'form-control', 'maxlength': '10', 'placeholder': 'Enter your Phone number'}),
            'profile_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        
# class ResetPassword(forms.ModelForm):
#     class meta:
#         model=Register
#         fields = ['password']
#         help_texts = {
#             'password': None
#             }
#         widgets={

#             'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'New Password'}),
#         }

from django.contrib.auth.forms import PasswordChangeForm
from django import forms

class ResetPassword(PasswordChangeForm):
    class Meta:
        model = Register  # This is optional, usually not required for PasswordChangeForm
        fields = ['new_password1', 'new_password2']
        widgets = {
            'new_password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'New Password'}),
            'new_password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm New Password'}),
        }
        help_texts = {
            'new_password1': 'Your password can’t be too similar to your other personal information. Your password must contain at least 8 characters. Your password can’t be a commonly used password. Your password can’t be entirely numeric.',
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
           
        }

class DanceClassForm(forms.ModelForm):
    class Meta:
        model = DanceClass
        fields = ['title', 'video_title', 'video_link', 'image', 'dance_style', 'description']
        widgets = {
            'title': forms.Textarea(attrs={'rows': 2, 'cols': 65}),
            'video_title': forms.Textarea(attrs={'rows': 5, 'cols': 65}),
            'video_link': forms.Textarea(attrs={'rows': 5, 'cols': 65}),
            'dance_style': forms.Select(choices=DanceClass.DANCE_STYLES),
            'description': forms.Textarea(attrs={'rows': 8, 'cols': 65}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }