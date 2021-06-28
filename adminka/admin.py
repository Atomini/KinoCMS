from django.contrib import admin

# Register your models here.


class AdmnikaArea(admin.AdminSite):
    site_header = "KinoCMS Admin"


adminka_site = AdmnikaArea(name="Admnika")
