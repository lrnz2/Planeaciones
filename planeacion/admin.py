from django.contrib import admin

from planeacion.data.database.entities.ClienteEntity import Cliente
from planeacion.data.database.entities.ProductoEntity import Producto
from planeacion.data.database.entities.PedidoEntity import Pedido
from planeacion.data.database.entities.PlaneacionEntity import Planeacion

admin.site.register(Planeacion)
admin.site.register(Pedido)
admin.site.register(Cliente)
admin.site.register(Producto)