from django.db import models


class Data(models.Model):
    start = models.CharField(max_length=5)
    end = models.CharField(max_length=5)
