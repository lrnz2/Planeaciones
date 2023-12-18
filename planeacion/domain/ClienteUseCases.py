
from planeacion.data.database.entities.ClienteEntity import Cliente
from planeacion.data.repository.ClienteRepository import ClienteRepository

from planeacion.domain.model.RespuestaOperacion import RespuestaOperacion

class ClienteUseCases():
    
    @staticmethod
    def obtenerClientesUseCase() -> list[Cliente]:
        respuesta: RespuestaOperacion = RespuestaOperacion()
        try:
            respuesta.contenido: list[Cliente] = ClienteRepository.obtenerClientesDeBD()
        except Cliente.DoesNotExist as error:
            print("ERROR:obtenerClientesUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "No hay registros"
            respuesta.contenido = []
        except Exception as error:
            print("ERROR:obtenerClientesUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "Ha ocurrido un error en el sistema"
            respuesta.contenido = []

        return respuesta
    
    @staticmethod
    def obtenerClienteUseCase(id:str) -> Cliente:
        respuesta: RespuestaOperacion = RespuestaOperacion()
        try:
            respuesta.contenido: Cliente = ClienteRepository.obtenerClienteDeBD(id=id)
        except Cliente.DoesNotExist as error:
            print("ERROR:obtenerClientesUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "No hay registros"
            respuesta.contenido = []
        except Exception as error:
            print("ERROR:obtenerClientesUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "Ha ocurrido un error en el sistema"
            respuesta.contenido = []

        return respuesta
    
    @staticmethod
    def crearClienteUseCase(nombre: str, apellidos:str):
        
        respuesta: RespuestaOperacion = RespuestaOperacion()

        try:
            ClienteRepository.crearClienteEnBD(nombre = nombre, apellidos = apellidos)
            respuesta.mensaje = "Cliente creado exitosamente"
        except Exception as error:
            print("ERROR:crearClienteUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "Operación fallida"

        return respuesta
    
    @staticmethod
    def actualizarClienteUseCase(id: str, nuevoNombre: str, nuevoApellidos: str):
        
        respuesta: RespuestaOperacion = RespuestaOperacion()

        try:
            ClienteRepository.actualizarClienteEnBD(id = id, nuevoNombre=nuevoNombre, nuevoApellidos=nuevoApellidos)
            respuesta.mensaje = "Cliente actualizado exitosamente"
        except Exception as error:
            print("ERROR:actualizarClienteUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "Operación fallida"
            
        return respuesta
    
    @staticmethod
    def eliminarClienteUseCase(id: str):
        respuesta: RespuestaOperacion = RespuestaOperacion()
        try:
            ClienteRepository.eliminarClienteEnBD(id)
            respuesta.mensaje = "Cliente eliminado exitosamente"
        except Exception as error:
            print("ERROR:eliminarClienteUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "Operación fallida"

        return respuesta

        