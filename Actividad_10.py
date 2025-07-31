# print("prueba funcionalidad del respositorio")
producto_nuevo= {}
cantidad_productos = int(input("==Cuantos productos desea ingresar==: "))
for i in range(cantidad_productos):
    print(f"\nIngresa el producto_{i+1}: ")
    codigo = int(input(f"==Ingrese Codigo del producto: "))
    nombre = input(f"==Ingrese Nombre del producto: ")
    categoria = input(f"==Ingrese Categoria del producto: ")
    talla = input(f"==Ingrese talla del producto: ")
    precio_unitario = input(f"==Ingrese el precio unitario del produto: ")
    cantidad_stock = int(input(f"==Cantidad en stock: "))

    producto_nuevo[codigo]={ #primera clave prinicipal 'codigo'
        'nombre': nombre,
        'categoria': categoria,
        'talla': talla,
        'precio_unitario': precio_unitario,
        'cantidad_stock': cantidad_stock
    }

print(f"\n========lista/Inventario de productos Registrados======= ")
#data es la variable temporal que recorrera los valores de las claves
for codigo, data in producto_nuevo.items():
    print(f"\nCodigo: {codigo}")
    print(f"Nombre: {data['nombre']}")
    print(f"Categoria: {data['categoria']}")
    print(f"Talla: {data['talla']}")
    print(f"Precion unitario: {data['precio_unitario']}")


