from django.contrib import admin
from django.utils.html import format_html
from django.db.models import Sum, Count
from .models import Pedido, ItemPedido


class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 0
    readonly_fields = ['subtotal']
    fields = ['producto', 'cantidad', 'sabor', 'precio_unitario', 'subtotal', 'notas']


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['numero', 'mesa', 'estado_badge', 'total', 'creado', 'tomado_por', 'tiempo_transcurrido']
    list_filter = ['estado', 'creado', 'tomado_por']
    search_fields = ['numero', 'mesa', 'notas']
    readonly_fields = ['numero', 'creado', 'actualizado', 'subtotal', 'total']
    inlines = [ItemPedidoInline]
    
    fieldsets = (
        ('Información del Pedido', {
            'fields': ('numero', 'mesa', 'estado', 'tomado_por')
        }),
        ('Tiempos', {
            'fields': ('creado', 'actualizado', 'hora_preparacion', 'hora_listo', 'hora_entregado')
        }),
        ('Totales', {
            'fields': ('subtotal', 'total')
        }),
        ('Notas', {
            'fields': ('notas',)
        }),
    )
    
    def estado_badge(self, obj):
        colores = {
            'pendiente': '#EF4444',
            'preparando': '#F59E0B',
            'listo': '#10B981',
            'entregado': '#3B82F6',
            'cancelado': '#6B7280'
        }
        color = colores.get(obj.estado, '#6B7280')
        return format_html(
            '<span style="background: {}; color: white; padding: 5px 10px; border-radius: 5px; font-weight: bold;">{}</span>',
            color,
            obj.get_estado_display()
        )
    estado_badge.short_description = 'Estado'
    
    def tiempo_transcurrido(self, obj):
        from django.utils import timezone
        diferencia = timezone.now() - obj.creado
        minutos = int(diferencia.total_seconds() / 60)
        
        if minutos < 60:
            return f"{minutos} min"
        else:
            horas = minutos // 60
            mins = minutos % 60
            return f"{horas}h {mins}min"
    tiempo_transcurrido.short_description = 'Tiempo'
    
    actions = ['exportar_reporte_dia']
    
    def exportar_reporte_dia(self, request, queryset):
        from django.http import HttpResponse
        import csv
        from datetime import date
        
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="pedidos_{date.today()}.csv"'
        
        writer = csv.writer(response)
        writer.writerow(['Número', 'Mesa', 'Estado', 'Total', 'Fecha', 'Atendió'])
        
        for pedido in queryset:
            writer.writerow([
                pedido.numero,
                pedido.mesa,
                pedido.get_estado_display(),
                pedido.total,
                pedido.creado.strftime('%Y-%m-%d %H:%M'),
                pedido.tomado_por.username if pedido.tomado_por else 'N/A'
            ])
        
        return response
    exportar_reporte_dia.short_description = 'Exportar a CSV'


@admin.register(ItemPedido)
class ItemPedidoAdmin(admin.ModelAdmin):
    list_display = ['pedido', 'producto', 'cantidad', 'sabor', 'precio_unitario', 'subtotal']
    list_filter = ['producto', 'sabor']
    search_fields = ['pedido__numero', 'producto__nombre']
    readonly_fields = ['precio_unitario', 'subtotal']


# Personalización del Admin
admin.site.site_header = "⚡ MANCHAS - Administración"
admin.site.site_title = "MANCHAS POS"
admin.site.index_title = "Panel de Control"
