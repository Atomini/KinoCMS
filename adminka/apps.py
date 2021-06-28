from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig


class AdminkaSiteConfig(AdminConfig):
    default_site = "adminka.admin.AdmnikaArea"


class AdminkaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'adminka'
