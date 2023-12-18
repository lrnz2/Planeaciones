
from planeacion.data.database.entities.ProductoEntity import Producto
from planeacion.data.repository.ProductoRepository import ProductoRepository

from planeacion.domain.model.RespuestaOperacion import RespuestaOperacion

class ProductoUseCases():
    
    @staticmethod
    def obtenerProductosUseCase() -> list[Producto]:
        respuesta: RespuestaOperacion = RespuestaOperacion()
        try:
            respuesta.contenido: list[Producto] = ProductoRepository.obtenerProductosDeBD()
        except Producto.DoesNotExist as error:
            print("ERROR:obtenerProductosUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "No hay registros"
            respuesta.contenido = []
        except Exception as error:
            print("ERROR:obtenerProductosUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "Ha ocurrido un error en el sistema"
            respuesta.contenido = []

        return respuesta
    
    @staticmethod
    def crearProductoUseCase(sku:int, pasillo: str, precio:float):
        
        respuesta: RespuestaOperacion = RespuestaOperacion()

        try:
            ProductoRepository.crearProductoEnBD(sku=sku, pasillo=pasillo, precio=precio)
            respuesta.mensaje = "Producto creado exitosamente"
        except Exception as error:
            print("ERROR:crearProductoUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "Operación fallida"

        return respuesta
    
    @staticmethod
    def actualizarProductoUseCase(sku:int, pasillo: str, precio:float):
        
        respuesta: RespuestaOperacion = RespuestaOperacion()

        try:
            ProductoRepository.actualizarProductoEnBD(sku=sku, pasillo=pasillo, precio=precio)
            respuesta.mensaje = "Producto actualizado exitosamente"
        except Exception as error:
            print("ERROR:actualizarProductoUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "Operación fallida"
            
        return respuesta
    
    @staticmethod
    def eliminarProductoUseCase(sku: int):
        respuesta: RespuestaOperacion = RespuestaOperacion()
        try:
            ProductoRepository.eliminarProductoEnBD(sku=sku)
            respuesta.mensaje = "Producto eliminado exitosamente"
        except Exception as error:
            print("ERROR:eliminarProductoUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "Operación fallida"

        return respuesta

        