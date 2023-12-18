from planeacion.data.database.dao.ClienteDao import ClienteDao
from planeacion.data.database.entities.ClienteEntity import Cliente

class ClienteRepository():
    
    @staticmethod
    def obtenerClientesDeBD():
        response:list[Cliente] = ClienteDao.obtenerClientes()
        return response
    
    @staticmethod
    def obtenerClienteDeBD(id:str):
        response:Cliente = ClienteDao.obtenerCliente(id=id)
        return response
    
    @staticmethod
    def crearClienteEnBD( nombre: str, apellidos:str):
        ClienteDao.crearCliente( nombre = nombre, apellidos = apellidos)
    
    @staticmethod
    def actualizarClienteEnBD(id: str, nuevoNombre: str, nuevoApellidos: str):
        ClienteDao.actualizarCliente(id = id, nuevoNombre=nuevoNombre, nuevoApellidos=nuevoApellidos)
    
    @staticmethod
    def eliminarClienteEnBD(id: str):
        ClienteDao.eliminarCliente(id)