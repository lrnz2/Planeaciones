from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return f"Nombre: {self.nombre}"
