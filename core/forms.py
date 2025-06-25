from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, Entrenador

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'role')


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full px-4 py-2 border rounded focus:outline-none focus:ring',
        'placeholder': 'Usuario',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full px-4 py-2 border rounded focus:outline-none focus:ring',
        'placeholder': 'Contraseña',
    }))
    
    


class EntrenadorForms(forms.ModelForm):
    class Meta:
        model : Entrenador