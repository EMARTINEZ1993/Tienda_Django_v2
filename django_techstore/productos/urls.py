from django.urls import path
from .views import index, detalle_producto,  lista_categorias, ofertas, productos, categoria, all_productos,buscar_productos, ver_carrito, agregar_al_carrito
from .views import eliminar_del_carrito, vaciar_carrito,    aumentar_cantidad, disminuir_cantidad
urlpatterns = [
    path('', index, name='index'),
    path('detalle/<int:id_producto>', detalle_producto, name='detalle_producto'),
    path('categorias/', lista_categorias, name='lista_categorias'),
    path('ofertas/', ofertas, name='ofertas'),
    path('productos/', productos, name='productos'),
    path('categoria/<int:id_categoria>', categoria, name='categoria'),
    path('all_productos/', all_productos, name='all_productos'),
    path('buscar/', buscar_productos, name='buscar_productos'),
    path('carrito/', ver_carrito, name='ver_carrito'),
    path('carrito/agregar/<int:producto_id>/', agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/eliminar/<int:producto_id>/', eliminar_del_carrito, name='eliminar_del_carrito'),
    path('carrito/vaciar/', vaciar_carrito, name='vaciar_carrito'),
    path('carrito/aumentar/<int:producto_id>/', aumentar_cantidad, name='aumentar_cantidad'),
    path('carrito/disminuir/<int:producto_id>/', disminuir_cantidad, name='disminuir_cantidad'),


]    