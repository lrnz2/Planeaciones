from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse, HttpResponseRedirect

from planeacion.domain.model.RespuestaOperacion import RespuestaOperacion
from planeacion.core.utils.Reverse import Reverse as custom_reverse
from dataclasses import asdict

from planeacion.domain.ClienteUseCases import ClienteUseCases
from planeacion.domain.ProductoUseCases import ProductoUseCases
from planeacion.domain.PedidoUseCases import PedidoUseCases
from planeacion.domain.PlaneacionUseCases import PlaneacionUseCases

require_http_methods(["GET"])
def home(request):
    return render(request, "planeacion/index.html")

require_http_methods(["GET"])
def clientes(request):
    mensaje = request.GET.get('mensaje')
    error = request.GET.get('error') == 'True'

    respuesta:RespuestaOperacion = ClienteUseCases.obtenerClientesUseCase()

    context = {
        "clientes" : respuesta.contenido,
        "mensaje": mensaje,
        "error": error
    }
    return render(request, "planeacion/clientes.html", context)

require_http_methods(["POST"])
def crearCliente(request):
    nombre = request.POST['nombre']
    apellidos = request.POST['apellidos']

    respuesta = ClienteUseCases.crearClienteUseCase(nombre=nombre, apellidos = apellidos)
    url_encoded = custom_reverse.reverse('clientes', dict = asdict(respuesta))

    return HttpResponseRedirect(url_encoded)

require_http_methods(["POST"])
def eliminarCliente(request):
    id = request.POST['id']

    respuesta = ClienteUseCases.eliminarClienteUseCase(id=id)
    url_encoded = custom_reverse.reverse('clientes', dict = asdict(respuesta))

    return HttpResponseRedirect(url_encoded)

require_http_methods(["POST"])

def actualizarCliente(request):
    id = request.POST['id']
    nombre = request.POST['nombre']
    apellidos = request.POST['apellidos']

    respuesta = ClienteUseCases.actualizarClienteUseCase(id=id, nuevoNombre = nombre, nuevoApellidos = apellidos)
    url_encoded = custom_reverse.reverse('clientes', dict = asdict(respuesta))

    return HttpResponseRedirect(url_encoded)


require_http_methods(["GET"])
def productos(request):
    mensaje = request.GET.get('mensaje')
    error = request.GET.get('error') == 'True'

    respuesta:RespuestaOperacion = ProductoUseCases.obtenerProductosUseCase()

    context = {
        "productos" : respuesta.contenido,
        "mensaje": mensaje,
        "error": error
    }
    return render(request, "planeacion/productos.html", context)

require_http_methods(["POST"])
def crearProducto(request):
    sku = request.POST['sku']
    pasillo = request.POST['pasillo']
    precio = request.POST['precio']

    respuesta = ProductoUseCases.crearProductoUseCase(sku=sku, pasillo=pasillo, precio=precio)
    url_encoded = custom_reverse.reverse('productos', dict = asdict(respuesta))

    return HttpResponseRedirect(url_encoded)

require_http_methods(["POST"])
def eliminarProducto(request):
    sku = request.POST['sku']

    respuesta = ProductoUseCases.eliminarProductoUseCase(sku = sku)
    url_encoded = custom_reverse.reverse('productos', dict = asdict(respuesta))

    return HttpResponseRedirect(url_encoded)

require_http_methods(["POST"])

def actualizarProducto(request):
    sku = request.POST['sku']
    pasillo = request.POST['pasillo']
    precio = request.POST['precio']

    respuesta = ProductoUseCases.actualizarProductoUseCase(sku=sku, pasillo=pasillo, precio=precio)
    url_encoded = custom_reverse.reverse('productos', dict = asdict(respuesta))

    return HttpResponseRedirect(url_encoded)

""" PEDIDOS ------------------------ """

require_http_methods(["GET"])
def pedidos(request):
    mensaje = request.GET.get('mensaje')
    error = request.GET.get('error') == 'True'

    respuesta:RespuestaOperacion = PedidoUseCases.obtenerPedidosUseCase()
    productos = ProductoUseCases.obtenerProductosUseCase().contenido
    clientes = ClienteUseCases.obtenerClientesUseCase().contenido

    context = {
        "pedidos" : respuesta.contenido,
        "mensaje": mensaje,
        "error": error,
        "clientes": clientes,
        "productos": productos,
    }
    return render(request, "planeacion/pedidos.html", context)

require_http_methods(["POST"])
def crearPedido(request):
    cliente_id = request.POST['cliente-id']
    producto_sku = request.POST['producto-sku']
    cantidad = request.POST['cantidad']
    ubicacion = request.POST['ubicacion']
    zona = request.POST['zona']
    _type = request.POST['type']

    respuesta = PedidoUseCases.crearPedidoUseCase(cliente_id = cliente_id, producto_sku=producto_sku, cantidad=cantidad,
            ubicacion=ubicacion, zona=zona, _type=_type)
    url_encoded = custom_reverse.reverse('pedidos', dict = asdict(respuesta))

    return HttpResponseRedirect(url_encoded)

require_http_methods(["POST"])
def eliminarPedido(request):
    id = request.POST['id']

    respuesta = PedidoUseCases.eliminarPedidoUseCase(id = id)
    url_encoded = custom_reverse.reverse('pedidos', dict = asdict(respuesta))

    return HttpResponseRedirect(url_encoded)

require_http_methods(["POST"])
def actualizarPedido(request):
    id = request.POST['id']
    cliente_id = request.POST['cliente-id']
    producto_sku = request.POST['producto-sku']
    cantidad = request.POST['cantidad']
    ubicacion = request.POST['ubicacion']
    zona = request.POST['zona']
    _type = request.POST['type']

    respuesta = PedidoUseCases.actualizarPedidoUseCase(id = id, cliente_id = cliente_id, producto_sku=producto_sku, cantidad=cantidad,
            ubicacion=ubicacion, zona=zona, _type=_type)
    url_encoded = custom_reverse.reverse('pedidos', dict = asdict(respuesta))

    return HttpResponseRedirect(url_encoded)


""" PLANEACIONES ------------------------ """

require_http_methods(["GET"])
def planeaciones(request):
    mensaje = request.GET.get('mensaje')
    error = request.GET.get('error') == 'True'

    respuesta:RespuestaOperacion = PlaneacionUseCases.obtenerPlaneacionesUseCase()
    productos = ProductoUseCases.obtenerProductosUseCase().contenido
    clientes = ClienteUseCases.obtenerClientesUseCase().contenido
    pedidos:RespuestaOperacion = PedidoUseCases.obtenerPedidosUseCase()

    pedidosSinPlaneacion = []
    for p in pedidos.contenido:
        if(p.planeacion == None):
            pedidosSinPlaneacion.append(p)

    context = {
        "planeaciones" : respuesta.contenido,
        "pedidos": pedidos,
        "pedidos_sin_planeacion": pedidosSinPlaneacion,
        "mensaje": mensaje,
        "error": error,
    }

    return render(request, "planeacion/index.html", context)

require_http_methods(["POST"])
def crearPlaneacion(request):
    clave = request.POST['clave']
    status = request.POST['status']
    pedidos = request.POST.getlist('pedidos') # pedidos a enlazar con planeacion

    respuesta = PlaneacionUseCases.crearPlaneacionUseCase(clave=clave, status=status)
    planeacion_creada:Planeacion = PlaneacionUseCases.obtenerPlaneacionPorClaveUseCase(clave).contenido

    for pedido_id in pedidos:
        res = PedidoUseCases.actualizarPlaneacionDePedidoUseCase(id=pedido_id, planeacion_id= planeacion_creada.id)
        print("RELACIONADO: | PEDIDO ID", pedido_id, "| PLANEACION", res)
    
    url_encoded = custom_reverse.reverse('planeaciones', dict = asdict(respuesta))
    return HttpResponseRedirect(url_encoded)

require_http_methods(["POST"])
def actualizarPlaneacion(request):
    id = request.POST['id']
    status = request.POST['status']

    respuesta = PlaneacionUseCases.actualizarPlaneacionUseCase(id=id, status=status)
    url_encoded = custom_reverse.reverse('planeaciones', dict = asdict(respuesta))

    return HttpResponseRedirect(url_encoded)

require_http_methods(["POST"])
def eliminarPlaneacion(request):
    id = request.POST['id']

    respuesta = PlaneacionUseCases.eliminarPlaneacionUseCase(id)
    url_encoded = custom_reverse.reverse('planeaciones', dict = asdict(respuesta))

    return HttpResponseRedirect(url_encoded)


class Resumen:
    sku=""
    cantidad=0
    precio=0.00
    pasillo=0
    tipo=""
    subtotal=0.00

    def __init__(self, sku, cantidad, precio, pasillo, tipo, subtotal):
        self.sku = sku
        self.cantidad = cantidad
        self.precio = precio
        self.pasillo = pasillo
        self.tipo = tipo
        self.subtotal = subtotal

class Cliente:
    nombre = ""
    resumenes:list[Resumen] = []
    total= 0.00
    def __init__(self, nombre, total=0.00, resumenes=[]):
        self.nombre = nombre
        self.total = total
        self.resumenes=resumenes
    def addResumen(self, resumen):
        self.resumenes.append(resumen)
    def sumaTotal(self, cantidad):
        self.total += cantidad


    
require_http_methods(["GET"])
def detallePlaneacion(request, planeacion_clave):
    planeacion:Planeacion = PlaneacionUseCases.obtenerPlaneacionPorClaveUseCase(planeacion_clave).contenido
    pedidos = PedidoUseCases.obtenerPedidosConPlaneacionUseCase(planeacion.id).contenido


    clientesTemp = []
    clientes:list[Cliente]  = []
    for pedido in pedidos:
        nombre_cliente = pedido.cliente.nombre
        sku = pedido.producto.sku
        cantidad = pedido.cantidad
        precio = pedido.producto.precio
        subtotal = cantidad * precio
        pasillo = pedido.producto.pasillo
        tipo = pedido.type
        if( nombre_cliente not in clientesTemp):
            clientes.append(Cliente(nombre= nombre_cliente, total=0.00, resumenes = []))
            clientesTemp.append(nombre_cliente)
            for c in clientes:
                if (c.nombre == nombre_cliente):
                    c.addResumen(Resumen(sku, cantidad, precio, pasillo, tipo, subtotal))
        else:
            for c in clientes:
                if (c.nombre == nombre_cliente):
                    c.addResumen(Resumen(sku, cantidad, precio, pasillo, tipo, subtotal))
    
    
    for cliente in clientes:
        for resumen in cliente.resumenes:
            cliente.sumaTotal(float(resumen.subtotal))

    total_general =0.00
    for cliente in clientes:
        total_general += cliente.total

    context = {
        "planeacion" : planeacion,
        "resumen_clientes": clientes,
        "total_general": total_general
    }

    return render(request, "planeacion/planeacion-detalle.html", context)

