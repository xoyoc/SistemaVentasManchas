from django.urls import path
from . import views

app_name = 'cocina'

urlpatterns = [
    path('panel/', views.panel_cocina, name='panel'),
    path('actualizar/<int:pedido_id>/', views.actualizar_estado_pedido, name='actualizar_estado'),
    path('api/pedidos-activos/', views.obtener_pedidos_activos, name='pedidos_activos'),
]