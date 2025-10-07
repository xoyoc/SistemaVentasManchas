from django.contrib import admin
from django.utils.html import format_html
from .models import Categoria, Producto, SaborAlitas


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['icono_display', 'nombre', 'orden', 'activo', 'cantidad_productos']
    list_editable = ['orden', 'activo']
    list_filter = ['activo']
    search_fields = ['nombre']
    
    def icono_display(self, obj):
        return format_html('<span style="font-size: 24px;">{}</span>', obj.icono)
    icono_display.short_description = 'Icono'
    
    def cantidad_productos(self, obj):
        return obj.productos.count()
    cantidad_productos.short_description = 'Productos'


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['emoji_display', 'nombre', 'categoria', 'precio', 'activo', 'stock_disponible', 'vendidos_hoy']
    list_editable = ['precio', 'activo', 'stock_disponible']
    list_filter = ['categoria', 'activo', 'stock_disponible', 'requiere_sabor']
    search_fields = ['nombre', 'descripcion']
    readonly_fields = ['cantidad_vendida_hoy']
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('categoria', 'nombre', 'descripcion', 'precio')
        }),
        ('Visual', {
            'fields': ('imagen', 'emoji')
        }),
        ('Configuración', {
            'fields': ('activo', 'requiere_sabor', 'incluye_papas')
        }),
        ('Inventario', {
            'fields': ('stock_disponible', 'cantidad_vendida_hoy')
        }),
    )
    
    def emoji_display(self, obj):
        if obj.imagen:
            return format_html('<img src="{}" style="width: 40px; height: 40px; object-fit: cover; border-radius: 5px;" />', obj.imagen.url)
        return format_html('<span style="font-size: 32px;">{}</span>', obj.emoji)
    emoji_display.short_description = ''
    
    def vendidos_hoy(self, obj):
        return f"{obj.cantidad_vendida_hoy} unidades"
    vendidos_hoy.short_description = 'Vendidos Hoy'
    
    actions = ['resetear_contador_diario', 'marcar_agotado', 'marcar_disponible']
    
    def resetear_contador_diario(self, request, queryset):
        queryset.update(cantidad_vendida_hoy=0)
        self.message_user(request, 'Contadores diarios reseteados')
    resetear_contador_diario.short_description = 'Resetear contador diario'
    
    def marcar_agotado(self, request, queryset):
        queryset.update(stock_disponible=False)
        self.message_user(request, f'{queryset.count()} productos marcados como agotados')
    marcar_agotado.short_description = 'Marcar como agotado'
    
    def marcar_disponible(self, request, queryset):
        queryset.update(stock_disponible=True)
        self.message_user(request, f'{queryset.count()} productos marcados como disponibles')
    marcar_disponible.short_description = 'Marcar como disponible'


@admin.register(SaborAlitas)
class SaborAlitasAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'activo']
    list_editable = ['activo']