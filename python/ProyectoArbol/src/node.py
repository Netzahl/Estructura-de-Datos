"""Módulo que define la estructura de Nodos para el árbol de archivos."""

class Nodo:
    """Representa un nodo en el árbol (carpeta o archivo)."""
    
    def __init__(self, node_id, nombre, tipo, contenido="", parent=None):
        self.id = node_id
        self.nombre = nombre
        self.tipo = tipo
        self.contenido = contenido
        self.parent = parent
        self.children = []

    def agregar_hijo(self, nodo):
        """Agrega un nodo hijo a este nodo."""
        nodo.parent = self
        self.children.append(nodo)

    def remover_hijo(self, nodo):
        """Remueve un nodo hijo."""
        if nodo in self.children:
            self.children.remove(nodo)
            nodo.parent = None

    def es_carpeta(self):
        """Verifica si el nodo es una carpeta."""
        return self.tipo == "carpeta"

    def obtener_ruta(self):
        """Retorna la ruta completa del nodo."""
        if self.parent is None:
            return "/" + self.nombre
        return self.parent.obtener_ruta() + "/" + self.nombre

    def to_dict(self):
        """Convierte el nodo a diccionario para JSON."""
        return {
            "id": self.id,
            "nombre": self.nombre,
            "tipo": self.tipo,
            "contenido": self.contenido,
            "children": [child.to_dict() for child in self.children]
        }