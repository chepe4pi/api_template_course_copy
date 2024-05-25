from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    emoji = models.CharField(max_length=16, null=True)
