from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.utils import timezone
from pedidos.models import Pedido


def panel_cocina(request):
    """Panel principal de cocina"""
    pedidos_pendientes = Pedido.objects.filter(
        estado__in=['pendiente', 'preparando', 'listo']
    ).order_by('creado')
    
    context = {
        'pedidos': pedidos_pendientes,
    }
    return render(request, 'cocina/panel.html', context)


@require_POST
def actualizar_estado_pedido(request, pedido_id):
    """Actualizar estado de un pedido"""
    try:
        pedido = Pedido.objects.get(id=pedido_id)
        nuevo_estado = request.POST.get('estado')
        
        if nuevo_estado in dict(Pedido.ESTADOS):
            pedido.estado = nuevo_estado
            
            # Registrar timestamps
            if nuevo_estado == 'preparando' and not pedido.hora_preparacion:
                pedido.hora_preparacion = timezone.now()
            elif nuevo_estado == 'listo' and not pedido.hora_listo:
                pedido.hora_listo = timezone.now()
            elif nuevo_estado == 'entregado' and not pedido.hora_entregado:
                pedido.hora_entregado = timezone.now()
            
            pedido.save()
            
            return JsonResponse({'success': True})
        
        return JsonResponse({'success': False, 'error': 'Estado inválido'}, status=400)
    
    except Pedido.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Pedido no encontrado'}, status=404)


def obtener_pedidos_activos(request):
    """Endpoint para actualización en tiempo real"""
    pedidos = Pedido.objects.filter(
        estado__in=['pendiente', 'preparando', 'listo']
    ).values(
        'id', 'numero', 'mesa', 'estado', 'creado', 'total'
    ).order_by('creado')
    
    return JsonResponse(list(pedidos), safe=False)