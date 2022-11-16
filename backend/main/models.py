from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    email = models.EmailField(_('email'), unique=True, blank=False, null=False,
                              error_messages={'unique': 'A user with that email already exists.'},
                              help_text='Required. Enter a valid email address.')
    firstname = models.CharField(max_length=30, blank=True, null=True, help_text='Optional.', verbose_name='First Name')
    lastname = models.CharField(max_length=30, blank=True, null=True, help_text='Optional.', verbose_name='Last Name')
