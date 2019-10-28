from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Reading)
admin.site.register(Device)
admin.site.register(DeviceType)
admin.site.register(ReadingType)
