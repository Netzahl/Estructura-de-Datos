"""Módulo que implementa un Trie para búsqueda y autocompletado."""

class NodoTrie:
    """Nodo del Trie."""
    
    def __init__(self):
        self.hijos = {}  # Diccionario: caracter -> NodoTrie
        self.es_fin_palabra = False
        self.nodos_id = []  # IDs de nodos que tienen este prefijo/nombre
    

class Trie:
    """
    Trie para búsqueda eficiente y autocompletado de nombres de nodos.
    Permite búsqueda por prefijo en O(m) donde m es longitud del prefijo.
    """
    
    def __init__(self):
        self.raiz = NodoTrie()
    
    def insertar(self, palabra, node_id):
        """
        Inserta una palabra en el Trie asociándola con un ID de nodo.
        palabra: nombre del nodo
        node_id: ID del nodo en el árbol
        """
        nodo_actual = self.raiz
        palabra = palabra.lower()  # Case insensitive
        
        for caracter in palabra:
            if caracter not in nodo_actual.hijos:
                nodo_actual.hijos[caracter] = NodoTrie()
            nodo_actual = nodo_actual.hijos[caracter]
            # Agregar el ID en cada nodo del camino (para prefijos)
            if node_id not in nodo_actual.nodos_id:
                nodo_actual.nodos_id.append(node_id)
        
        nodo_actual.es_fin_palabra = True
    
    def buscar_exacto(self, palabra):
        """
        Busca una palabra exacta en el Trie.
        Retorna lista de IDs de nodos con ese nombre exacto.
        """
        nodo_actual = self.raiz
        palabra = palabra.lower()
        
        for caracter in palabra:
            if caracter not in nodo_actual.hijos:
                return []
            nodo_actual = nodo_actual.hijos[caracter]
        
        if nodo_actual.es_fin_palabra:
            return nodo_actual.nodos_id
        return []
    
    def buscar_prefijo(self, prefijo):
        """
        Busca todos los nodos cuyos nombres empiezan con el prefijo.
        Retorna lista de IDs de nodos que coinciden.
        """
        nodo_actual = self.raiz
        prefijo = prefijo.lower()
        
        # Navegar hasta el final del prefijo
        for caracter in prefijo:
            if caracter not in nodo_actual.hijos:
                return []
            nodo_actual = nodo_actual.hijos[caracter]
        
        # Retornar todos los IDs asociados a este prefijo
        return nodo_actual.nodos_id
    
    def autocompletar(self, prefijo, arbol, limite=10):
        """
        Genera sugerencias de autocompletado para un prefijo.
        Retorna lista de tuplas: (id, nombre_completo, tipo, ruta)
        """
        ids = self.buscar_prefijo(prefijo)
        resultados = []
        
        for node_id in ids[:limite]:
            nodo = arbol.obtener_nodo_por_id(node_id)
            if nodo:
                resultados.append({
                    "id": nodo.id,
                    "nombre": nodo.nombre,
                    "tipo": nodo.tipo,
                    "ruta": nodo.obtener_ruta()
                })
        
        return resultados
    
    def eliminar(self, palabra, node_id):
        """
        Elimina un ID de nodo asociado a una palabra.
        Útil cuando se elimina o renombra un nodo.
        """
        def _eliminar_recursivo(nodo, palabra, profundidad):
            if profundidad == len(palabra):
                if node_id in nodo.nodos_id:
                    nodo.nodos_id.remove(node_id)
                return len(nodo.nodos_id) == 0 and len(nodo.hijos) == 0
            
            caracter = palabra[profundidad]
            if caracter not in nodo.hijos:
                return False
            
            hijo = nodo.hijos[caracter]
            if node_id in hijo.nodos_id:
                hijo.nodos_id.remove(node_id)
            
            debe_eliminar = _eliminar_recursivo(hijo, palabra, profundidad + 1)
            
            if debe_eliminar:
                del nodo.hijos[caracter]
                return len(nodo.hijos) == 0 and len(nodo.nodos_id) == 0
            
            return False
        
        palabra = palabra.lower()
        _eliminar_recursivo(self.raiz, palabra, 0)
    
    def reconstruir_desde_arbol(self, arbol):
        """
        Reconstruye el Trie completo desde el árbol.
        Útil después de cargar desde JSON.
        """
        self.raiz = NodoTrie()
        
        def recorrer(nodo):
            self.insertar(nodo.nombre, nodo.id)
            for hijo in nodo.children:
                recorrer(hijo)
        
        recorrer(arbol.root)