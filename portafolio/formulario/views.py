from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Proyecto
from django.views.generic import FormView,View
from .forms import ProyectoForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

class CreateProyecto(LoginRequiredMixin,FormView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = "form.html"

    #Para guardar la informacion existe esta función 
    def form_valid(self, form):
        #cleaned_data es el objeto que tiene toda la info que hemos llenado en el formulario
        Proyecto.objects.create(**form.cleaned_data)
        return redirect('formulario')
    
    def form_invalid(self,form):
        messages.error(self.request,'Por favor, completa todos los campos requeridos')
        return super().form_invalid(form)
        

class Formulario(View):
    def get(self,request):
        proyectos = Proyecto.objects.all()
        context = {"proyectos": proyectos}
        return render(request, "formulario.html", context)

