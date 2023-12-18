from django.db import models

class Producto(models.Model):
    sku = models.CharField(max_length=50, primary_key = True, unique = True)
    pasillo = models.IntegerField(null=False)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"SKU: {self.sku} | Pasillo: {self.pasillo} | Precio: {self.precio}"
