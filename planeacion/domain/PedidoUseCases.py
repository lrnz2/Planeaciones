
from planeacion.data.database.entities.PedidoEntity import Pedido
from planeacion.data.repository.PedidoRepository import PedidoRepository

from planeacion.domain.model.RespuestaOperacion import RespuestaOperacion

class PedidoUseCases():
    
    @staticmethod
    def obtenerPedidosUseCase() -> list[Pedido]:
        respuesta: RespuestaOperacion = RespuestaOperacion()
        try:
            respuesta.contenido: list[Pedido] = PedidoRepository.obtenerPedidosDeBD()
        except Pedido.DoesNotExist as error:
            print("ERROR:obtenerPedidosUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "No hay registros"
            respuesta.contenido = []
        except Exception as error:
            print("ERROR:obtenerPedidosUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "Ha ocurrido un error en el sistema"
            respuesta.contenido = []

        return respuesta
    
    @staticmethod
    def obtenerPedidoUseCase(id:str) -> Pedido:
        respuesta: RespuestaOperacion = RespuestaOperacion()
        try:
            respuesta.contenido: Pedido = PedidoRepository.obtenerPedidoDeBD(id=id)
        except Pedido.DoesNotExist as error:
            print("ERROR:obtenerPedidosUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "No hay registros"
            respuesta.contenido = []
        except Exception as error:
            print("ERROR:obtenerPedidosUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "Ha ocurrido un error en el sistema"
            respuesta.contenido = []

        return respuesta
    
    @staticmethod
    def crearPedidoUseCase(cliente_id:int, producto_sku:int, cantidad:int,
            ubicacion:int, zona:int, _type:str):
        
        respuesta: RespuestaOperacion = RespuestaOperacion()

        try:
            PedidoRepository.crearPedidoEnBD(cliente_id = cliente_id, producto_sku=producto_sku, cantidad=cantidad,
            ubicacion=ubicacion, zona=zona, _type=_type)
            respuesta.mensaje = "Pedido creado exitosamente"
        except Exception as error:
            print("ERROR:crearPedidoUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "Operación fallida"

        return respuesta
    
    @staticmethod
    def actualizarPedidoUseCase(id: str, cliente_id:int, producto_sku:int, cantidad:int,
            ubicacion:int, zona:int, _type:str):
        
        respuesta: RespuestaOperacion = RespuestaOperacion()

        try:
            PedidoRepository.actualizarPedidoEnBD(id = id, cliente_id = cliente_id, producto_sku=producto_sku, cantidad=cantidad,
            ubicacion=ubicacion, zona=zona, _type=_type)
            respuesta.mensaje = "Pedido actualizado exitosamente"
        except Exception as error:
            print("ERROR:actualizarPedidoUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "Operación fallida"
            
        return respuesta
    
    @staticmethod
    def eliminarPedidoUseCase(id: str):
        respuesta: RespuestaOperacion = RespuestaOperacion()
        try:
            PedidoRepository.eliminarPedidoEnBD(id)
            respuesta.mensaje = "Pedido eliminado exitosamente"
        except Exception as error:
            print("ERROR:eliminarPedidoUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "Operación fallida"

        return respuesta

    @staticmethod
    def obtenerPedidosSinPlaneacionUseCase() -> list[Pedido]:
        respuesta: RespuestaOperacion = RespuestaOperacion()
        try:
            respuesta.contenido: Pedido = PedidoRepository.obtenerPedidosSinPlaneacionDeBD()
        except Pedido.DoesNotExist as error:
            print("ERROR:obtenerPedidosSinPlaneacionUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "No hay registros"
            respuesta.contenido = []
        except Exception as error:
            print("ERROR:obtenerPedidosSinPlaneacionUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "Ha ocurrido un error en el sistema"
            respuesta.contenido = []

        return respuesta

    @staticmethod
    def obtenerPedidosConPlaneacionUseCase(planeacion_id) -> list[Pedido]:
        respuesta: RespuestaOperacion = RespuestaOperacion()
        try:
            respuesta.contenido: Pedido = PedidoRepository.obtenerPedidosConPlaneacionDeBD(planeacion_id=planeacion_id)
        except Pedido.DoesNotExist as error:
            print("ERROR:obtenerPedidosConPlaneacionUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "No hay registros"
            respuesta.contenido = []
        except Exception as error:
            print("ERROR:obtenerPedidosConPlaneacionUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "Ha ocurrido un error en el sistema"
            respuesta.contenido = []

        return respuesta
    
    @staticmethod
    def actualizarPlaneacionDePedidoUseCase(id, planeacion_id):
        
        respuesta: RespuestaOperacion = RespuestaOperacion()

        try:
            PedidoRepository.actualizarPlaneacionDePedidoEnBD(id=id, planeacion_id=planeacion_id)
            respuesta.mensaje = "Pedido actualizado exitosamente"
        except Exception as error:
            print("ERROR:actualizarPlaneacionDePedidoUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "Operación fallida"
            
        return respuesta