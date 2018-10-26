from django.shortcuts import render, redirect
from apps.Producto.models import Producto
from django.views.generic import ListView
from apps.Producto.forms import ProductoForm

# Create your views here.
def index(request):
	contexto = { 
		'Producto': Producto.objects.all()
	}
	return render(request, 'producto/index.html', contexto)

def especial(request):
	return render(request, 'producto/plantillaProducto.html')

def agregarProducto(request):
	if request.method == 'POST':
		form = ProductoForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('Producto:listaProductos')
	else:
		form = ProductoForm()
	return render(request, 'producto/productoFormulario.html', {'form':form})

def editarProducto(request, idProducto):
	producto = Producto.objects.get(id=idProducto)
	if (request.method == 'GET'):
		form = ProductoForm(instance=producto)
	else:
		form = ProductoForm(request.POST, instance=producto)
		if form.is_valid():
			form.save()
		return redirect('producto:listaProductos')
	return render(request, 'producto/productoFormulario.html', {'form':form})

def eliminarProducto(request, idProducto):
	producto = Producto.objects.get(id=idProducto)
	if (request.method == 'GET'):
		instance=producto
		instance.delete()
	return redirect('Producto:listaProductos')


class viewProductos(ListView):
	model = Producto
	queryset = Producto.objects.all()
	template_name = 'producto/plantillaProducto.html'
