from django.db import models

class Galeria(models.Model):
    titulo = models.CharField(max_length=200)
    foto = models.ImageField(upload_to="galeria/")
    fecha_creada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class Fecha(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    razon = models.TextField()

    def __str__(self):
        return f"{self.fecha_creacion} - {self.razon[:20]}..."
