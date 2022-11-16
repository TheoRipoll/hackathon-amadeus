from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms


class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('firstname', 'lastname', 'email', 'username', 'password1', 'password2')
        labels = {'firstname': 'First Name', 'lastname': 'Last Name', 'email': 'Email', 'username': 'Username',
                  'password1': 'Password', 'password2': 'Confirm Password'}


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username')
