from django.shortcuts import render
from .models import Proyecto

def formulario(request):
    proyectos = Proyecto.objects.all()
    context = {
        "proyectos": proyectos
    }
    return render(request, "formulario.html", context)
