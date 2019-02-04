from django.db import models

# Create your models here.
from django.db import models

class Lock(models.Model):
    name = models.CharField(max_length=30)
    bitting_depth = models.FloatField()
