from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs= {
                'autocomplete':'text',
                'placeholder':'Логин',
            }
        ),
        required=False
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'autocomplete':"current-password",
                'placeholder':'Пароль',
            }
        ),
        required=False
    )

    error_messages ={
        "invalid_login": (
            "Введите логин или пароль"
        ),
    }

    def clean_password(self):
        password = self.cleaned_data['password']
        if password == '':
            raise forms.ValidationError('Введите пароль', code='invalid')
        return password
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if username == '':
            raise forms.ValidationError('Введите логин', code='invalid')
        if not User.objects.filter(username=username):
            raise forms.ValidationError('Такого пользователя не существует', code='invalid')
        return username
