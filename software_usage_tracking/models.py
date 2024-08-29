from django.db import models

# Create your models here.
class SystemMonitor(models.Model):
    objects = None
    system_number = models.CharField(max_length=255)
    user = models.CharField(max_length=255)
    processid = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    software = models.CharField(max_length=255)
    open_time = models.CharField(max_length=255, null=True, blank=True)
    close_time = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.system_number} - {self.software}"