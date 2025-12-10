from src.tree import Arbol

# Crear árbol
arbol = Arbol()

print("=== PRUEBA 1: Crear estructura ===")
arbol.crear_nodo("/root", "documentos", "carpeta")
arbol.crear_nodo("/root", "fotos", "carpeta")
arbol.crear_nodo("/root/documentos", "nota.txt", "archivo", "Hola mundo")
arbol.crear_nodo("/root/documentos", "trabajo", "carpeta")
arbol.mostrar_arbol()

print("\n=== PRUEBA 2: Búsqueda por ID ===")
nodo = arbol.obtener_nodo_por_id(3)
print(f"Nodo ID 3: {nodo.nombre if nodo else 'No encontrado'}")

print("\n=== PRUEBA 3: Listar contenido ===")
hijos, msg = arbol.listar_hijos("/root")
if hijos:
    for id_n, nombre, tipo in hijos:
        print(f"  ID: {id_n}, Nombre: {nombre}, Tipo: {tipo}")

print("\n=== PRUEBA 4: Mover nodo ===")
exito, msg = arbol.mover_nodo(3, "/root/fotos")
print(msg)
arbol.mostrar_arbol()

print("\n=== PRUEBA 5: Renombrar ===")
exito, msg = arbol.renombrar_nodo(1, "docs")
print(msg)
arbol.mostrar_arbol()

print("\n=== PRUEBA 6: Eliminar con papelera ===")
ids, msg = arbol.eliminar_nodo(2, usar_papelera=True)
print(f"{msg} - IDs: {ids}")
arbol.mostrar_arbol()

print("\n=== PRUEBA 7: Ver papelera ===")
items, msg = arbol.ver_papelera()
if items:
    for i, node_id, nombre, tipo, cant in items:
        print(f"  [{i}] ID:{node_id} - {nombre} ({tipo}) - {cant} elementos")

print("\n=== PRUEBA 8: Altura y tamaño ===")
print(f"Altura del árbol: {arbol.calcular_altura()}")
print(f"Tamaño del árbol: {arbol.calcular_tamano()}")

print("\n=== PRUEBA 9: Navegación (cd/pwd) ===")
print(f"Directorio actual: {arbol.obtener_directorio_actual()}")
exito, msg = arbol.cambiar_directorio("/root/docs")
print(msg)
print(f"Directorio actual: {arbol.obtener_directorio_actual()}")