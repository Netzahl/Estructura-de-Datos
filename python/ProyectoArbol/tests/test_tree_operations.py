"""Tests para operaciones avanzadas del árbol."""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.tree import Arbol


def test_mover_nodo():
    """Test mover un nodo a otra ubicación."""
    arbol = Arbol()
    arbol.crear_nodo("/root", "origen", "carpeta")
    arbol.crear_nodo("/root", "destino", "carpeta")
    nodo, _ = arbol.crear_nodo("/root/origen", "archivo.txt", "archivo")
    
    exito, msg = arbol.mover_nodo(nodo.id, "/root/destino")
    
    assert exito is True
    assert nodo.parent.nombre == "destino"
    hijos_origen, _ = arbol.listar_hijos("/root/origen")
    assert len(hijos_origen) == 0


def test_mover_nodo_a_si_mismo():
    """Test intentar mover nodo a sí mismo."""
    arbol = Arbol()
    nodo, _ = arbol.crear_nodo("/root", "carpeta", "carpeta")
    arbol.crear_nodo("/root/carpeta", "sub", "carpeta")
    
    exito, msg = arbol.mover_nodo(nodo.id, "/root/carpeta/sub")
    
    assert exito is False
    assert "descendiente" in msg.lower()


def test_renombrar_nodo():
    """Test renombrar un nodo."""
    arbol = Arbol()
    nodo, _ = arbol.crear_nodo("/root", "viejo", "carpeta")
    
    exito, msg = arbol.renombrar_nodo(nodo.id, "nuevo")
    
    assert exito is True
    assert nodo.nombre == "nuevo"


def test_renombrar_nodo_conflicto():
    """Test renombrar con nombre existente."""
    arbol = Arbol()
    arbol.crear_nodo("/root", "nombre1", "carpeta")
    nodo2, _ = arbol.crear_nodo("/root", "nombre2", "carpeta")
    
    exito, msg = arbol.renombrar_nodo(nodo2.id, "nombre1")
    
    assert exito is False
    assert "existe" in msg.lower()


def test_eliminar_nodo():
    """Test eliminar un nodo."""
    arbol = Arbol()
    nodo, _ = arbol.crear_nodo("/root", "test", "carpeta")
    
    ids, msg = arbol.eliminar_nodo(nodo.id)
    
    assert len(ids) == 1
    assert nodo.id in ids
    assert arbol.obtener_nodo_por_id(nodo.id) is None


def test_eliminar_nodo_con_hijos():
    """Test eliminar nodo con descendientes."""
    arbol = Arbol()
    padre, _ = arbol.crear_nodo("/root", "padre", "carpeta")
    arbol.crear_nodo("/root/padre", "hijo1", "carpeta")
    arbol.crear_nodo("/root/padre", "hijo2", "archivo")
    
    ids, msg = arbol.eliminar_nodo(padre.id)
    
    assert len(ids) == 3  # padre + 2 hijos


def test_papelera():
    """Test funcionalidad de papelera."""
    arbol = Arbol()
    nodo, _ = arbol.crear_nodo("/root", "test", "carpeta")
    
    arbol.eliminar_nodo(nodo.id, usar_papelera=True)
    
    items, msg = arbol.ver_papelera()
    assert len(items) == 1
    assert items[0][2] == "test"


def test_restaurar_papelera():
    """Test restaurar desde papelera."""
    arbol = Arbol()
    nodo, _ = arbol.crear_nodo("/root", "test", "carpeta")
    node_id = nodo.id
    
    arbol.eliminar_nodo(node_id, usar_papelera=True)
    exito, msg = arbol.restaurar_papelera(0)
    
    assert exito is True
    assert arbol.obtener_nodo_por_id(node_id) is not None


def test_vaciar_papelera():
    """Test vaciar papelera."""
    arbol = Arbol()
    nodo, _ = arbol.crear_nodo("/root", "test", "carpeta")
    arbol.eliminar_nodo(nodo.id, usar_papelera=True)
    
    exito, msg = arbol.vaciar_papelera()
    
    assert exito is True
    items, _ = arbol.ver_papelera()
    assert len(items) == 0