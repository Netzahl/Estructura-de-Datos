#!/usr/bin/env python3
"""
Script de demostración automatizada del sistema de archivos.
Muestra todas las funcionalidades principales del proyecto.
"""

from src.tree import Arbol
import time
import os

def limpiar_pantalla():
    """Limpia la pantalla."""
    os.system('cls' if os.name == 'nt' else 'clear')

def pausa(segundos=2):
    """Pausa la ejecución."""
    time.sleep(segundos)

def titulo(texto):
    """Muestra un título."""
    print("\n" + "=" * 60)
    print(f"  {texto}")
    print("=" * 60 + "\n")

def demo():
    """Ejecuta la demostración completa."""
    
    limpiar_pantalla()
    print("\n🌳 DEMOSTRACIÓN - SISTEMA DE ARCHIVOS CON ÁRBOL GENERAL")
    print("=" * 60)
    pausa(2)
    
    # Crear árbol
    titulo("1. CREACIÓN DE ESTRUCTURA BÁSICA")
    arbol = Arbol()
    
    print("📁 Creando carpetas...")
    arbol.crear_nodo("/root", "proyectos", "carpeta")
    arbol.crear_nodo("/root", "documentos", "carpeta")
    arbol.crear_nodo("/root", "descargas", "carpeta")
    print("✓ Carpetas creadas\n")
    pausa(1)
    
    print("📄 Creando archivos...")
    arbol.crear_nodo("/root/proyectos", "web", "carpeta")
    arbol.crear_nodo("/root/proyectos/web", "index.html", "archivo", "<html>Hola Mundo</html>")
    arbol.crear_nodo("/root/proyectos/web", "style.css", "archivo", "body { margin: 0; }")
    arbol.crear_nodo("/root/documentos", "README.md", "archivo", "# Mi Proyecto")
    arbol.crear_nodo("/root/documentos", "notas.txt", "archivo", "Notas importantes")
    print("✓ Archivos creados\n")
    pausa(1)
    
    print("🌳 Estructura actual:")
    arbol.mostrar_arbol()
    pausa(3)
    
    # Búsqueda con Trie
    titulo("2. BÚSQUEDA Y AUTOCOMPLETADO (TRIE)")
    
    print("🔍 Búsqueda exacta de 'web':")
    ids = arbol.trie.buscar_exacto("web")
    for node_id in ids:
        nodo = arbol.obtener_nodo_por_id(node_id)
        print(f"  → Encontrado: {nodo.nombre} (ID: {nodo.id}) en {nodo.obtener_ruta()}")
    pausa(2)
    
    print("\n🔍 Autocompletado con prefijo 'no':")
    resultados = arbol.trie.autocompletar("no", arbol)
    for r in resultados:
        icono = "📁" if r['tipo'] == "carpeta" else "📄"
        print(f"  {icono} {r['nombre']} - {r['ruta']}")
    pausa(2)
    
    print("\n🔍 Búsqueda por prefijo 'do':")
    ids = arbol.trie.buscar_prefijo("do")
    for node_id in ids:
        nodo = arbol.obtener_nodo_por_id(node_id)
        print(f"  → {nodo.nombre} ({nodo.obtener_ruta()})")
    pausa(3)
    
    # Operaciones CRUD
    titulo("3. OPERACIONES: MOVER, RENOMBRAR, ELIMINAR")
    
    print("📦 Moviendo 'notas.txt' de /documentos a /proyectos:")
    nodo_notas = arbol._encontrar_nodo_por_ruta("/root/documentos/notas.txt")
    exito, msg = arbol.mover_nodo(nodo_notas.id, "/root/proyectos")
    print(f"  {msg}")
    arbol.mostrar_arbol()
    pausa(3)
    
    print("\n✏️ Renombrando 'proyectos' a 'mis_proyectos':")
    nodo_proyectos = arbol._encontrar_nodo_por_ruta("/root/proyectos")
    exito, msg = arbol.renombrar_nodo(nodo_proyectos.id, "mis_proyectos")
    print(f"  {msg}")
    arbol.mostrar_arbol()
    pausa(3)
    
    print("\n🗑️ Eliminando carpeta 'descargas' (va a papelera):")
    nodo_descargas = arbol._encontrar_nodo_por_ruta("/root/descargas")
    ids, msg = arbol.eliminar_nodo(nodo_descargas.id, usar_papelera=True)
    print(f"  {msg}")
    arbol.mostrar_arbol()
    pausa(2)
    
    print("\n📋 Contenido de la papelera:")
    items, msg = arbol.ver_papelera()
    for i, node_id, nombre, tipo, cant in items:
        print(f"  [{i}] {nombre} (ID: {node_id}) - {cant} elemento(s)")
    pausa(3)
    
    # Persistencia
    titulo("4. PERSISTENCIA JSON")
    
    print("💾 Guardando árbol en JSON...")
    arbol.guardar_json("data/demo_arbol.json")
    print("✓ Árbol guardado en 'data/demo_arbol.json'\n")
    pausa(2)
    
    print("📂 Cargando árbol desde JSON...")
    arbol2 = Arbol()
    exito, msg = arbol2.cargar_json("data/demo_arbol.json")
    print(f"✓ {msg}")
    print(f"  Total de nodos: {len(arbol2.nodos)}")
    print(f"  Contador ID: {arbol2.contador_id}")
    pausa(2)
    
    print("\n✓ Verificación: Árbol cargado correctamente")
    arbol2.mostrar_arbol()
    pausa(3)
    
    # Export preorden
    titulo("5. EXPORT RECORRIDO PREORDEN")
    
    print("📋 Generando recorrido en preorden...")
    recorrido, msg = arbol2.exportar_preorden("data/demo_preorden.json")
    print(f"✓ {msg}")
    print(f"\n  Total de nodos en recorrido: {len(recorrido)}\n")
    
    print("Orden de visita (preorden: Raíz → Hijos):")
    for item in recorrido:
        icono = "📁" if item['tipo'] == "carpeta" else "📄"
        print(f"  {icono} {item['ruta']}")
    pausa(3)
    
    # Papelera y restauración
    titulo("6. RESTAURACIÓN DESDE PAPELERA")
    
    print("♻️ Restaurando 'descargas' desde papelera...")
    exito, msg = arbol2.restaurar_papelera(0)
    print(f"✓ {msg}\n")
    arbol2.mostrar_arbol()
    pausa(2)
    
    print("\n📋 Papelera después de restaurar:")
    items, msg = arbol2.ver_papelera()
    if items:
        for i, node_id, nombre, tipo, cant in items:
            print(f"  [{i}] {nombre}")
    else:
        print(f"  {msg}")
    pausa(3)
    
    # Cálculos del árbol
    titulo("7. INFORMACIÓN DEL ÁRBOL")
    
    altura = arbol2.calcular_altura()
    tamano = arbol2.calcular_tamano()
    
    print(f"📊 Estadísticas del árbol:")
    print(f"  • Altura: {altura}")
    print(f"  • Total de nodos: {tamano}")
    print(f"  • Nodos en hash map: {len(arbol2.nodos)}")
    print(f"  • Elementos en Trie: {len([k for k in arbol2.nodos.keys()])}")
    pausa(3)
    
    # Final
    titulo("✅ DEMOSTRACIÓN COMPLETADA")
    print("Funcionalidades demostradas:")
    print("  ✓ Creación de estructura jerárquica")
    print("  ✓ Búsqueda eficiente con Trie (exacta, prefijo, autocompletado)")
    print("  ✓ Operaciones CRUD (crear, mover, renombrar, eliminar)")
    print("  ✓ Sistema de papelera con restauración")
    print("  ✓ Persistencia completa en JSON")
    print("  ✓ Export de recorrido preorden")
    print("  ✓ Cálculos sobre el árbol")
    print("\n" + "=" * 60)
    print("🎉 Gracias por ver la demostración")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    try:
        demo()
    except KeyboardInterrupt:
        print("\n\n⚠️ Demostración interrumpida")
    except Exception as e:
        print(f"\n\n❌ Error en la demostración: {e}")