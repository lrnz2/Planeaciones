"""
from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return f"Nombre: {self.nombre}"

class Producto(models.Model):
    sku = models.CharField(max_length=50, primary_key = True, unique = True)
    pasillo = models.IntegerField(null=False)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"SKU: {self.sku} | Pasillo: {self.pasillo} | Precio: {self.precio}"


class Pedido(models.Model):

    class Types(models.TextChoices):
        MASTER = "MSR", "Master"
        PZAS = "PZAS", "Piezas"
        KILOS = "KG", "Kilogramos"

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null = True)
    cantidad = models.IntegerField()
    ubicacion = models.IntegerField()
    zona = models.IntegerField()
    _type = models.CharField(choices= Types.choices, max_length = 15)

    def __str__(self):
        return f"CLIENTE {self.cliente} | PRODUCTO {self.producto} | Cant: {self.cantidad} | Ubi: {self.ubicacion} | Zona: {self.zona} | Typo: {self._type}"


class Planeacion(models.Model):
    clave = models.CharField(max_length=15)
    pedido = models.ForeignKey(Pedido, on_delete = models.CASCADE)
    def __str__(self):
        return f" Clave: {self.clave} | Pedidos: {self.pedido}"

"""