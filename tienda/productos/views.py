from django.shortcuts import render

# Create your views here.

from.models import Cliente
from.models import producto

def listar_clientes(request):
    cliente = Cliente.objects.all()
    return render(request, 'listar_clientes.html',{'clientes': clientes})
                  
def listar_productos(request):
    producto = Producto.objects.all()
    return render(request, 'listar_producto.html',{'producto':producto})                 

