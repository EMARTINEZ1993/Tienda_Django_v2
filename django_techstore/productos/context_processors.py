# productos/context_processors.py

from .models import Carrito

def total_productos_en_carrito(request):
    carrito_items = Carrito.objects.all()
    total_items = sum(item.cantidad for item in carrito_items)

    return {
        'total_productos_en_carrito': total_items,
        'vista_previa_carrito': carrito_items
    }
