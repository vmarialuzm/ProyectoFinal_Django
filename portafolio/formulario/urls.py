from django.urls import path
from . import views


urlpatterns = [
    #path('',views.Formulario.as_view(),name='formulario'),
    path('crear/',views.CreateProyecto.as_view(), name='crear')
]