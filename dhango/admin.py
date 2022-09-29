from django.contrib import admin

from dhango.models import Device


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    pass
