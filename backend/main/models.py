from django.contrib.auth.models import AbstractUser
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _


# Creating a custom user model.
class CustomUser(AbstractUser):
    email = models.EmailField(_('email'), unique=True, blank=False, null=False,
                              error_messages={'unique': 'A user with that email already exists.'},
                              help_text='Required. Enter a valid email address.')
    firstname = models.CharField(max_length=30, blank=True, help_text='Optional.', verbose_name='First Name')
    lastname = models.CharField(max_length=30, blank=True, help_text='Optional.', verbose_name='Last Name')


# Creating a class called Place that inherits from the Model class.
class Place(models.Model):
    # Used to change the name of the model in the admin panel.
    class Meta:
        verbose_name_plural = 'Places'
        verbose_name = 'Place'

    # Creating the fields for the model.
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    favourites = models.ManyToManyField(CustomUser, related_name='favourites', blank=True)
    slug = models.SlugField(blank=True, null=True)

    # Creating a slug for the place.
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Place, self).save(*args, **kwargs)

    # Returning the name of the place.
    def __str__(self):
        return self.name

    # Returning the url of the place.
    def get_absolute_url(self):
        return f"/places/{self.slug}"
