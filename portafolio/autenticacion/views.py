from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import NewUserForm
from django.views.generic import View,CreateView

class AutenticacionView(View):
  def get(self,request):
    return HttpResponse(" Hola soy una clase de la aplicacion autenticacion")
  
class RegisterView(CreateView):
  template_name = "registration/register.html"
  form_class = NewUserForm

  def form_valid(self,form):
    form.save()
    return redirect('login')


