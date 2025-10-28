from django import forms
from .models import Proveedor, Videojuego

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre_proveedor', 'contacto_nombre', 'contacto_telefono', 'contacto_email', 'direccion_proveedor']

class VideojuegoForm(forms.ModelForm):
    # Asegúrate de que los campos del modelo estén listados aquí
    class Meta:
        model = Videojuego
        fields = ['titulo', 'desarrollador', 'genero', 'plataforma', 'fecha_lanzamiento', 'foto', 'proveedor']
        widgets = {
            'fecha_lanzamiento': forms.DateInput(attrs={'type': 'date'}), # Esto ayuda a mostrar un selector de fecha en el navegador
        }