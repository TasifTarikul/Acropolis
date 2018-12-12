from django.apps import AppConfig


class UserprofileappConfig(AppConfig):
    name = 'userProfileApp'

    def ready(self):
        import coreApp.signals
