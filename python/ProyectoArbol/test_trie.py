from src.tree import Arbol

print("=== TEST 1: Crear árbol con varios nodos ===")
arbol = Arbol()
arbol.crear_nodo("/root", "documentos", "carpeta")
arbol.crear_nodo("/root", "descargas", "carpeta")
arbol.crear_nodo("/root", "desktop", "carpeta")
arbol.crear_nodo("/root/documentos", "doc1.txt", "archivo")
arbol.crear_nodo("/root/documentos", "doc2.txt", "archivo")
arbol.crear_nodo("/root/descargas", "data.csv", "archivo")

arbol.mostrar_arbol()

print("\n=== TEST 2: Búsqueda exacta ===")
ids = arbol.trie.buscar_exacto("documentos")
print(f"Búsqueda exacta 'documentos': {ids}")
for node_id in ids:
    nodo = arbol.obtener_nodo_por_id(node_id)
    print(f"  → {nodo.nombre} ({nodo.obtener_ruta()})")

print("\n=== TEST 3: Búsqueda por prefijo ===")
ids = arbol.trie.buscar_prefijo("do")
print(f"Búsqueda prefijo 'do': {ids}")
for node_id in ids:
    nodo = arbol.obtener_nodo_por_id(node_id)
    print(f"  → {nodo.nombre} ({nodo.obtener_ruta()})")

print("\n=== TEST 4: Autocompletado ===")
resultados = arbol.trie.autocompletar("de", arbol)
print(f"Autocompletar 'de':")
for r in resultados:
    print(f"  [{r['id']}] {r['nombre']} ({r['tipo']}) - {r['ruta']}")

print("\n=== TEST 5: Búsqueda después de renombrar ===")
arbol.renombrar_nodo(1, "mis_docs")
ids = arbol.trie.buscar_exacto("documentos")
print(f"Búsqueda 'documentos' después de renombrar: {ids} (debe estar vacío)")
ids = arbol.trie.buscar_exacto("mis_docs")
print(f"Búsqueda 'mis_docs': {ids}")

print("\n=== TEST 6: Búsqueda después de eliminar ===")
arbol.eliminar_nodo(2)
ids = arbol.trie.buscar_prefijo("de")
print(f"Búsqueda 'de' después de eliminar descargas:")
for node_id in ids:
    nodo = arbol.obtener_nodo_por_id(node_id)
    if nodo:
        print(f"  → {nodo.nombre}")

print("\n=== TEST 7: Persistencia y reconstrucción ===")
arbol.guardar_json("data/test_trie.json")
arbol2 = Arbol()
arbol2.cargar_json("data/test_trie.json")
resultados = arbol2.trie.autocompletar("d", arbol2)
print(f"Autocompletar 'd' después de cargar:")
for r in resultados:
    print(f"  [{r['id']}] {r['nombre']}")