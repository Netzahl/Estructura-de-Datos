"""Módulo que implementa el árbol general de archivos/carpetas."""
from src.node import Nodo
from src.trie import Trie

class Arbol:
    """Árbol general que gestiona la jerarquía de nodos."""
    
    def __init__(self):
        self.root = Nodo(0, "root", "carpeta")
        self.contador_id = 1
        self.nodos = {0: self.root}
        self.papelera = []
        self.ruta_actual = "/root"
        self.trie = Trie()  
        self.trie.insertar("root", 0) 
    
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

        self.trie.insertar(nombre, nuevo_nodo.id)  
        
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
            
        nombre_viejo = nodo.nombre
        self.trie.eliminar(nombre_viejo, node_id)  
        self.trie.insertar(nuevo_nombre, node_id)  
        
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
            self.trie.eliminar(n.nombre, n.id)
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
    
    def restaurar_papelera(self, indice):
        """
        Restaura un elemento de la papelera a su ubicación original.
        Maneja conflictos de nombres si es necesario.
        """
        if indice >= len(self.papelera) or indice < 0:
            return False, "Índice inválido"
        
        item = self.papelera[indice]
        nodo = item["nodo"]
        padre_original = item["padre_original"]
        
        # Verificar que el padre original aún existe en el árbol
        if padre_original.id not in self.nodos:
            return False, "La ubicación original ya no existe"
        
        # Verificar conflicto de nombres
        for hijo in padre_original.children:
            if hijo.nombre == nodo.nombre:
                return False, f"Ya existe un nodo con el nombre '{nodo.nombre}' en la ubicación original"
        
        # Restaurar el nodo al padre
        padre_original.agregar_hijo(nodo)
        
        # Re-agregar todos los nodos al hash map y al Trie (recursivamente)
        def reagregar_recursivo(n):
            self.nodos[n.id] = n
            self.trie.insertar(n.nombre, n.id)
            for hijo in n.children:
                reagregar_recursivo(hijo)
        
        reagregar_recursivo(nodo)
        
        # Remover de la papelera
        self.papelera.pop(indice)
        
        return True, f"Nodo '{nodo.nombre}' restaurado exitosamente"
    
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
    
    def guardar_json(self, archivo):
        """Guarda el árbol completo en un archivo JSON, incluyendo la papelera."""
        import json
        
        try:
            # Serializar la papelera
            papelera_serializada = []
            for item in self.papelera:
                papelera_serializada.append({
                    "nodo": item["nodo"].to_dict(),
                    "padre_original_id": item["padre_original"].id,
                    "ids": item["ids"]
                })
            
            data = {
                "version": "1.0",
                "contador_id": self.contador_id,
                "root": self.root.to_dict(),
                "papelera": papelera_serializada
            }
            
            with open(archivo, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            
            return True, f"Árbol guardado en {archivo}"
        except Exception as e:
            return False, f"Error al guardar: {str(e)}"

    def cargar_json(self, archivo):
        """Carga el árbol desde un archivo JSON, incluyendo la papelera."""
        import json
        
        try:
            with open(archivo, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Resetear el árbol
            self.nodos.clear()
            self.papelera.clear()
            
            # Restaurar contador
            self.contador_id = data.get("contador_id", 1)
            
            # Reconstruir el árbol recursivamente
            def reconstruir_nodo(nodo_dict, padre=None):
                """Reconstruye un nodo y sus hijos desde un diccionario."""
                nodo = Nodo(
                    nodo_dict["id"],
                    nodo_dict["nombre"],
                    nodo_dict["tipo"],
                    nodo_dict.get("contenido", ""),
                    padre
                )
                
                # Agregar al hash map
                self.nodos[nodo.id] = nodo
                
                # Reconstruir hijos recursivamente
                for hijo_dict in nodo_dict.get("children", []):
                    hijo = reconstruir_nodo(hijo_dict, nodo)
                    nodo.children.append(hijo)
                
                return nodo
            
            # Reconstruir desde la raíz
            self.root = reconstruir_nodo(data["root"])
            self.ruta_actual = "/root"
            
            # Reconstruir Trie
            self.trie.reconstruir_desde_arbol(self)
            
            # Reconstruir papelera
            papelera_data = data.get("papelera", [])
            for item_data in papelera_data:
                # Reconstruir el nodo eliminado
                nodo_eliminado = reconstruir_nodo(item_data["nodo"], padre=None)
                
                # Buscar el padre original
                padre_original_id = item_data["padre_original_id"]
                padre_original = self.nodos.get(padre_original_id)
                
                if padre_original:
                    self.papelera.append({
                        "nodo": nodo_eliminado,
                        "padre_original": padre_original,
                        "ids": item_data["ids"]
                    })
            
            return True, f"Árbol cargado desde {archivo}"
        
        except FileNotFoundError:
            return False, f"Archivo {archivo} no encontrado"
        except json.JSONDecodeError:
            return False, "Archivo JSON corrupto o mal formateado"
        except Exception as e:
            return False, f"Error al cargar: {str(e)}"
        
    def exportar_preorden(self, archivo=None):
        """
        Exporta el recorrido en preorden del árbol.
        Si archivo es None, retorna lista. Si no, guarda en archivo.
        """
        resultado = []
        
        def recorrer_preorden(nodo):
            """Recorrido preorden: Raíz -> Hijos (izq a der)."""
            # Visitar nodo actual
            resultado.append({
                "id": nodo.id,
                "nombre": nodo.nombre,
                "tipo": nodo.tipo,
                "ruta": nodo.obtener_ruta(),
                "contenido": nodo.contenido if nodo.tipo == "archivo" else ""
            })
            
            # Visitar hijos
            for hijo in nodo.children:
                recorrer_preorden(hijo)
        
        recorrer_preorden(self.root)
        
        # Si se especifica archivo, guardar
        if archivo:
            try:
                import json
                with open(archivo, 'w', encoding='utf-8') as f:
                    json.dump(resultado, f, indent=2, ensure_ascii=False)
                return resultado, f"Recorrido exportado a {archivo}"
            except Exception as e:
                return None, f"Error al exportar: {str(e)}"
        
        return resultado, "Recorrido generado"