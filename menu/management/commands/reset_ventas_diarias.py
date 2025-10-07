from django.core.management.base import BaseCommand
from menu.models import Producto


class Command(BaseCommand):
    help = 'Resetea el contador de ventas diarias de todos los productos'
    
    def handle(self, *args, **options):
        Producto.objects.all().update(cantidad_vendida_hoy=0)
        self.stdout.write(
            self.style.SUCCESS('✓ Contadores de ventas reseteados exitosamente')
        )