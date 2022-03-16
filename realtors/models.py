from django.db import models
from datetime import datetime


class RealTor(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    is_mvp = models.BooleanField(default=True)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
