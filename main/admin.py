from django.contrib import admin

from main import models


@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):
    pass
