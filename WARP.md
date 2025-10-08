# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

**Manchas POS** is a Django-based Point of Sale system designed specifically for a restaurant called "MANCHAS". The system provides separate interfaces for:
- Order taking (meseros/cashiers) with visual product selection
- Kitchen management with real-time order tracking 
- Administrative management through Django admin

## Development Setup

### Essential Commands

```bash
# Environment setup
python -m venv venv_manchas
source venv_manchas/bin/activate  # macOS/Linux
# venv_manchas\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
npm install

# Database management
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

# Populate initial menu data
python populate_menu.py

# CSS compilation (Tailwind)
npm run build:css          # Production build
npm run watch:css          # Development with auto-rebuild

# Run development server
python manage.py runserver
python manage.py runserver 0.0.0.0:8000  # Network access for tablets
```

### Testing Commands

```bash
# Run tests for specific apps
python manage.py test menu
python manage.py test pedidos
python manage.py test cocina

# Run all tests
python manage.py test

# Test specific test cases
python manage.py test pedidos.tests.TestPedidoCreation
```

### Daily Maintenance

```bash
# Reset daily sales counter (should be automated)
python manage.py reset_ventas_diarias

# Backup database
cp db.sqlite3 backup_$(date +%Y%m%d).sqlite3
```

## Architecture & Structure

### Application Structure
This is a modular Django project with three core apps:

- **`menu/`**: Product catalog, categories, flavors (wings), and inventory tracking
- **`pedidos/`**: Order management, order items, and order workflow
- **`cocina/`**: Kitchen panel for real-time order tracking and status updates
- **`manchas/`**: Main project settings and URL routing

### Key Models & Relationships

**Menu System**:
- `Categoria` → `Producto` (one-to-many)
- `Producto` ←→ `SaborAlitas` (many-to-many for wing flavors)
- Products have inventory tracking (`stock_disponible`, `cantidad_vendida_hoy`)

**Order System**:
- `Pedido` → `ItemPedido` (one-to-many)
- `ItemPedido` → `Producto` (foreign key)
- `ItemPedido` → `SaborAlitas` (optional for wings)

**Order State Machine**:
```
pendiente → preparando → listo → entregado
         ↘            ↙
           cancelado
```

### URL Structure
- `/` → Redirects to order taking interface
- `/pedidos/tomar/` → Main order taking interface (tablets/cashiers)
- `/pedidos/crear/` → API endpoint for order creation
- `/pedidos/ticket/<id>/` → Print-ready ticket view
- `/cocina/panel/` → Real-time kitchen dashboard
- `/cocina/api/pedidos-activos/` → API for active orders
- `/admin/` → Django admin for menu/order management

### Frontend Technology
- **Tailwind CSS** with custom Manchas branding colors
- **Alpine.js** for interactive components (implied from structure)
- Mobile-first responsive design optimized for tablets
- Print-optimized ticket layout (80mm thermal printers)

## Key Business Logic

### Order Number Generation
Orders use format: `YYMMDD-XXX` (e.g., `241208-001`)

### Product Categories & Pricing
- Hamburgers ($70-$120) - include fries by default
- Wings (6pc: $85, 12pc: $170) - require flavor selection (BBQ, Habanero, Buffalo)
- Dogos ($28-$35)
- Papas ($95-$145) 
- Others ($50)
- Drinks ($12-$25) - don't include fries

### Kitchen Workflow
Real-time updates between order-taking and kitchen interfaces. Orders flow through states with timestamps for performance tracking.

## Environment Configuration

### Required Environment Variables
Create `.env` file:
```bash
SECRET_KEY=your-secret-key-here
DEBUG=True  # False for production
```

### Database
- **Development**: SQLite (`db.sqlite3`)
- **Production**: Recommended PostgreSQL migration

### Static Files
- Input CSS: `./static/css/input.css`
- Output CSS: `./static/css/output.css` (built by Tailwind)
- Static files served from `./static/` and `./staticfiles/`
- Media files (product images): `./media/`

## Network Deployment for Tablets

The system is designed for tablet access on local networks:

```bash
# Find local IP
ifconfig  # macOS/Linux
ipconfig  # Windows

# Run server for network access
python manage.py runserver 0.0.0.0:8000

# Access from tablets: http://YOUR_IP:8000/pedidos/tomar/
```

## Development Notes

### Localization
- Configured for Mexican Spanish (`es-mx`)
- Timezone: `America/Mexico_City`
- Currency formatting assumes Mexican pesos

### Print Integration
Uses standard `window.print()` for thermal receipt printers (80mm width). Tickets are formatted for Courier New monospace font.

### Dependencies
- **Django 5.2.7** - Main framework
- **Channels** - WebSocket support for real-time updates
- **Redis** - Channel layer backend
- **Pillow** - Image handling for product photos
- **python-decouple** - Environment variable management
- **Tailwind CSS 3.4.18** - Styling framework

## Common Development Tasks

### Adding New Products
1. Use Django admin: `/admin/menu/producto/`
2. Or extend `populate_menu.py` script
3. Rebuild CSS if using new categories: `npm run build:css`

### Modifying Order States
Update `ESTADOS` choices in `pedidos/models.py` and corresponding templates.

### Custom Styling
Edit `tailwind.config.js` brand colors and run `npm run build:css`.

### API Extensions
Kitchen panel uses `/cocina/api/pedidos-activos/` - extend this for mobile apps or integrations.