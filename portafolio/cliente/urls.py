from django.urls import path
from . import views

urlpatterns = [
    path('clienteview/',views.ClienteView.as_view(),name='clienteview')
]