"""Módulo que implementa el árbol general de archivos/carpetas."""
from src.node import Nodo

class Arbol:
    """Árbol general que gestiona la jerarquía de nodos."""
    
    def __init__(self):
        self.root = Nodo(0, "root", "carpeta")
        self.contador_id = 1
        self.nodos = {0: self.root}
        self.papelera = []
        self.ruta_actual = "/root"
    
    def _encontrar_nodo_por_ruta(self, ruta):
        """Encuentra un nodo por su ruta."""
        if ruta == "/" or ruta == "/root":
            return self.root
        
        partes = ruta.strip("/").split("/")
        if partes[0] != "root":
            return None
        
        nodo_actual = self.root
        for parte in partes[1:]:
            encontrado = False
            for hijo in nodo_actual.children:
                if hijo.nombre == parte:
                    nodo_actual = hijo
                    encontrado = True
                    break
            if not encontrado:
                return None
        
        return nodo_actual
    
    def crear_nodo(self, ruta_padre, nombre, tipo, contenido=""):
        """Crea un nuevo nodo en la ruta especificada."""
        padre = self._encontrar_nodo_por_ruta(ruta_padre)
        
        if padre is None:
            return None, "Ruta padre no existe"
        
        if not padre.es_carpeta():
            return None, "No se puede crear un nodo dentro de un archivo"
        
        for hijo in padre.children:
            if hijo.nombre == nombre:
                return None, f"Ya existe un nodo con el nombre '{nombre}' en esta ubicación"
        
        nuevo_nodo = Nodo(self.contador_id, nombre, tipo, contenido, padre)
        self.contador_id += 1
        
        padre.agregar_hijo(nuevo_nodo)
        self.nodos[nuevo_nodo.id] = nuevo_nodo
        
        return nuevo_nodo, "Nodo creado exitosamente"
    
    def obtener_nodo_por_id(self, node_id):
        """Obtiene un nodo por su ID."""
        return self.nodos.get(node_id)
    
    def listar_hijos(self, ruta):
        """Lista todos los hijos de un nodo."""
        nodo = self._encontrar_nodo_por_ruta(ruta)
        if nodo is None:
            return None, "Ruta no existe"
        
        if not nodo.es_carpeta():
            return None, "No es una carpeta"
        
        return [(hijo.id, hijo.nombre, hijo.tipo) for hijo in nodo.children], "OK"
    
    def mostrar_arbol(self, nodo=None, nivel=0):
        """Muestra el árbol en formato visual."""
        if nodo is None:
            nodo = self.root
        
        print("  " * nivel + f"[{nodo.id}] {nodo.nombre} ({nodo.tipo})")
        for hijo in nodo.children:
            self.mostrar_arbol(hijo, nivel + 1)
    
    def mover_nodo(self, node_id, ruta_destino):
        """Mueve un nodo a una nueva ubicación."""
        nodo = self.obtener_nodo_por_id(node_id)
        if nodo is None:
            return False, "Nodo no existe"
        
        if nodo == self.root:
            return False, "No se puede mover el nodo raíz"
        
        nuevo_padre = self._encontrar_nodo_por_ruta(ruta_destino)
        if nuevo_padre is None:
            return False, "Ruta destino no existe"
        
        if not nuevo_padre.es_carpeta():
            return False, "El destino debe ser una carpeta"
        
        temp = nuevo_padre
        while temp is not None:
            if temp == nodo:
                return False, "No se puede mover un nodo a uno de sus descendientes"
            temp = temp.parent
        
        for hijo in nuevo_padre.children:
            if hijo.nombre == nodo.nombre:
                return False, f"Ya existe un nodo con el nombre '{nodo.nombre}' en el destino"
        
        padre_actual = nodo.parent
        padre_actual.remover_hijo(nodo)
        nuevo_padre.agregar_hijo(nodo)
        
        return True, "Nodo movido exitosamente"
    
    def renombrar_nodo(self, node_id, nuevo_nombre):
        """Renombra un nodo."""
        nodo = self.obtener_nodo_por_id(node_id)
        if nodo is None:
            return False, "Nodo no existe"
        
        if nodo == self.root:
            return False, "No se puede renombrar el nodo raíz"
        
        padre = nodo.parent
        for hijo in padre.children:
            if hijo != nodo and hijo.nombre == nuevo_nombre:
                return False, f"Ya existe un nodo con el nombre '{nuevo_nombre}' en esta ubicación"
        
        nodo.nombre = nuevo_nombre
        return True, "Nodo renombrado exitosamente"
    
    def eliminar_nodo(self, node_id, usar_papelera=True):
        """Elimina un nodo y todos sus descendientes."""
        nodo = self.obtener_nodo_por_id(node_id)
        if nodo is None:
            return [], "Nodo no existe"
        
        if nodo == self.root:
            return [], "No se puede eliminar el nodo raíz"
        
        ids_eliminados = []
        
        def recolectar_ids(n):
            ids_eliminados.append(n.id)
            for hijo in n.children:
                recolectar_ids(hijo)
        
        recolectar_ids(nodo)
        
        if usar_papelera:
            self.papelera.append({
                "nodo": nodo,
                "padre_original": nodo.parent,
                "ids": ids_eliminados.copy()
            })
        
        padre = nodo.parent
        padre.remover_hijo(nodo)
        
        for id_elim in ids_eliminados:
            if id_elim in self.nodos:
                del self.nodos[id_elim]
        
        return ids_eliminados, f"Eliminados {len(ids_eliminados)} nodo(s)"
    
    def ver_papelera(self):
        """Muestra los elementos en la papelera."""
        if not self.papelera:
            return [], "Papelera vacía"
        
        items = []
        for i, item in enumerate(self.papelera):
            nodo = item["nodo"]
            items.append((i, nodo.id, nodo.nombre, nodo.tipo, len(item["ids"])))
        
        return items, "OK"
    
    def vaciar_papelera(self):
        """Vacía completamente la papelera."""
        cant = len(self.papelera)
        self.papelera.clear()
        return True, f"Papelera vaciada ({cant} elementos eliminados permanentemente)"
    
    def calcular_altura(self, nodo=None):
        """Calcula la altura del árbol desde un nodo."""
        if nodo is None:
            nodo = self.root
        
        if not nodo.children:
            return 0
        
        return 1 + max(self.calcular_altura(hijo) for hijo in nodo.children)
    
    def calcular_tamano(self, nodo=None):
        """Calcula el número total de nodos en el subárbol."""
        if nodo is None:
            nodo = self.root
        
        tamano = 1
        for hijo in nodo.children:
            tamano += self.calcular_tamano(hijo)
        
        return tamano
    
    def cambiar_directorio(self, ruta):
        """Cambia el directorio actual."""
        nodo = self._encontrar_nodo_por_ruta(ruta)
        if nodo is None:
            return False, "Ruta no existe"
        
        if not nodo.es_carpeta():
            return False, "No es una carpeta"
        
        self.ruta_actual = nodo.obtener_ruta()
        return True, f"Directorio cambiado a {self.ruta_actual}"
    
    def obtener_directorio_actual(self):
        """Retorna el directorio actual."""
        return self.ruta_actual