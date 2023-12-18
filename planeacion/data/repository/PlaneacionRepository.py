from planeacion.data.database.dao.PlaneacionDao import PlaneacionDao
from planeacion.data.database.entities.PlaneacionEntity import Planeacion

class PlaneacionRepository():
    
    @staticmethod
    def obtenerPlaneacionesDeBD():
        response:list[Planeacion] = PlaneacionDao.obtenerPlaneaciones()
        return response
    
    @staticmethod
    def obtenerPlaneacionPorClaveDeBD(clave):
        response:list[Planeacion] = PlaneacionDao.obtenerPlaneacionPorClave(clave)
        return response
    
    @staticmethod
    def obtenerPlaneacionDeBD(id:str):
        response:Planeacion = PlaneacionDao.obtenerPlaneacion(id=id)
        return response
    
    @staticmethod
    def crearPlaneacionEnBD( clave:str, status:str):
        PlaneacionDao.crearPlaneacion( clave=clave, status = status)
    
    @staticmethod
    def actualizarPlaneacionEnBD(id: str, status:str):
        PlaneacionDao.actualizarPlaneacion(id = id,  status=status)
    
    @staticmethod
    def eliminarPlaneacionEnBD(id: str):
        PlaneacionDao.eliminarPlaneacion(id)