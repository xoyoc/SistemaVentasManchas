# 🍔⚡ MANCHAS POS

Sistema de Punto de Venta diseñado específicamente para el restaurante MANCHAS.

## 🎯 Características Principales

### 📱 Para el Mesero/Caja
- ✅ Interfaz visual con fotos de productos
- ✅ Toma de pedidos rápida y sin errores
- ✅ Cálculo automático de totales
- ✅ Gestión de múltiples mesas
- ✅ Impresión de tickets
- ✅ Selección de sabores para alitas

### 👨‍🍳 Para la Cocina
- ✅ Panel en tiempo real de pedidos
- ✅ Sistema de estados (Pendiente → Preparando → Listo)
- ✅ Tickets claros con todos los detalles
- ✅ Contador de tiempo transcurrido
- ✅ Alertas visuales por prioridad
- ✅ Sin papeles perdidos

### 🛠️ Para el Administrador
- ✅ Panel de administración Django
- ✅ Control de inventario básico
- ✅ Reportes de ventas diarias
- ✅ Gestión de menú y precios
- ✅ Estadísticas de productos más vendidos
- ✅ Exportación de datos a CSV

## 🚀 Instalación Rápida

```bash
# 1. Clonar el proyecto
git clone <tu-repositorio>
cd manchas_pos

# 2. Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\\Scripts\\activate

# 3. Instalar dependencias
pip install -r requirements.txt
npm install

# 4. Configurar base de datos
python manage.py migrate

# 5. Crear superusuario
python manage.py createsuperuser

# 6. Poblar menú
python populate_menu.py

# 7. Construir CSS
npm run build:css

# 8. Iniciar servidor
python manage.py runserver
```

## 📖 Uso del Sistema

### Tomar un Pedido

1. Acceder a `/pedidos/tomar/`
2. Seleccionar categoría de producto
3. Hacer clic en productos para agregarlos
4. Ajustar cantidades con +/-
5. Ingresar número de mesa
6. Clic en "Enviar a Cocina"
7. El ticket se imprime automáticamente

### Panel de Cocina

1. Acceder a `/cocina/panel/`
2. Ver pedidos en tiempo real
3. Cambiar estados:
   - **Rojo (Pendiente)**: Clic en "Empezar a Preparar"
   - **Amarillo (Preparando)**: Clic en "Marcar Listo"
   - **Verde (Listo)**: Clic en "Entregar"

### Administración

1. Acceder a `/admin/`
2. **Menú**: Agregar/editar productos y categorías
3. **Pedidos**: Ver historial completo
4. **Reportes**: Exportar ventas del día

## 📊 Menú Actual

### Hamburguesas
- Hamburguesa Solitaria - $70
- H. Bacon - $90
- H. Omar - $95
- H. Crazy - $100
- H. MataHambre - $110
- H. Hawaiana - $120

### Dogos
- Dogo Sencillo - $28
- Dogo Bacon - $35

### Alitas
- 12 piezas - $170
- 6 piezas - $85
- Sabores: BBQ, Habanero, Buffalo

### Papas
- Papas a la Francesa - $95
- Papas Manchas (Locas) - $145

### Otros
- Salchipulpos - $50

### Bebidas
- Refresco 600ml - $25
- Agua Natural 600ml - $12

## 🔧 Mantenimiento

### Resetear ventas diarias
```bash
python manage.py reset_ventas_diarias
```

### Backup de base de datos
```bash
cp db.sqlite3 backup_$(date +%Y%m%d).sqlite3
```

### Actualizar precios
Desde el admin de Django: `/admin/menu/producto/`

## 📱 Configuración para Tablet

### Acceso en red local

1. Obtén tu IP:
   ```bash
   # Windows
   ipconfig
   
   # Mac/Linux
   ifconfig
   ```

2. Ejecuta el servidor:
   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```

3. Accede desde tablet:
   ```
   http://TU_IP:8000/pedidos/tomar/
   ```

### Modo Pantalla Completa

- **iPad**: Safari → Compartir → "Añadir a inicio"
- **Android**: Chrome → Menú → "Añadir a pantalla de inicio"
- **PC**: F11 para pantalla completa

## 🖨️ Impresora Térmica

### Configuración

1. Conectar impresora USB
2. Instalar drivers
3. Configurar como predeterminada
4. El sistema usa `window.print()` estándar

### Formato de Ticket

- Ancho: 80mm
- Fuente: Courier New (monospace)
- Incluye: Logo, pedido, items, totales
- Optimizado para impresión térmica

## 🎨 Personalización

### Cambiar colores del tema

Editar `tailwind.config.js`:
```javascript
theme: {
  extend: {
    colors: {
      'manchas-yellow': '#TU_COLOR',
      'manchas-black': '#TU_COLOR',
    }
  }
}
```

Luego reconstruir:
```bash
npm run build:css
```

### Agregar productos

1. Admin → Menú → Productos → Agregar
2. O usar el script `populate_menu.py`

## 📞 Información de Contacto

**MANCHAS**
- Teléfono: 753 102 1814
- Sistema desarrollado con Django + Tailwind CSS

## 📄 Licencia

Este sistema fue desarrollado específicamente para MANCHAS.

## 🙏 Créditos

- Framework: Django 5.0
- CSS: Tailwind CSS 3.4
- JavaScript: Alpine.js
- Iconos: Lucide Icons

---

**¿Problemas o sugerencias?** Contacta al desarrollador.