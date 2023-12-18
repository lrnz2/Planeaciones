from planeacion.data.database.dao.ProductoDao import ProductoDao
from planeacion.data.database.entities.ProductoEntity import Producto

class ProductoRepository():
    
    @staticmethod
    def obtenerProductosDeBD():
        response:list[Producto] = ProductoDao.obtenerProductos()
        return response
    
    @staticmethod
    def crearProductoEnBD( sku:int, pasillo: str, precio:float):
        ProductoDao.crearProducto( sku=sku, pasillo=pasillo, precio=precio)
    
    @staticmethod
    def actualizarProductoEnBD(sku:int, pasillo: str, precio:float):
        ProductoDao.actualizarProducto(sku=sku, pasillo=pasillo, precio=precio)
    
    @staticmethod
    def eliminarProductoEnBD(sku:int):
        ProductoDao.eliminarProducto(sku=sku)