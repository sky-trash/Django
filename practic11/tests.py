from django.test import TestCase
from .forms import RegisterForm
from django.urls import reverse 
from django.contrib.auth.models import User

class TestCaseViewAccount(TestCase):
    def setUp(self) -> None:
        self.form_data = {
            'username':'тест',
            'email':'test@gmail.com',
            'password1': '~{C%eA21',
            'password2': '~{C%eA21'
        }

    def test_register_view(self):
        RegisterForm(data=self.form_data)
        self.client.post(reverse('register'), data=self.form_data)
        print(self.form_data['email'])
        user = User.objects.filter(username=self.form_data['username']).exists()
        self.assertTrue(user)