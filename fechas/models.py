from django.db import models
class Fechas(models.Model):
    """
    Representa fechas especiales.
    Atributes:
        fecha: Fecha y hora del evento.
        titulo: Titulo del evento.
        descripcion_m: Descripcion del evento para Danna.
        descripcion_d: Descripcion del evento para Matías.
    """
    fecha = models.DateTimeField()
    titulo = models.CharField(max_length=200, help_text="Que sucedio en la fecha?")
    descripcion_m = models.TextField(help_text="Descripcion del evento")
    descripcion_d = models.TextField(help_text="Descripcion del evento")

    def __str__(self):
        return f"{self.titulo} - {self.fecha.strftime('%Y-%m-%d %H:%M:%S')}" #Retorna el título y la fecha del evento como representación del objeto.

    class Meta:
        """Configuraciones del modelo Fechas."""
        indexes = [
            models.Index(fields=['fecha']),
        ]        
        constraints = [
            models.UniqueConstraint(
                fields=['fecha'],
                name='fecha_no _repetida',
                condition=models.Q(fecha__isnull=False),       
            )] #Constraint para que no se repitan fechas pero pueda haber fechas nulas.
        ordering = ['-fecha']
        verbose_name = "Fecha Importante"
        verbose_name_plural = "Fechas Importantes"