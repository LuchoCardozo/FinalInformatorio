from datetime import datetime
from django.db import models
from django.utils import timezone


class Evento(models.Model):
    organizador = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    img = models.ImageField(null=True, blank=True, upload_to='img/eventos',help_text="Seleccione una imagen para mostrar")
    creado = models.DateTimeField(default=timezone.now)
    publicado = models.DateTimeField(blank=True, null=True)

    def publicarEvento(self):
        self.publicado = datetime.now()
        self.save()

    def comentariosAprobados(self):
        return self.comentarios.filter(aprobado=True)

