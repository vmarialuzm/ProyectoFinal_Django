from django.urls import path
# django tiene un tempalte preparado para le login
# Es decir no provee de la clase LoginView para poder mostrar el formalario de inicio de session
from django.contrib.auth.views import LoginView
from . import views

# Segun el documento de django la url correcta para que funcione debe ser accounts/login/
urlpatterns = [
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('AutenticacionView/', views.AutenticacionView.as_view(),name="index"),
    path('register/',views.RegisterView.as_view(), name='register')
]


"""
LoginView
va a buscar al archivo registration/login
template_name = "registration/login.html"
Esta clase recibe 2 cosas username y password
Dentro de la clase va a verificar que el username y password
ingresados sea correctos 

Para que este funcione hay que seguir ciertas reglas
1: La url se debe llamar: accounts/login/
2: El template de login debe estar en la carpeta registration/login.html
"""