from dataclasses import field, fields
from rest_framework import serializers
from SiembrasApp.models import Municipios, Contratistas, Arboles, Veredas, Siembras

class MunicipiosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipios
        fields = ('codigo', 
                  'nombre')

class ContratistasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contratistas
        fields = ('codigo', 
                  'nombre')

class ArbolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arboles
        fields = ('codigo',
                  'nombre')

class VeredasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veredas
        fields = ('codigo',
                  'nombre',
                  'codigo_municipio')

class SiembrasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Siembras
        fields = ('codigo',
                  'codigo_vereda',
                  'codigo_arbol',
                  'codigo_contratista',
                  'fecha',
                  'total_arboles',
                  'total_hectareas')