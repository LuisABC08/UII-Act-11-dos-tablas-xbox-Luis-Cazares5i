from django.urls import path
from . import views

app_name = 'app_videojuegos_proveedores'

urlpatterns = [
    # URLs para Videojuegos
    path('', views.listar_videojuegos, name='listar_videojuegos'), # Página de inicio
    path('videojuego/<int:videojuego_id>/', views.detalle_videojuego, name='detalle_videojuego'),
    path('videojuego/crear/', views.crear_videojuego, name='crear_videojuego'),
    path('videojuego/editar/<int:videojuego_id>/', views.editar_videojuego, name='editar_videojuego'),
    path('videojuego/borrar/<int:videojuego_id>/', views.borrar_videojuego, name='borrar_videojuego'),

    # URLs para Proveedores
    path('proveedores/', views.listar_proveedores, name='listar_proveedores'),
    path('proveedor/<int:proveedor_id>/', views.detalle_proveedor, name='detalle_proveedor'),
    path('proveedor/crear/', views.crear_proveedor, name='crear_proveedor'),
    path('proveedor/editar/<int:proveedor_id>/', views.editar_proveedor, name='editar_proveedor'),
    path('proveedor/borrar/<int:proveedor_id>/', views.borrar_proveedor, name='borrar_proveedor'),
]