from cgitb import html
from django.shortcuts import render, HttpResponse
from core.models import loc
from django.http import JsonResponse

# Create your views here.

def all_ceps(request):
    cep = loc.objects.all()
    dados = {'ceps': cep}
    return HttpResponse(request, dados)

def cep_json(request, cp):
    try:
        cep = loc.objects.get(cep=cp)
        dados = {
            "Cep": cep.cep,
            "Endereco": cep.endereco,
            "numero": cep.numero,
            "bairro": cep.bairro
        }
        return JsonResponse(status=200, data=dados)
    except:
        dados ={
            "Cep": "Cep nao existe",
            "aa": "aa"
            
        }
        return JsonResponse(status=200, data=dados)
        