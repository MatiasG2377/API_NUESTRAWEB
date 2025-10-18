from django.db import models

class Galeria(models.Model):
    """
    Representa las imagenes de la galería.
    Atributes:
        titulo: Titulo de la imagen.
        image: Imagen.
        fecha: Fecha en la que se subio la imagen.
    """
    titulo = models.CharField(max_length=200, help_text="Título de la imagen")
    image = models.ImageField(upload_to='img/')
    fecha = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.titulo #Retorna el título de la imagen como representación del objeto.
    
    class Meta:
        indexes = [
            models.Index(fields=['-fecha']),
        ]
        ordering = ['-fecha']
        verbose_name = "Imagen"
        verbose_name_plural = "Galería"



