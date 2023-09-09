from django.urls import path
from .views import inicio, usuario

urlpatterns = [
    path("inicio/", inicio, name="inicio"),
    path("usuario/", usuario, name="usuario"),
]
