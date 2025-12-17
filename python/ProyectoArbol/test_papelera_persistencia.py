"""Test de persistencia de papelera."""
from src.tree import Arbol
import os

print("=== TEST: PERSISTENCIA DE PAPELERA ===\n")

# Crear árbol y estructura
arbol1 = Arbol()
arbol1.crear_nodo("/root", "carpeta1", "carpeta")
arbol1.crear_nodo("/root/carpeta1", "archivo1.txt", "archivo", "Contenido 1")
arbol1.crear_nodo("/root/carpeta1", "archivo2.txt", "archivo", "Contenido 2")
arbol1.crear_nodo("/root", "carpeta2", "carpeta")

print("1. Árbol inicial:")
arbol1.mostrar_arbol()

# Eliminar nodo a papelera
print("\n2. Eliminando carpeta1 (con 2 archivos) a papelera...")
ids, msg = arbol1.eliminar_nodo(1, usar_papelera=True)
print(f"   {msg}")

print("\n3. Papelera ANTES de guardar:")
items, msg = arbol1.ver_papelera()
for i, node_id, nombre, tipo, cant in items:
    print(f"   [{i}] {nombre} (ID: {node_id}) - {cant} elementos")

# Guardar con papelera
print("\n4. Guardando árbol con papelera...")
arbol1.guardar_json("data/test_papelera.json")
print("   ✓ Guardado")

# Cargar en nuevo árbol
print("\n5. Cargando en nuevo árbol...")
arbol2 = Arbol()
exito, msg = arbol2.cargar_json("data/test_papelera.json")
print(f"   {msg}")

print("\n6. Árbol cargado:")
arbol2.mostrar_arbol()

print("\n7. Papelera DESPUÉS de cargar:")
items, msg = arbol2.ver_papelera()
if items:
    for i, node_id, nombre, tipo, cant in items:
        print(f"   [{i}] {nombre} (ID: {node_id}) - {cant} elementos")
    print(f"\n   ✓ PAPELERA RESTAURADA CORRECTAMENTE")
else:
    print(f"   ❌ ERROR: {msg}")

# Probar restauración desde papelera cargada
print("\n8. Restaurando desde papelera cargada...")
exito, msg = arbol2.restaurar_papelera(0)
print(f"   {msg}")

print("\n9. Árbol después de restaurar:")
arbol2.mostrar_arbol()

print("\n10. Verificación de contenido restaurado:")
nodo = arbol2.obtener_nodo_por_id(2)
if nodo:
    print(f"    ✓ Archivo encontrado: {nodo.nombre}")
    print(f"    ✓ Contenido: {nodo.contenido}")
else:
    print("    ❌ ERROR: Nodo no encontrado")

print("\n=== TEST COMPLETADO ===")