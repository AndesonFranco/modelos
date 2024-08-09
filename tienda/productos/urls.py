from django.urls import path
from.views import listar_clientes, listar_producto

urlpatterns = [
    path('clientes/', listar_clientes, name='listar_cliente'),
    path('productos/', listar_productos, name='listar_productos'),
]
