from django.shortcuts import render, get_object_or_404, redirect
from .models import Proveedor, Videojuego
from .forms import ProveedorForm, VideojuegoForm

# Vistas para Videojuegos
def listar_videojuegos(request):
    videojuegos = Videojuego.objects.all()
    return render(request, 'listar_videojuegos.html', {'videojuegos': videojuegos})

def detalle_videojuego(request, videojuego_id):
    videojuego = get_object_or_404(Videojuego, id=videojuego_id)
    return render(request, 'detalle_videojuego.html', {'videojuego': videojuego})

def crear_videojuego(request):
    if request.method == 'POST':
        form = VideojuegoForm(request.POST, request.FILES) # request.FILES es crucial para las imágenes
        if form.is_valid():
            form.save()
            return redirect('app_videojuegos_proveedores:listar_videojuegos')
    else:
        form = VideojuegoForm()
    return render(request, 'formulario_videojuego.html', {'form': form, 'titulo': 'Crear Videojuego'})

def editar_videojuego(request, videojuego_id):
    videojuego = get_object_or_404(Videojuego, id=videojuego_id)
    if request.method == 'POST':
        form = VideojuegoForm(request.POST, request.FILES, instance=videojuego) # request.FILES también aquí
        if form.is_valid():
            form.save()
            return redirect('app_videojuegos_proveedores:detalle_videojuego', videojuego_id=videojuego.id)
    else:
        form = VideojuegoForm(instance=videojuego)
    return render(request, 'formulario_videojuego.html', {'form': form, 'titulo': 'Editar Videojuego'})

def borrar_videojuego(request, videojuego_id):
    videojuego = get_object_or_404(Videojuego, id=videojuego_id)
    if request.method == 'POST':
        videojuego.delete()
        return redirect('app_videojuegos_proveedores:listar_videojuegos')
    return render(request, 'confirmar_borrar_videojuego.html', {'videojuego': videojuego})

# Vistas para Proveedores
def listar_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'listar_proveedores.html', {'proveedores': proveedores})

def detalle_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    return render(request, 'detalle_proveedor.html', {'proveedor': proveedor})

def crear_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_videojuegos_proveedores:listar_proveedores')
    else:
        form = ProveedorForm()
    return render(request, 'formulario_proveedor.html', {'form': form, 'titulo': 'Crear Proveedor'})

def editar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('app_videojuegos_proveedores:detalle_proveedor', proveedor_id=proveedor.id)
    else:
        form = ProveedorForm(instance=proveedor)
    return render(request, 'formulario_proveedor.html', {'form': form, 'titulo': 'Editar Proveedor'})

def borrar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('app_videojuegos_proveedores:listar_proveedores')
    return render(request, 'confirmar_borrar_proveedor.html', {'proveedor': proveedor})