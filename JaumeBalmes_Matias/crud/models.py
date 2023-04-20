from django.db import models

# Create your models here.
    # Campos
class Person(models.Model):
    nom = models.CharField(max_length=30)
    cognom = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    age = models.CharField(max_length=2)
    Equipo = models.CharField(max_length=30)
    Seleccion = models.CharField(max_length=30)
