import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'manchas.settings')
django.setup()

from menu.models import Categoria, Producto, SaborAlitas


def poblar_menu():
    print("🍔 Poblando menú de MANCHAS...")
    
    # Crear categorías
    categorias_data = [
        {'nombre': 'Hamburguesas', 'icono': '🍔', 'orden': 1},
        {'nombre': 'Dogos', 'icono': '🌭', 'orden': 2},
        {'nombre': 'Alitas', 'icono': '🍗', 'orden': 3},
        {'nombre': 'Papas', 'icono': '🍟', 'orden': 4},
        {'nombre': 'Otros', 'icono': '🐙', 'orden': 5},
        {'nombre': 'Bebidas', 'icono': '🥤', 'orden': 6},
    ]
    
    categorias = {}
    for cat_data in categorias_data:
        cat, created = Categoria.objects.get_or_create(
            nombre=cat_data['nombre'],
            defaults=cat_data
        )
        categorias[cat.nombre] = cat
        print(f"{'✓ Creada' if created else '• Existe'}: {cat}")
    
    # Crear sabores de alitas
    sabores_data = ['BBQ', 'Habanero', 'Buffalo']
    for sabor_nombre in sabores_data:
        sabor, created = SaborAlitas.objects.get_or_create(nombre=sabor_nombre)
        print(f"{'✓ Creado' if created else '• Existe'}: Sabor {sabor}")
    
    # Crear productos - HAMBURGUESAS
    hamburguesas_data = [
        {
            'nombre': 'Hamburguesa Solitaria',
            'precio': 70,
            'descripcion': 'Carne de res, jitomate, cebolla, chile toreado, chile en vinagre, mayonesa, catsup, mostaza y lechuga',
            'emoji': '🍔'
        },
        {
            'nombre': 'H. Bacon',
            'precio': 90,
            'descripcion': 'Carne de res, tocino, queso, jitomate, cebolla, chile toreado, chile en vinagre, mayonesa, catsup, mostaza y lechuga',
            'emoji': '🍔'
        },
        {
            'nombre': 'H. Omar',
            'precio': 95,
            'descripcion': 'Carne de res, salchicha, tocino, queso, jitomate, cebolla, chile toreado, chile en vinagre, mayonesa, catsup, mostaza y lechuga',
            'emoji': '🍔'
        },
        {
            'nombre': 'H. Crazy',
            'precio': 100,
            'descripcion': 'Carne de res, salchicha, tocino, queso, jitomate, cebolla, aguacate, chile toreado, chile en vinagre, mayonesa, catsup, mostaza y lechuga',
            'emoji': '🍔'
        },
        {
            'nombre': 'H. MataHambre',
            'precio': 110,
            'descripcion': 'Doble carne, salchicha, tocino, queso, jitomate, cebolla, aguacate, chile toreado, chile en vinagre, mayonesa, catsup, mostaza y lechuga',
            'emoji': '🍔'
        },
        {
            'nombre': 'H. Hawaiana',
            'precio': 120,
            'descripcion': 'Doble carne, salchicha, tocino, queso, piña, jitomate, cebolla, aguacate, chile toreado, chile en vinagre, mayonesa, catsup, mostaza y lechuga',
            'emoji': '🍔'
        },
    ]
    
    for producto_data in hamburguesas_data:
        prod, created = Producto.objects.get_or_create(
            nombre=producto_data['nombre'],
            categoria=categorias['Hamburguesas'],
            defaults=producto_data
        )
        print(f"{'✓ Creado' if created else '• Existe'}: {prod.nombre}")
    
    # Crear productos - DOGOS
    dogos_data = [
        {
            'nombre': 'Dogo Sencillo',
            'precio': 28,
            'descripcion': 'Salchicha, jitomate, cebolla, chile toreado, chile en vinagre, mayonesa, catsup y mostaza',
            'emoji': '🌭'
        },
        {
            'nombre': 'Dogo Bacon',
            'precio': 35,
            'descripcion': 'Salchicha con tocino, jitomate, cebolla, chile toreado, chile en vinagre, mayonesa, catsup y mostaza',
            'emoji': '🌭'
        },
    ]
    
    for producto_data in dogos_data:
        prod, created = Producto.objects.get_or_create(
            nombre=producto_data['nombre'],
            categoria=categorias['Dogos'],
            defaults=producto_data
        )
        print(f"{'✓ Creado' if created else '• Existe'}: {prod.nombre}")
    
    # Crear productos - ALITAS
    alitas_data = [
        {
            'nombre': 'Alitas (12 piezas)',
            'precio': 170,
            'descripcion': 'Orden de 12 piezas',
            'emoji': '🍗',
            'requiere_sabor': True
        },
        {
            'nombre': 'Alitas (6 piezas)',
            'precio': 85,
            'descripcion': 'Orden de 6 piezas',
            'emoji': '🍗',
            'requiere_sabor': True
        },
    ]
    
    for producto_data in alitas_data:
        prod, created = Producto.objects.get_or_create(
            nombre=producto_data['nombre'],
            categoria=categorias['Alitas'],
            defaults=producto_data
        )
        print(f"{'✓ Creado' if created else '• Existe'}: {prod.nombre}")
    
    # Crear productos - PAPAS
    papas_data = [
        {
            'nombre': 'Papas a la Francesa',
            'precio': 95,
            'descripcion': 'Orden de papas fritas aderezadas con catsup y mayonesa',
            'emoji': '🍟'
        },
        {
            'nombre': 'Papas Manchas (Locas)',
            'precio': 145,
            'descripcion': 'Orden de papas a la francesa aderezadas con tocino, queso oaxaca, jitomate, cebolla, chiles en vinagre, catsup, mostaza y mayonesa',
            'emoji': '🍟'
        },
    ]
    
    for producto_data in papas_data:
        prod, created = Producto.objects.get_or_create(
            nombre=producto_data['nombre'],
            categoria=categorias['Papas'],
            defaults=producto_data
        )
        print(f"{'✓ Creado' if created else '• Existe'}: {prod.nombre}")
    
    # Crear productos - OTROS
    otros_data = [
        {
            'nombre': 'Salchipulpos',
            'precio': 50,
            'descripcion': 'Salchicha en forma de pulpo acompañadas con papas, mayonesa, catsup y mostaza',
            'emoji': '🐙'
        },
    ]
    
    for producto_data in otros_data:
        prod, created = Producto.objects.get_or_create(
            nombre=producto_data['nombre'],
            categoria=categorias['Otros'],
            defaults=producto_data
        )
        print(f"{'✓ Creado' if created else '• Existe'}: {prod.nombre}")
    
    # Crear productos - BEBIDAS
    bebidas_data = [
        {
            'nombre': 'Refresco 600ml',
            'precio': 25,
            'descripcion': 'Refresco de 600ml',
            'emoji': '🥤',
            'incluye_papas': False
        },
        {
            'nombre': 'Agua Natural 600ml',
            'precio': 12,
            'descripcion': 'Agua natural de 600ml',
            'emoji': '💧',
            'incluye_papas': False
        },
    ]
    
    for producto_data in bebidas_data:
        prod, created = Producto.objects.get_or_create(
            nombre=producto_data['nombre'],
            categoria=categorias['Bebidas'],
            defaults=producto_data
        )
        print(f"{'✓ Creado' if created else '• Existe'}: {prod.nombre}")
    
    print("\n✅ ¡Menú poblado exitosamente!")
    print(f"📊 Total categorías: {Categoria.objects.count()}")
    print(f"📊 Total productos: {Producto.objects.count()}")
    print(f"📊 Total sabores: {SaborAlitas.objects.count()}")


if __name__ == '__main__':
    poblar_menu()