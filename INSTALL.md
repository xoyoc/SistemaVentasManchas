# ============================================
# Instrucciones de instalación
# INSTALL.md
# ============================================

"""
# 🍔 MANCHAS POS - Guía de Instalación

## Requisitos Previos
- Python 3.10 o superior
- pip (gestor de paquetes de Python)
- Node.js y npm (para Tailwind CSS)

## Instalación Paso a Paso

### 1. Clonar o crear el proyecto

```bash
mkdir manchas_pos
cd manchas_pos
```

### 2. Crear entorno virtual

```bash
python -m venv venv

# En Windows:
venv\\Scripts\\activate

# En Mac/Linux:
source venv/bin/activate
```

### 3. Instalar dependencias de Python

```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno

Crear archivo `.env` en la raíz del proyecto:

```env
SECRET_KEY=tu-clave-secreta-super-segura-aqui
DEBUG=True
```

### 5. Crear la base de datos

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Crear superusuario

```bash
python manage.py createsuperuser
```

### 7. Poblar el menú con datos iniciales

```bash
python populate_menu.py
```

### 8. Configurar Tailwind CSS

```bash
# Instalar dependencias de Node.js
npm install

# Construir CSS (producción)
npm run build:css

# O en modo desarrollo (auto-reconstrucción)
npm run watch:css
```

### 9. Ejecutar el servidor

```bash
python manage.py runserver
```

### 10. Acceder al sistema

- **Panel de pedidos**: http://localhost:8000/pedidos/tomar/
- **Panel de cocina**: http://localhost:8000/cocina/panel/
- **Admin**: http://localhost:8000/admin/

## 📱 Configuración para Tablet/Móvil

### Acceso desde otros dispositivos en la red local

1. Obtén tu IP local:
   - Windows: `ipconfig`
   - Mac/Linux: `ifconfig` o `ip addr`

2. Ejecuta el servidor permitiendo conexiones externas:
   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```

3. Accede desde tablet/móvil:
   ```
   http://TU_IP_LOCAL:8000/pedidos/tomar/
   ```

### Modo Kiosco (pantalla completa)

En la tablet/navegador:
- **Chrome**: F11 o Menú → "Instalar aplicación"
- **iPad**: Safari → Compartir → "Añadir a pantalla de inicio"

## 🖨️ Configuración de Impresora de Tickets

### Opción 1: Impresora Térmica USB

1. Instalar drivers de la impresora
2. Configurar como impresora predeterminada
3. En el navegador, permitir impresión automática

### Opción 2: Impresora de Red

1. Configurar IP fija en la impresora
2. Agregar impresora en el sistema operativo
3. Usar comando de impresión del navegador

## 🔧 Tareas de Mantenimiento

### Resetear contador de ventas diarias (ejecutar cada día)

```bash
python manage.py reset_ventas_diarias
```

Puedes automatizarlo con cron (Linux/Mac) o Task Scheduler (Windows).

### Backup de la base de datos

```bash
# SQLite (desarrollo)
cp db.sqlite3 db_backup_$(date +%Y%m%d).sqlite3

# PostgreSQL (producción)
pg_dump nombre_bd > backup_$(date +%Y%m%d).sql
```

## 📊 Reportes y Estadísticas

Desde el admin de Django puedes:
- Ver pedidos del día
- Exportar reportes CSV
- Ver productos más vendidos
- Gestionar inventario

## 🚀 Despliegue en Producción

### Recomendaciones:

1. **Base de datos**: Migrar a PostgreSQL
2. **Servidor web**: Usar Gunicorn + Nginx
3. **HTTPS**: Configurar certificado SSL
4. **Dominio**: Obtener dominio personalizado
5. **Hosting**: 
   - Railway.app (fácil y económico)
   - DigitalOcean
   - AWS/Azure (más complejo)

### Comandos para producción:

```bash
# Recolectar archivos estáticos
python manage.py collectstatic --noinput

# Ejecutar con Gunicorn
gunicorn config.wsgi:application --bind 0.0.0.0:8000
```

## ❓ Solución de Problemas

### Error: "No module named 'apps'"

```bash
# Asegúrate de estar en el directorio correcto
cd manchas_pos
python manage.py runserver
```

### Error: Tailwind CSS no se aplica

```bash
# Reconstruir CSS
npm run build:css
python manage.py collectstatic
```

### Error: CSRF Token

Verifica que `{% csrf_token %}` esté en todos los formularios.

## 📞 Soporte

Para dudas adicionales sobre el sistema, consulta la documentación de Django:
- https://docs.djangoproject.com/
- https://tailwindcss.com/docs

## 🎉 ¡Listo!

Tu sistema POS de MANCHAS está configurado y listo para usar.
"""