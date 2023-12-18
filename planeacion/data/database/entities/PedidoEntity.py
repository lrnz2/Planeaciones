from django.db import models
from .ClienteEntity import Cliente
from .ProductoEntity import Producto
from .PlaneacionEntity import Planeacion

class Pedido(models.Model):

    class Types(models.TextChoices):
        MASTER = "Master", "Master"
        PZAS = "Piezas", "Piezas"
        KILOS = "Kg", "Kilogramos"

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null = True)
    cantidad = models.IntegerField()
    ubicacion = models.IntegerField()
    zona = models.IntegerField()
    type = models.CharField(choices= Types.choices, max_length = 15)
    planeacion = models.ForeignKey(Planeacion, on_delete= models.SET_NULL, null = True)

    def __str__(self):
        return f"CLIENTE {self.cliente} | PRODUCTO {self.producto} | Cant: {self.cantidad} | Ubi: {self.ubicacion} | Zona: {self.zona} | Typo: {self.type} | Planeacion: {self.planeacion}"
