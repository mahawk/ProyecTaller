from django.urls import path
from apps.Producto.views import index, especial, viewProductos, agregarProducto, editarProducto, eliminarProducto

app_name = "Producto"

urlpatterns = [
	path('', index),
	path('index', index),
	path('especial', viewProductos.as_view(), name = 'listaProductos'),
	path('agregarProducto', agregarProducto, name="agregarProducto"),
	path('editarProducto/<idProducto>', editarProducto, name="editarProducto"),
	path('eliminarProducto/<idProducto>', eliminarProducto, name="eliminarProducto"),

]
