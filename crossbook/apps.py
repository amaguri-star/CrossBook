from django.apps import AppConfig


class CrossbookConfig(AppConfig):
    name = 'crossbook'

    def ready(self):
        import crossbook.signals
