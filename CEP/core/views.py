from cgitb import html
import site
from django.shortcuts import render, HttpResponse
from core.models import loc
from rest_framework.views import APIView
from django.http import JsonResponse

# Create your views here.



def all_ceps(request):
    cep = loc.objects.all()
    dados = {'ceps': cep}
    return render(request, 'index.html', dados)

def cep_json(request, cep):
    try:
        cep = loc.objects.get(cep=cep)
        dados = {'loc': cep}
        return JsonResponse(status=200, data=dados)
    except:
        dados ={
            "Cep": "Cep nao existe"
        }
        return JsonResponse(status=200, data=dados)