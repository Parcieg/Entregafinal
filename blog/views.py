from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .models import Usuario, Noticias
from .forms import Loginform

# Create your views here.


def inicio(request):
    return HttpResponse


def usuario(request):
    if request.method == "POST":
        form = Loginform(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            usuario = info["usuario"]
            clave = info["clave"]
            user = authenticate(request, username=usuario, password=clave)
            if user is not None:
                login(request, user)
                return redirect("url")  # definir url

    else:
        form = Loginform()

    return render(request, "login.html", {"form": form})
