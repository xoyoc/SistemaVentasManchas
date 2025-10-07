from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from menu.models import Producto, SaborAlitas

class Pedido(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('preparando', 'Preparando'),
        ('listo', 'Listo'),
        ('entregado', 'Entregado'),
        ('cancelado', 'Cancelado'),
    ]
    
    numero = models.CharField(max_length=20, unique=True, editable=False)
    mesa = models.CharField(max_length=50, help_text="Número de mesa o nombre")
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    
    # Timestamps
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    hora_preparacion = models.DateTimeField(null=True, blank=True)
    hora_listo = models.DateTimeField(null=True, blank=True)
    hora_entregado = models.DateTimeField(null=True, blank=True)
    
    # Usuario que tomó el pedido
    tomado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='pedidos_tomados')
    
    # Totales
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    # Notas especiales
    notas = models.TextField(blank=True, help_text="Instrucciones especiales")
    
    class Meta:
        ordering = ['-creado']
    
    def __str__(self):
        return f"Pedido {self.numero} - {self.mesa}"
    
    def save(self, *args, **kwargs):
        if not self.numero:
            # Generar número de pedido: YYMMDD-XXX
            fecha = timezone.now().strftime('%y%m%d')
            ultimo = Pedido.objects.filter(numero__startswith=fecha).count()
            self.numero = f"{fecha}-{str(ultimo + 1).zfill(3)}"
        super().save(*args, **kwargs)
    
    def calcular_total(self):
        self.subtotal = sum(item.subtotal for item in self.items.all())
        self.total = self.subtotal
        self.save()


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='items')
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Para productos con opciones
    sabor = models.ForeignKey(SaborAlitas, on_delete=models.SET_NULL, null=True, blank=True)
    notas = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        sabor_str = f" ({self.sabor})" if self.sabor else ""
        return f"{self.cantidad}x {self.producto.nombre}{sabor_str}"
    
    def save(self, *args, **kwargs):
        self.precio_unitario = self.producto.precio
        self.subtotal = self.cantidad * self.precio_unitario
        super().save(*args, **kwargs)