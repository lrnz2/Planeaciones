"""
URL configuration for prueba_tecnica project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from planeacion.ui import views

urlpatterns = [
    path("", views.home, name="home"),
    path("clientes", views.clientes, name="clientes"),
    path("clientes/crear", views.crearCliente, name="crear-cliente"),
    path("clientes/eliminar", views.eliminarCliente, name="eliminar-cliente"),
    path("clientes/actualizar", views.actualizarCliente, name="actualizar-cliente"),

    path("productos", views.productos, name="productos"),
    path("productos/crear", views.crearProducto, name="crear-producto"),
    path("productos/eliminar", views.eliminarProducto, name="eliminar-producto"),
    path("productos/actualizar", views.actualizarProducto, name="actualizar-producto"),

    path("pedidos", views.pedidos, name="pedidos"),
    path("pedidos/crear", views.crearPedido, name="crear-pedido"),
    path("pedidos/eliminar", views.eliminarPedido, name="eliminar-pedido"),
    path("pedidos/actualizar", views.actualizarPedido, name="actualizar-pedido"),

    path("planeaciones", views.planeaciones, name="planeaciones"),
    path("planeaciones/crear", views.crearPlaneacion, name="crear-planeacion"),
    path("planeaciones/actualizar", views.actualizarPlaneacion, name="actualizar-planeacion"),
    path("planeaciones/eliminar", views.eliminarPlaneacion, name="eliminar-planeacion"),
    path("planeacion/<str:planeacion_clave>/", views.detallePlaneacion, name="detalle-planeacion"),
]
