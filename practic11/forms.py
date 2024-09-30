from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.validators import RegexValidator

class RegisterForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'autocomplete': 'text',
                'placeholder':'Введите логин',
            }
        ),
        required=False,
        validators=[RegexValidator(r'[0-9а-яA-ЯёЁ]',"Введите логин ")], 
    )
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'autocomplete':'email',
            'placeholder':'Введите почту'
        }
        ), required=False
    )
    password1= forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Введите пароль'
            }
        ),
    )
    password2= forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Повторите пароль'
            }
        ),
    )
    
    def clean_password(self):
        password = self.cleaned_data['password1']
        if password == '':
            raise forms.ValidationError('Введите пароль', code='invalid')
        return password
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if username == '':
            raise forms.ValidationError('Введите логин', code='invalid')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if email == '':
            raise forms.ValidationError('Введите пароль', code='invalid')
        return email

class Meta(UserCreationForm.Meta):
    fields = ("username", "name", "password1", "password2")