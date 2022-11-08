from django.apps import AppConfig


class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'

    # default
    # name = base

    # if the app is in a specific folder (apps in this case)
    label = 'base'
    name = 'apps.base'

    def ready(self):
        import apps.base.signals
