from django.db import models

class Planeacion(models.Model):

    class Status(models.TextChoices):
        PENDIENTE = "Pendiente", "Pendiente"
        EN_PROCESO = "En proceso", "En proceso"
        ENTREGADO = "Entregado", "Entregado"
    clave = models.CharField(max_length=15)
    status = models.CharField(choices= Status.choices, max_length = 15)
    def __str__(self):
        return f" Clave: {self.clave} | Status: {self.status}"

