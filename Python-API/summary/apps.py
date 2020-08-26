from django.apps import AppConfig


class SummaryConfig(AppConfig):
    name = 'summary'

    def ready(self):
        from . import updater
        updater.start_job()

