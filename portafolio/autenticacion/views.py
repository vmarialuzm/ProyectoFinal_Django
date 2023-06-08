from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import NewUserForm
from django.views.generic import TemplateView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

class AutenticacionView(LoginRequiredMixin,TemplateView):
  template_name = "prueba.html"
  
class RegisterView(CreateView):
  template_name = "registration/register.html"
  form_class = NewUserForm

  def form_valid(self,form):
    form.save()
    return redirect('login')


