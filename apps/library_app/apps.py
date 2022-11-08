from django.apps import AppConfig


class LibraryAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    label = 'library_app'
    name = 'apps.library_app'
