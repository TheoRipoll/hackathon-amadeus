from django.apps import AppConfig


# Setting the default auto field to BigAutoField.
class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'
