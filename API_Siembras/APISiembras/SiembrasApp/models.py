from django.db import models

# Create your models here.

class municipios:
    codigo = models.IntegerField(db_column='codigo',primary_key = True)
    nombre = models.CharField()

class arboles:
    codigo = models.AutoField(db_column='codigo',primary_key = True)
    nombre = models.CharField()

class contratistas:
    codigo = models.AutoField(db_column='codigo',primary_key = True)
    nombre = models.CharField()

class veredas:
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField()
    codigo_municipio = models.IntegerField()

class siembras:
    codigo = models.AutoField(primary_key=True)
    codigo_vereda = models.IntegerField()
    codigo_arbol = models.IntegerField()
    codigo_contratista = models.IntegerField()
    fecha = models.CharField()
    total_arboles = models.IntegerField()
    total_hectareas = models.IntegerField()