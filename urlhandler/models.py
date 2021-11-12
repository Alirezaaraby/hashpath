from django.db import models


class Data(models.Model):
    switch = models.CharField(max_length=5)
    light = models.CharField(max_length=3)
