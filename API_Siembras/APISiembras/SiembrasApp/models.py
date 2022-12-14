# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Arboles(models.Model):
    codigo = models.AutoField(primary_key=True, blank=True, null=False)
    nombre = models.TextField(unique=True)

    class Meta:
        managed = False
        db_table = 'arboles'


class Contratistas(models.Model):
    codigo = models.AutoField(primary_key=True, blank=True, null=False)
    nombre = models.TextField(unique=True)

    class Meta:
        managed = False
        db_table = 'contratistas'


class Municipios(models.Model):
    codigo = models.AutoField(primary_key=True, blank=True, null=False)
    nombre = models.TextField()

    class Meta:
        managed = False
        db_table = 'municipios'


class Siembras(models.Model):
    codigo = models.AutoField(primary_key=True, blank=True, null=False)
    codigo_vereda = models.ForeignKey('Veredas', models.DO_NOTHING, db_column='codigo_vereda')
    codigo_arbol = models.ForeignKey(Arboles, models.DO_NOTHING, db_column='codigo_arbol')
    codigo_contratista = models.ForeignKey(Contratistas, models.DO_NOTHING, db_column='codigo_contratista')
    fecha = models.TextField()
    total_arboles = models.IntegerField(blank=True, null=True)
    total_hectareas = models.FloatField()

    class Meta:
        managed = False
        db_table = 'siembras'


class Veredas(models.Model):
    codigo = models.AutoField(primary_key=True, blank=True, null=False)
    nombre = models.TextField()
    codigo_municipio = models.ForeignKey(Municipios, models.DO_NOTHING, db_column='codigo_municipio')

    class Meta:
        managed = False
        db_table = 'veredas'
