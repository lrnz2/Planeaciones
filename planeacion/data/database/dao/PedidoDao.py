from planeacion.data.database.entities.PedidoEntity import Pedido
from planeacion.data.database.entities.PlaneacionEntity import Planeacion

class PedidoDao():

    @staticmethod
    def obtenerPedidos():
        return Pedido.objects.all()

    @staticmethod
    def crearPedido( cliente_id:int, producto_sku:int, cantidad:int,
            ubicacion:int, zona:int, _type:str):
        Pedido( cliente_id = cliente_id, producto_id=producto_sku, cantidad=cantidad,
            ubicacion=ubicacion, zona=zona, type=_type).save()
    
    @staticmethod
    def actualizarPedido(id:int, cliente_id:int, producto_sku:int, cantidad:int,
            ubicacion:int, zona:int, _type:str):
        Pedido.objects.filter(id = id).update(cliente_id = cliente_id, producto_id=producto_sku, cantidad=cantidad,
            ubicacion=ubicacion, zona=zona, type=_type)

    @staticmethod
    def eliminarPedido(id: str):
        Pedido.objects.get(id = id).delete()


    @staticmethod
    def obtenerPedidosSinPlaneacion():
        return Pedido.objects.filter(planeacion = None)

    @staticmethod
    def obtenerPedidosConPlaneacion(planeacion_id):
        return Pedido.objects.filter(planeacion__id = planeacion_id)
           
    @staticmethod
    def actualizarPlaneacionDePedido(id:int, planeacion_id):
        Pedido.objects.filter(id = id).update(planeacion_id = planeacion_id)
    