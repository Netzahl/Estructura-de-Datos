"""Tests para persistencia JSON."""
import sys
import os
import tempfile
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.tree import Arbol


def test_guardar_cargar_json():
    """Test guardar y cargar árbol desde JSON."""
    arbol1 = Arbol()
    arbol1.crear_nodo("/root", "test", "carpeta")
    arbol1.crear_nodo("/root/test", "file.txt", "archivo", "contenido")
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        temp_file = f.name
    
    try:
        arbol1.guardar_json(temp_file)
        
        arbol2 = Arbol()
        exito, msg = arbol2.cargar_json(temp_file)
        
        assert exito is True
        assert len(arbol2.nodos) == len(arbol1.nodos)
        assert arbol2.contador_id == arbol1.contador_id
        
        nodo = arbol2._encontrar_nodo_por_ruta("/root/test/file.txt")
        assert nodo is not None
        assert nodo.contenido == "contenido"
    finally:
        if os.path.exists(temp_file):
            os.remove(temp_file)


def test_exportar_preorden():
    """Test exportar recorrido en preorden."""
    arbol = Arbol()
    arbol.crear_nodo("/root", "a", "carpeta")
    arbol.crear_nodo("/root/a", "b", "carpeta")
    arbol.crear_nodo("/root", "c", "carpeta")
    
    recorrido, msg = arbol.exportar_preorden()
    
    assert len(recorrido) == 4  # root + a + b + c
    nombres = [item['nombre'] for item in recorrido]
    # Preorden: root -> a -> b -> c
    assert nombres == ['root', 'a', 'b', 'c']