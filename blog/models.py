from django.db import models
from django.utils import timezone

# Create your models here.


class Noticias(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="noticias/", null=True, blank=True)

    def __str__(self):
        return f"{self.titulo}"


class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    clave = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre}"

    def crear_noticia(self, titulo, contenido):
        return Noticias.objects.create(titulo=titulo, contenido=contenido, autor=self)
