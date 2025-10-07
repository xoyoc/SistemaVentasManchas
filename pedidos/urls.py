from django.urls import path
from . import views

app_name = 'pedidos'

urlpatterns = [
    path('tomar/', views.tomar_pedido, name='tomar_pedido'),
    path('crear/', views.crear_pedido, name='crear_pedido'),
    path('ticket/<int:pedido_id>/', views.ticket_pedido, name='ticket_pedido'),
]