from django.contrib import admin
from .models import Device, RepairLog

admin.site.register(Device)
admin.site.register(RepairLog)