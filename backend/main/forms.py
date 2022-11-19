from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# Creating a form that allows the user to register.
class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('firstname', 'lastname', 'email', 'username', 'password1', 'password2')
        labels = {'firstname': 'First Name', 'lastname': 'Last Name', 'email': 'Email', 'username': 'Username',
                  'password1': 'Password', 'password2': 'Confirm Password'}


# A form that allows the user to login.
class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username')
