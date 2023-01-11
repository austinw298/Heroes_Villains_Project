from django.db import models

# Create your models here.
class SuperType(models.Model):
    typer = models.CharField(max_length=255)