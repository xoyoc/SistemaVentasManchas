from django.db import models
from django.core.validators import MinValueValidator

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    icono = models.CharField(max_length=10, help_text="Emoji o icono")
    orden = models.IntegerField(default=0)
    activo = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['orden']
        verbose_name_plural = "Categorías"
    
    def __str__(self):
        return f"{self.icono} {self.nombre}"


class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    emoji = models.CharField(max_length=10, default='🍔')
    activo = models.BooleanField(default=True)
    requiere_sabor = models.BooleanField(default=False, help_text="Para alitas")
    incluye_papas = models.BooleanField(default=True, help_text="Hamburguesas incluyen papas")
    
    # Gestión de inventario
    stock_disponible = models.BooleanField(default=True)
    cantidad_vendida_hoy = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['categoria', 'nombre']
    
    def __str__(self):
        return f"{self.nombre} - ${self.precio}"


class SaborAlitas(models.Model):
    nombre = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre
