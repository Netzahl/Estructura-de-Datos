from src.tree import Arbol
import os

print("=== TEST 1: Crear árbol y guardar ===")
arbol = Arbol()
arbol.crear_nodo("/root", "proyectos", "carpeta")
arbol.crear_nodo("/root/proyectos", "web", "carpeta")
arbol.crear_nodo("/root/proyectos/web", "index.html", "archivo", "<html>Hola</html>")
arbol.crear_nodo("/root/proyectos/web", "style.css", "archivo", "body { color: red; }")
arbol.crear_nodo("/root", "README.md", "archivo", "# Mi Proyecto")

print("\n--- Árbol original ---")
arbol.mostrar_arbol()
print(f"Total de nodos: {len(arbol.nodos)}")
print(f"Contador ID: {arbol.contador_id}")

# Guardar
exito, msg = arbol.guardar_json("data/test_arbol.json")
print(f"\n{msg}")

print("\n=== TEST 2: Cargar árbol desde JSON ===")
arbol2 = Arbol()
exito, msg = arbol2.cargar_json("data/test_arbol.json")
print(msg)

print("\n--- Árbol cargado ---")
arbol2.mostrar_arbol()
print(f"Total de nodos: {len(arbol2.nodos)}")
print(f"Contador ID: {arbol2.contador_id}")

# Verificar integridad
print("\n=== TEST 3: Verificar integridad ===")
print("Buscando nodo por ID...")
nodo = arbol2.obtener_nodo_por_id(3)
if nodo:
    print(f"✓ Nodo ID 3: {nodo.nombre} - Ruta: {nodo.obtener_ruta()}")
else:
    print("✗ Error: Nodo no encontrado")

print("\nBuscando por ruta...")
nodo = arbol2._encontrar_nodo_por_ruta("/root/proyectos/web")
if nodo:
    print(f"✓ Nodo en /root/proyectos/web: {nodo.nombre}")
    print(f"  Hijos: {[h.nombre for h in nodo.children]}")
else:
    print("✗ Error: Ruta no encontrada")

print("\n=== TEST 4: Modificar y guardar de nuevo ===")
arbol2.crear_nodo("/root/proyectos", "mobile", "carpeta")
arbol2.renombrar_nodo(1, "mis_proyectos")
arbol2.mostrar_arbol()

exito, msg = arbol2.guardar_json("data/test_arbol_modificado.json")
print(f"\n{msg}")

print("\n=== TEST 5: Exportar preorden ===")
recorrido, msg = arbol2.exportar_preorden("data/preorden.json")
print(msg)
print(f"\nPrimeros 3 elementos del recorrido:")
for item in recorrido[:3]:
    print(f"  [{item['id']}] {item['ruta']} ({item['tipo']})")

print("\n=== TEST 6: Exportar preorden sin archivo ===")
recorrido, msg = arbol2.exportar_preorden()
print(f"Total de nodos en recorrido: {len(recorrido)}")
print("Orden de visita:")
for item in recorrido:
    print(f"  {item['ruta']}")