from django.apps import AppConfig


class ApiConfig(AppConfig):
    name = 'api'
    default_auto_field = 'django.db.models.AutoField'

    # class AutoField(AutoField):
    #     AutoField = 'django.db.models.BigAutoField'
