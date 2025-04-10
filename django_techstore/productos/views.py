from django.shortcuts import render
from .models import Producto, Categoria

from .models import Carrito

from django.shortcuts import get_object_or_404, redirect
from .models import Carrito, Producto

def index(request):
    categorias = Categoria.objects.all()
    productos_oferta = Producto.objects.filter(en_oferta=True)
    productos = Producto.objects.all()
    return render(request, 'productos/index.html', {
        'categorias': categorias,
        'productos_oferta': productos_oferta,
        'productos': productos
    })

def detalle_producto(request, id_producto):
    producto = Producto.objects.get(id=id_producto)
    return render(request, 'productos/detalle.html', {'producto': producto})

def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'productos/lista_categorias.html', {'categorias': categorias})

def ofertas(request):
    productos_oferta = Producto.objects.filter(en_oferta=True)
    return render(request, 'productos/ofertas.html', {'productos_oferta': productos_oferta})

def all_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/allproductos.html', {'productos': productos})

def categoria(request, id_categoria):
    categoria = Categoria.objects.get(id=id_categoria)
    productos = Producto.objects.filter(categoria=categoria)
    return render(request, 'productos/categoria.html', {'categoria': categoria, 'productos': productos})

def productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/allproductos.html', {'productos': productos})


def buscar_productos(request):
    query = request.GET.get('search-input', '')
    productos = Producto.objects.filter(nombre__icontains=query)
    return render(request, 'productos/buscar.html', {'productos': productos, 'query': query})


def ver_carrito(request):
    carrito_items = Carrito.objects.all()
    total = sum(item.subtotal for item in carrito_items)

    return render(request, 'productos/carrito.html', {
        'carrito_items': carrito_items,
        'total': total
    })

def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    # Verifica si ya está en el carrito
    item, creado = Carrito.objects.get_or_create(producto=producto)
    if not creado:
        item.cantidad += 1
        item.save()
    return redirect(request.META.get('HTTP_REFERER', 'index'))

def eliminar_del_carrito(request, producto_id):
    item = Carrito.objects.filter(producto_id=producto_id).first()
    if item:
        item.delete()
    return redirect('ver_carrito')

def vaciar_carrito(request):
    Carrito.objects.all().delete()
    return redirect('ver_carrito')

def aumentar_cantidad(request, producto_id):
    item = Carrito.objects.filter(producto_id=producto_id).first()
    if item:
        item.cantidad += 1
        item.save()
    return redirect('ver_carrito')

def disminuir_cantidad(request, producto_id):
    item = Carrito.objects.filter(producto_id=producto_id).first()
    if item:
        if item.cantidad > 1:
            item.cantidad -= 1
            item.save()
        else:
            item.delete()
    return redirect('ver_carrito')
