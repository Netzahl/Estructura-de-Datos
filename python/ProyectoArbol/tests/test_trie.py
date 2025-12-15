"""Tests para el Trie."""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.tree import Arbol


def test_buscar_exacto():
    """Test búsqueda exacta en Trie."""
    arbol = Arbol()
    nodo, _ = arbol.crear_nodo("/root", "documento", "carpeta")
    
    ids = arbol.trie.buscar_exacto("documento")
    
    assert len(ids) == 1
    assert nodo.id in ids


def test_buscar_prefijo():
    """Test búsqueda por prefijo."""
    arbol = Arbol()
    arbol.crear_nodo("/root", "documento1", "carpeta")
    arbol.crear_nodo("/root", "documento2", "carpeta")
    arbol.crear_nodo("/root", "foto", "carpeta")
    
    ids = arbol.trie.buscar_prefijo("doc")
    
    assert len(ids) == 2


def test_autocompletar():
    """Test autocompletado."""
    arbol = Arbol()
    arbol.crear_nodo("/root", "test1", "carpeta")
    arbol.crear_nodo("/root", "test2", "carpeta")
    arbol.crear_nodo("/root", "otro", "carpeta")
    
    resultados = arbol.trie.autocompletar("te", arbol)
    
    assert len(resultados) == 2
    nombres = [r['nombre'] for r in resultados]
    assert "test1" in nombres
    assert "test2" in nombres


def test_trie_despues_renombrar():
    """Test que Trie se actualiza al renombrar."""
    arbol = Arbol()
    nodo, _ = arbol.crear_nodo("/root", "viejo", "carpeta")
    
    arbol.renombrar_nodo(nodo.id, "nuevo")
    
    ids_viejo = arbol.trie.buscar_exacto("viejo")
    ids_nuevo = arbol.trie.buscar_exacto("nuevo")
    
    assert len(ids_viejo) == 0
    assert len(ids_nuevo) == 1


def test_trie_despues_eliminar():
    """Test que Trie se actualiza al eliminar."""
    arbol = Arbol()
    nodo, _ = arbol.crear_nodo("/root", "test", "carpeta")
    
    arbol.eliminar_nodo(nodo.id)
    
    ids = arbol.trie.buscar_exacto("test")
    assert len(ids) == 0


def test_trie_reconstruir_desde_json():
    """Test que Trie se reconstruye al cargar JSON."""
    import tempfile
    
    arbol1 = Arbol()
    arbol1.crear_nodo("/root", "test", "carpeta")
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        temp_file = f.name
    
    try:
        arbol1.guardar_json(temp_file)
        
        arbol2 = Arbol()
        arbol2.cargar_json(temp_file)
        
        resultados = arbol2.trie.autocompletar("te", arbol2)
        assert len(resultados) == 1
        assert resultados[0]['nombre'] == "test"
    finally:
        if os.path.exists(temp_file):
            os.remove(temp_file)