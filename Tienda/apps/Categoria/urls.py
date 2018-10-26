from django.urls import path
from apps.Categoria.views import index

urlpatterns = [
	path('',index),
	path('index',index),
]