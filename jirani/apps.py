from django.apps import AppConfig


class JiraniConfig(AppConfig):
    name = 'jirani'

    def ready(self):
        import jirani.signals