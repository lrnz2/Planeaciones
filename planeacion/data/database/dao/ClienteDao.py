from planeacion.data.database.entities.ClienteEntity import Cliente

class ClienteDao():

    @staticmethod
    def obtenerClientes():
        return Cliente.objects.all()
    
    @staticmethod
    def obtenerCliente(id): # no usado
        return Cliente.objects.get(id = id)
    
    @staticmethod
    def crearCliente( nombre: str, apellidos:str):
        Cliente( nombre = nombre).save()
    
    @staticmethod
    def actualizarCliente(id: str, nuevoNombre: str, nuevoApellidos: str):
        Cliente.objects.filter(id = id).update(nombre =nuevoNombre)

    @staticmethod
    def eliminarCliente(id: str):
        Cliente.objects.get(id = id).delete()
    