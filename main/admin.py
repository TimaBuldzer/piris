from django.contrib import admin

from main import models


@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):
    pass


@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Citizenship)
class CitizenshipAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MaritalStatus)
class MaritalStatusAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Disability)
class DisabilityAdmin(admin.ModelAdmin):
    pass
