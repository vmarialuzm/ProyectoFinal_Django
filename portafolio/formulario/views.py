from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Proyecto
from django.views.generic import FormView,View
from .forms import ProyectoForm

class CreateProyecto(FormView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = "form.html"

    #Para guardar la informacion existe esta función 
    def form_valid(self, form):
        #cleaned_data es el objeto que tiene toda la info que hemos llenado en el formulario
        Proyecto.objects.create(**form.cleaned_data)
        return redirect('formulario')
    
    def form_invalid(self, form):
        print("errors", form.errors)
        return redirect('formulario')

class Formulario(View):
    def get(self,request):
        proyectos = Proyecto.objects.all()
        context = {"proyectos": proyectos}
        return render(request, "formulario.html", context)

