from planeacion.data.database.dao.PedidoDao import PedidoDao
from planeacion.data.database.entities.PedidoEntity import Pedido

class PedidoRepository():
    
    @staticmethod
    def obtenerPedidosDeBD():
        response:list[Pedido] = PedidoDao.obtenerPedidos()
        return response
    
    @staticmethod
    def crearPedidoEnBD( cliente_id:int, producto_sku:int, cantidad:int,
            ubicacion:int, zona:int, _type:str):
        PedidoDao.crearPedido( cliente_id = cliente_id, producto_sku=producto_sku, cantidad=cantidad,
            ubicacion=ubicacion, zona=zona, _type=_type)
    
    @staticmethod
    def actualizarPedidoEnBD(id:str, cliente_id:int, producto_sku:int, cantidad:int,
            ubicacion:int, zona:int, _type:str):
        PedidoDao.actualizarPedido(id = id, cliente_id = cliente_id, producto_sku=producto_sku, cantidad=cantidad,
            ubicacion=ubicacion, zona=zona, _type=_type)
    
    @staticmethod
    def eliminarPedidoEnBD(id: str):
        PedidoDao.eliminarPedido(id)


    @staticmethod
    def obtenerPedidosSinPlaneacionDeBD():
        PedidoDao.obtenerPedidosSinPlaneacion()

    @staticmethod
    def obtenerPedidosConPlaneacionDeBD(planeacion_id):
        return PedidoDao.obtenerPedidosConPlaneacion(planeacion_id=planeacion_id)

           
    @staticmethod
    def actualizarPlaneacionDePedidoEnBD(id:int, planeacion_id):
        PedidoDao.actualizarPlaneacionDePedido(id=id, planeacion_id = planeacion_id)