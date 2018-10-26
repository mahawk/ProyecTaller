from django import forms
from apps.Producto.models import Producto

class ProductoForm(forms.ModelForm):
	class Meta:
		model = Producto
		fields= [
		'nombreProducto',
		'descripcion',
		'costo',
		'disponible',
		'numExistencias',
		]

		labels = {
		'nombre':'Nombre del producto',
		'descripcion': 'Descripcion',
		'costo': 'Costo',
		'disponible':'Disponible',
		'numExistencias':'Número de existencias',
		}

		widgets = {
		'nombre':forms.TextInput(attrs={'class' : 'form-control'}),
		'descripcion':forms.TextInput(attrs={'class' : 'form-control'}),
		'costo':forms.TextInput(attrs={'class' : 'form-control'}),
		'disponible':forms.TextInput(attrs={'class' : 'form-control'}),
		'numExistencias':forms.TextInput(attrs={'class' : 'form-control'}),
		}
