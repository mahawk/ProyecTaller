from django.shortcuts import render
from apps.Categoria.models import Categoria

def index(request):
	contexto = {
		'Categoria': Categoria.objects.all()
	}
	return render(request, 'categoria/index.html', contexto)