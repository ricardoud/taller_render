from django.http import HttpResponse
from django.shortcuts import render
from django.template import *

# Create your views here.

def index(request): return HttpResponse("Hello, world!")
def menu(request): 
    doc_externo=open("C:/Users/ricar/OneDrive/Documentos/ING SISTEMAS/4 SEMESTRE/APLICACIONES EN LA NUBE/pruebapps/helloproject/templates/index.html")
    
    plt=Template(doc_externo.read())
    ctx=Context()
    documento=plt.render(ctx)
    return HttpResponse(documento)

