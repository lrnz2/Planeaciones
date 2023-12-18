from planeacion.data.database.entities.PlaneacionEntity import Planeacion

class PlaneacionDao():

    @staticmethod
    def obtenerPlaneaciones():
        return Planeacion.objects.all()

    @staticmethod
    def obtenerPlaneacionPorClave(clave):
        return Planeacion.objects.get(clave=clave)

    @staticmethod
    def crearPlaneacion( clave: str, status:str):
        Planeacion( clave = clave, status=status ).save()
    
    @staticmethod
    def actualizarPlaneacion(id: str, status:str):
        Planeacion.objects.filter(id = id).update(status=status)

    @staticmethod
    def eliminarPlaneacion(id: str):
        Planeacion.objects.get(id = id).delete()
    