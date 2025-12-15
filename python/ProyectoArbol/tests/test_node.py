"""Tests para la clase Nodo."""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.node import Nodo


def test_crear_nodo():
    """Test crear un nodo básico."""
    nodo = Nodo(1, "test", "carpeta")
    assert nodo.id == 1
    assert nodo.nombre == "test"
    assert nodo.tipo == "carpeta"
    assert nodo.contenido == ""
    assert nodo.parent is None
    assert len(nodo.children) == 0


def test_nodo_es_carpeta():
    """Test verificar tipo de nodo."""
    carpeta = Nodo(1, "carpeta", "carpeta")
    archivo = Nodo(2, "archivo.txt", "archivo")
    
    assert carpeta.es_carpeta() is True
    assert archivo.es_carpeta() is False


def test_agregar_hijo():
    """Test agregar hijo a un nodo."""
    padre = Nodo(1, "padre", "carpeta")
    hijo = Nodo(2, "hijo", "archivo")
    
    padre.agregar_hijo(hijo)
    
    assert len(padre.children) == 1
    assert hijo.parent == padre
    assert padre.children[0] == hijo


def test_remover_hijo():
    """Test remover hijo de un nodo."""
    padre = Nodo(1, "padre", "carpeta")
    hijo = Nodo(2, "hijo", "archivo")
    
    padre.agregar_hijo(hijo)
    padre.remover_hijo(hijo)
    
    assert len(padre.children) == 0
    assert hijo.parent is None


def test_obtener_ruta():
    """Test obtener ruta completa de un nodo."""
    root = Nodo(0, "root", "carpeta")
    carpeta1 = Nodo(1, "docs", "carpeta")
    archivo = Nodo(2, "file.txt", "archivo")
    
    root.agregar_hijo(carpeta1)
    carpeta1.agregar_hijo(archivo)
    
    assert root.obtener_ruta() == "/root"
    assert carpeta1.obtener_ruta() == "/root/docs"
    assert archivo.obtener_ruta() == "/root/docs/file.txt"


def test_to_dict():
    """Test serialización a diccionario."""
    nodo = Nodo(1, "test", "archivo", "contenido")
    hijo = Nodo(2, "hijo", "carpeta")
    nodo.agregar_hijo(hijo)
    
    data = nodo.to_dict()
    
    assert data["id"] == 1
    assert data["nombre"] == "test"
    assert data["tipo"] == "archivo"
    assert data["contenido"] == "contenido"
    assert len(data["children"]) == 1
    assert data["children"][0]["id"] == 2