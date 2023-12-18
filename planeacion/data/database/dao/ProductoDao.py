from planeacion.data.database.entities.ProductoEntity import Producto

class ProductoDao():

    @staticmethod
    def obtenerProductos():
        return Producto.objects.all()
    
    @staticmethod
    def crearProducto( sku:int, pasillo: str, precio:float):
        Producto( sku=sku, pasillo=pasillo, precio=precio).save()
    
    @staticmethod
    def actualizarProducto(sku:int, pasillo: str, precio:float):
        Producto.objects.filter(sku = sku).update(pasillo=pasillo, precio=precio)

    @staticmethod
    def eliminarProducto(sku:int):
        Producto.objects.get(sku = sku).delete()
    