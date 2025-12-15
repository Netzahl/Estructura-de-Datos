"""Tests para operaciones básicas del árbol."""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.tree import Arbol


def test_crear_arbol():
    """Test crear árbol vacío."""
    arbol = Arbol()
    assert arbol.root is not None
    assert arbol.root.nombre == "root"
    assert arbol.contador_id == 1
    assert len(arbol.nodos) == 1


def test_crear_nodo_carpeta():
    """Test crear una carpeta."""
    arbol = Arbol()
    nodo, msg = arbol.crear_nodo("/root", "test", "carpeta")
    
    assert nodo is not None
    assert nodo.nombre == "test"
    assert nodo.tipo == "carpeta"
    assert nodo.id == 1
    assert len(arbol.nodos) == 2


def test_crear_nodo_archivo():
    """Test crear un archivo con contenido."""
    arbol = Arbol()
    nodo, msg = arbol.crear_nodo("/root", "file.txt", "archivo", "contenido")
    
    assert nodo is not None
    assert nodo.contenido == "contenido"
    assert nodo.tipo == "archivo"


def test_crear_nodo_en_ruta_invalida():
    """Test crear nodo en ruta que no existe."""
    arbol = Arbol()
    nodo, msg = arbol.crear_nodo("/root/noexiste", "test", "carpeta")
    
    assert nodo is None
    assert "no existe" in msg.lower()


def test_crear_nodo_nombre_duplicado():
    """Test crear nodo con nombre duplicado."""
    arbol = Arbol()
    arbol.crear_nodo("/root", "test", "carpeta")
    nodo2, msg = arbol.crear_nodo("/root", "test", "carpeta")
    
    assert nodo2 is None
    assert "existe" in msg.lower()


def test_obtener_nodo_por_id():
    """Test buscar nodo por ID."""
    arbol = Arbol()
    nodo, _ = arbol.crear_nodo("/root", "test", "carpeta")
    
    encontrado = arbol.obtener_nodo_por_id(nodo.id)
    assert encontrado == nodo
    
    no_existe = arbol.obtener_nodo_por_id(999)
    assert no_existe is None


def test_listar_hijos():
    """Test listar hijos de un nodo."""
    arbol = Arbol()
    arbol.crear_nodo("/root", "carpeta1", "carpeta")
    arbol.crear_nodo("/root", "carpeta2", "carpeta")
    arbol.crear_nodo("/root", "file.txt", "archivo")
    
    hijos, msg = arbol.listar_hijos("/root")
    
    assert hijos is not None
    assert len(hijos) == 3
    nombres = [h[1] for h in hijos]
    assert "carpeta1" in nombres
    assert "carpeta2" in nombres
    assert "file.txt" in nombres