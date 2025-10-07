from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Count, Sum
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
import json

from menu.models import Categoria, Producto, SaborAlitas
from .models import Pedido, ItemPedido


@login_required
def tomar_pedido(request):
    """Vista principal para tomar pedidos"""
    categorias = Categoria.objects.filter(activo=True).prefetch_related('productos')
    sabores = SaborAlitas.objects.filter(activo=True)
    
    context = {
        'categorias': categorias,
        'sabores': sabores,
    }
    return render(request, 'pedidos/tomar_pedido.html', context)


@require_POST
@login_required
def crear_pedido(request):
    """Crear un nuevo pedido vía AJAX"""
    try:
        data = json.loads(request.body)
        
        # Crear pedido
        pedido = Pedido.objects.create(
            mesa=data.get('mesa'),
            tomado_por=request.user,
            notas=data.get('notas', '')
        )
        
        # Agregar items
        for item_data in data.get('items', []):
            producto = Producto.objects.get(id=item_data['producto_id'])
            sabor = None
            if item_data.get('sabor_id'):
                sabor = SaborAlitas.objects.get(id=item_data['sabor_id'])
            
            ItemPedido.objects.create(
                pedido=pedido,
                producto=producto,
                cantidad=item_data['cantidad'],
                sabor=sabor,
                notas=item_data.get('notas', '')
            )
            
            # Actualizar estadísticas del producto
            producto.cantidad_vendida_hoy += item_data['cantidad']
            producto.save()
        
        # Calcular totales
        pedido.calcular_total()
        
        return JsonResponse({
            'success': True,
            'pedido_id': pedido.id,
            'numero': pedido.numero,
            'total': float(pedido.total)
        })
    
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)


@login_required
def ticket_pedido(request, pedido_id):
    """Generar ticket de pedido para imprimir"""
    pedido = get_object_or_404(Pedido, id=pedido_id)
    return render(request, 'pedidos/ticket.html', {'pedido': pedido})