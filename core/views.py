from django.shortcuts import render
import random

# Create your views here.
def inicio(request):
  return render(request, 'index.html')


def jugar(request):
  '''
    crear contador de preguntas
    crear acumulador de puntaje
    Elegir pregunta al azar
    obtener respuestas y desplegar en pantalla categoría y respuestas
    validar correcta en valor de respuesta
    acumular puntaje
  '''
  pass
