from django.db import models

# Create your models here.


class DeviceType(models.Model):
    device_type = models.CharField(max_length=64)

    def __str__(self):
        return self.device_type


class ReadingType(models.Model):
    name = models.CharField(max_length=16)
    type = models.CharField(max_length=16)
    bool_true = models.CharField(max_length=32, blank=True)
    bool_false = models.CharField(max_length=32, blank=True)
    unit = models.CharField(max_length=16, null=True, blank=True)

    def __str__(self):
        return self.name


class Device(models.Model):
    device_name = models.CharField(max_length=255, unique=True)
    device_type = models.ForeignKey(DeviceType, on_delete=models.SET_NULL, null=True)
    reading_type = models.ForeignKey(ReadingType, on_delete=models.CASCADE)

    def __str__(self):
        return self.device_name


class Reading(models.Model):
    reading_time = models.DateTimeField()
    reading_timestamp = models.DateTimeField()
    reading_value = models.FloatField()
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

    @property
    def reading_value_human(self):
        if self.device.reading_type.type == 'Boolean':
            return self.device.reading_type.bool_true if self.reading_value else self.device.reading_type.bool_false
        elif self.device.reading_type.type == "Integer":
            return f'{int(self.reading_value)} {self.device.reading_type.unit}'
        else:
            return f'{self.reading_value} {self.device.reading_type.unit}'

    def __str__(self):
        return f"Reading <type = '{self.device.reading_type.name}', value = '{self.reading_value}'>"
