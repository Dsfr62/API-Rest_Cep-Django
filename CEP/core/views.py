from cgitb import html
from django.shortcuts import render, HttpResponse
import datetime
from django.http import JsonResponse
import json
from pprint import pprint

# Create your views here.

def info_cep_49045083(request):
    info = '''
    {
        "CEP": "49045-083",
        "Endereco": "Rua Matilde Silva Lima",
        "Numero": "550",
        "Bairro": "Luzia"
    }
    '''
    data = json.loads(info)
    return JsonResponse(data)

def info_cep_49026900(request):
    info = '''
    {
        "CEP": "49026-900",
        "Endereco": "Avenida Ministro Geraldo Barreto Sobral",
        "Numero": "215",
        "Bairro": "Jardins"
    }
    '''
    data = json.loads(info)
    return JsonResponse(data)

def info_cep_49032490(request):
    info = '''
    {
        "CEP": "49032-490",
        "Endereco": "Avenida Murilo Dantas",
        "Numero": "300",
        "Bairro": "Farolandia"
    }
    '''
    data = json.loads(info)
    return JsonResponse(data)