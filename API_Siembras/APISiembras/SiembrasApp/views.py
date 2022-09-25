from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from SiembrasApp.models import Municipios, Veredas, Arboles, Contratistas, Siembras
from SiembrasApp.serializers import MunicipiosSerializer, SiembrasSerializer, VeredasSerializer, ArbolesSerializer, ContratistasSerializer, SiembrasSerializer

# Create your views here.
@csrf_exempt
def municipiosApi(request, id=0):
    if request.method == 'GET':
        municipios = Municipios.objects.all()
        municipios_serializer = MunicipiosSerializer(municipios, many=True)
        return JsonResponse(municipios_serializer.data, safe=False)
    else:
        print("error")

def arbolesApi(request, id=0):
    if request.method == 'GET':
        arboles = Arboles.objects.all()
        arboles_serializer = ArbolesSerializer(arboles, many=True)
        return JsonResponse(arboles_serializer.data, safe=False)
    else:
        print("error")

def contratistasApi(request, id=0):
    if request.method == 'GET':
        contratistas = Contratistas.objects.all()
        contratistas_serializer = ContratistasSerializer(contratistas, many=True)
        return JsonResponse(contratistas_serializer.data, safe=False)
    else:
        print("error")

def veredasApi(request, id=0):
    if request.method == 'GET':
        veredas = Veredas.objects.all()
        veredas_serializer = VeredasSerializer(veredas, many=True)
        return JsonResponse(veredas_serializer.data, safe=False)
    else:
        print("error")

def siembrasApi(request, id=0):
    if request.method == 'GET':
        siembras = Siembras.objects.all()
        siembras_serializer = SiembrasSerializer(siembras, many=True)
        return JsonResponse(siembras_serializer.data, safe=False)
    else:
        print("error")
