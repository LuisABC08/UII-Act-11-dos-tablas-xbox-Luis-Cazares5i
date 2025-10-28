from django.db import models

class Proveedor(models.Model):
    # ID_Proveedor se crea automáticamente por Django
    nombre_proveedor = models.CharField(max_length=100)
    contacto_nombre = models.CharField(max_length=100, blank=True, null=True)
    contacto_telefono = models.CharField(max_length=20, blank=True, null=True)
    contacto_email = models.EmailField(blank=True, null=True)
    direccion_proveedor = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nombre_proveedor

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"

class Videojuego(models.Model):
    # ID_Videojuego se crea automáticamente por Django
    titulo = models.CharField(max_length=100, help_text="Título del videojuego")
    desarrollador = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    plataforma = models.CharField(max_length=50)
    fecha_lanzamiento = models.DateField(blank=True, null=True)
    foto = models.ImageField(upload_to='portadas_videojuegos/', blank=True, null=True) # Carpeta donde se guardan las fotos
    proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, related_name='videojuegos', blank=True, null=True) # Si el proveedor se borra, el campo se pone a NULL

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Videojuego"
        verbose_name_plural = "Videojuegos"