
from planeacion.data.database.entities.PlaneacionEntity import Planeacion
from planeacion.data.repository.PlaneacionRepository import PlaneacionRepository

from planeacion.domain.model.RespuestaOperacion import RespuestaOperacion

class PlaneacionUseCases():
    
    @staticmethod
    def obtenerPlaneacionesUseCase() -> list[Planeacion]:
        respuesta: RespuestaOperacion = RespuestaOperacion()
        try:
            respuesta.contenido: list[Planeacion] = PlaneacionRepository.obtenerPlaneacionesDeBD()
        except Planeacion.DoesNotExist as error:
            print("ERROR:obtenerPlaneacionesUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "No hay registros"
            respuesta.contenido = []
        except Exception as error:
            print("ERROR:obtenerPlaneacionesUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "Ha ocurrido un error en el sistema"
            respuesta.contenido = []

        return respuesta

        
    
    @staticmethod
    def obtenerPlaneacionPorClaveUseCase(clave) -> Planeacion:
        respuesta: RespuestaOperacion = RespuestaOperacion()
        try:
            respuesta.contenido: list[Planeacion] = PlaneacionRepository.obtenerPlaneacionPorClaveDeBD(clave)
        except Planeacion.DoesNotExist as error:
            print("ERROR:obtenerPlaneacionPorClaveUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "No hay registros"
            respuesta.contenido = []
        except Exception as error:
            print("ERROR:obtenerPlaneacionPorClaveUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "Ha ocurrido un error en el sistema"
            respuesta.contenido = []
        return respuesta

    @staticmethod
    def crearPlaneacionUseCase(clave:str, status:str):
        respuesta: RespuestaOperacion = RespuestaOperacion()
        try:
            PlaneacionRepository.crearPlaneacionEnBD(clave = clave, status=status)
            respuesta.mensaje = "Planeacion creado exitosamente"
        except Exception as error:
            print("ERROR:crearPlaneacionUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "Operación fallida"

        return respuesta
    
    @staticmethod
    def actualizarPlaneacionUseCase(id: str, status:str):
        
        respuesta: RespuestaOperacion = RespuestaOperacion()

        try:
            PlaneacionRepository.actualizarPlaneacionEnBD(id = id, status = status)
            respuesta.mensaje = "Planeacion actualizado exitosamente"
        except Exception as error:
            print("ERROR:actualizarPlaneacionUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "Operación fallida"
            
        return respuesta
    
    @staticmethod
    def eliminarPlaneacionUseCase(id: str):
        respuesta: RespuestaOperacion = RespuestaOperacion()
        try:
            PlaneacionRepository.eliminarPlaneacionEnBD(id)
            respuesta.mensaje = "Planeacion eliminado exitosamente"
        except Exception as error:
            print("ERROR:eliminarPlaneacionUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "Operación fallida"

        return respuesta

        