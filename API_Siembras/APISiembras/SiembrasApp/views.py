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

@csrf_exempt
def arbolesApi(request, id=0):
    if request.method == 'GET':
        arboles = Arboles.objects.all()
        arboles_serializer = ArbolesSerializer(arboles, many=True)
        return JsonResponse(arboles_serializer.data, safe=False)
    else:
        print("error")

@csrf_exempt
def contratistasApi(request, id=0):
    if request.method == 'GET':
        contratistas = Contratistas.objects.all()
        contratistas_serializer = ContratistasSerializer(contratistas, many=True)
        return JsonResponse(contratistas_serializer.data, safe=False)
    else:
        print("error")

@csrf_exempt
def veredasApi(request, id=0):
    if request.method == 'GET':
        veredas = Veredas.objects.all()
        veredas_serializer = VeredasSerializer(veredas, many=True)
        return JsonResponse(veredas_serializer.data, safe=False)
    else:
        print("error")

@csrf_exempt
def siembrasApi(request, id=0):
    if request.method == 'GET':
        siembras = Siembras.objects.all()
        siembras_serializer = SiembrasSerializer(siembras, many=True)
        return JsonResponse(siembras_serializer.data, safe=False)
    elif request.method == 'POST':
        siembras_data = JSONParser().parse(request)
        siembras_serializer = SiembrasSerializer(data=siembras_data)
        if siembras_serializer.is_valid():
            siembras_serializer.save()
            return JsonResponse("Siembra agregada exitosamente", safe=False)
        return JsonResponse("Error al agregar siembra", safe=False)
    elif request.method == 'PUT':
        siembras_data = JSONParser().parse(request)
        siembras = Siembras.objects.get(codigo=siembras_data['codigo'])
        siembras_serializer = SiembrasSerializer(siembras,data=siembras_data)
        if siembras_serializer.is_valid():
            siembras_serializer.save()
            return JsonResponse("Siembra actualizada exitosamente", safe=False)
        return JsonResponse("Error al actualizar siembra", safe=False)
    elif request.method == 'DELETE':
        siembras = Siembras.objects.get(codigo=id)
        siembras.delete()
        return JsonResponse("Siembra eliminada exitosamente", safe=False)
    else:
        print("error")
