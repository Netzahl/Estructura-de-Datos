"""Interfaz de línea de comandos para el sistema de archivos."""
from src.tree import Arbol
import sys


class CLI:
    """Interfaz de comandos interactiva."""
    
    def __init__(self):
        self.arbol = Arbol()
        self.archivo_actual = None
        self.running = True
    
    def mostrar_ayuda(self):
        """Muestra la lista de comandos disponibles."""
        print("\n=== COMANDOS DISPONIBLES ===")
        print("mkdir <ruta> <nombre>       - Crear carpeta")
        print("touch <ruta> <nombre>       - Crear archivo")
        print("mv <id> <ruta_destino>      - Mover nodo")
        print("rename <id> <nuevo_nombre>  - Renombrar nodo")
        print("rm <id>                     - Eliminar nodo")
        print("ls <ruta>                   - Listar contenido")
        print("tree                        - Mostrar árbol completo")
        print("search <prefijo>            - Buscar por prefijo (autocompletado)")
        print("export [archivo]            - Exportar recorrido preorden")
        print("save <archivo>              - Guardar árbol a JSON")
        print("load <archivo>              - Cargar árbol desde JSON")
        print("trash                       - Ver papelera")
        print("restore <indice>            - Restaurar de papelera")
        print("emptytrash                  - Vaciar papelera")
        print("info <id>                   - Información de nodo")
        print("cd <ruta>                   - Cambiar directorio actual")
        print("pwd                         - Mostrar directorio actual")
        print("help                        - Mostrar esta ayuda")
        print("exit                        - Salir")
        print("=" * 40)
    
    def ejecutar_comando(self, comando):
        """Procesa y ejecuta un comando."""
        if not comando.strip():
            return
        
        partes = comando.strip().split()
        cmd = partes[0].lower()
        args = partes[1:]
        
        try:
            if cmd == "help":
                self.mostrar_ayuda()
            
            elif cmd == "mkdir":
                if len(args) < 1:
                    print("❌ Uso: mkdir <nombre> o mkdir <ruta> <nombre>")
                    return
                
                # Si solo un argumento, usar ruta actual
                if len(args) == 1:
                    ruta = self.arbol.ruta_actual
                    nombre = args[0]
                else:
                    ruta = args[0]
                    nombre = args[1]
                
                nodo, msg = self.arbol.crear_nodo(ruta, nombre, "carpeta")
                if nodo:
                    print(f"✓ Carpeta '{nombre}' creada con ID {nodo.id} en {ruta}")
                else:
                    print(f"❌ {msg}")
            
            elif cmd == "touch":
                if len(args) < 1:
                    print("❌ Uso: touch <nombre> [contenido] o touch <ruta> <nombre> [contenido]")
                    return
                
                # Si primer arg tiene /, es ruta
                if "/" in args[0] and len(args) >= 2:
                    ruta = args[0]
                    nombre = args[1]
                    contenido = " ".join(args[2:]) if len(args) > 2 else ""
                else:
                    ruta = self.arbol.ruta_actual
                    nombre = args[0]
                    contenido = " ".join(args[1:]) if len(args) > 1 else ""
                
                nodo, msg = self.arbol.crear_nodo(ruta, nombre, "archivo", contenido)
                if nodo:
                    print(f"✓ Archivo '{nombre}' creado con ID {nodo.id} en {ruta}")
                else:
                    print(f"❌ {msg}")
            
            elif cmd == "mv":
                if len(args) < 2:
                    print("❌ Uso: mv <id> <ruta_destino>")
                    return
                node_id = int(args[0])
                destino = args[1]
                exito, msg = self.arbol.mover_nodo(node_id, destino)
                if exito:
                    print(f"✓ {msg}")
                else:
                    print(f"❌ {msg}")
            
            elif cmd == "rename":
                if len(args) < 2:
                    print("❌ Uso: rename <id> <nuevo_nombre>")
                    return
                node_id = int(args[0])
                nuevo_nombre = args[1]
                exito, msg = self.arbol.renombrar_nodo(node_id, nuevo_nombre)
                if exito:
                    print(f"✓ {msg}")
                else:
                    print(f"❌ {msg}")
            
            elif cmd == "rm":
                if len(args) < 1:
                    print("❌ Uso: rm <id>")
                    return
                node_id = int(args[0])
                ids, msg = self.arbol.eliminar_nodo(node_id)
                if ids:
                    print(f"✓ {msg}")
                else:
                    print(f"❌ {msg}")
            
            elif cmd == "ls":
                if len(args) < 1:
                    ruta = self.arbol.ruta_actual
                else:
                    ruta = args[0]
                hijos, msg = self.arbol.listar_hijos(ruta)
                if hijos:
                    print(f"\n📁 Contenido de {ruta}:")
                    for node_id, nombre, tipo in hijos:
                        icono = "📁" if tipo == "carpeta" else "📄"
                        print(f"  {icono} [{node_id}] {nombre}")
                else:
                    print(f"❌ {msg}")
            
            elif cmd == "tree":
                print("\n🌳 Árbol completo:")
                self.arbol.mostrar_arbol()
            
            elif cmd == "search":
                if len(args) < 1:
                    print("❌ Uso: search <prefijo>")
                    return
                prefijo = args[0]
                resultados = self.arbol.trie.autocompletar(prefijo, self.arbol, limite=20)
                if resultados:
                    print(f"\n🔍 Resultados para '{prefijo}':")
                    for r in resultados:
                        icono = "📁" if r['tipo'] == "carpeta" else "📄"
                        print(f"  {icono} [{r['id']}] {r['nombre']} - {r['ruta']}")
                else:
                    print(f"❌ No se encontraron resultados para '{prefijo}'")
            
            elif cmd == "export":
                archivo = args[0] if args else None
                if archivo:
                    recorrido, msg = self.arbol.exportar_preorden(archivo)
                    print(f"✓ {msg}")
                else:
                    recorrido, msg = self.arbol.exportar_preorden()
                    print(f"\n📋 Recorrido preorden ({len(recorrido)} nodos):")
                    for item in recorrido:
                        icono = "📁" if item['tipo'] == "carpeta" else "📄"
                        print(f"  {icono} {item['ruta']}")
            
            elif cmd == "save":
                if len(args) < 1:
                    print("❌ Uso: save <archivo>")
                    return
                archivo = args[0]
                exito, msg = self.arbol.guardar_json(archivo)
                if exito:
                    print(f"✓ {msg}")
                    self.archivo_actual = archivo
                else:
                    print(f"❌ {msg}")
            
            elif cmd == "load":
                if len(args) < 1:
                    print("❌ Uso: load <archivo>")
                    return
                archivo = args[0]
                exito, msg = self.arbol.cargar_json(archivo)
                if exito:
                    print(f"✓ {msg}")
                    self.archivo_actual = archivo
                else:
                    print(f"❌ {msg}")
            
            elif cmd == "trash":
                items, msg = self.arbol.ver_papelera()
                if items:
                    print("\n🗑️  Papelera:")
                    for i, node_id, nombre, tipo, cant in items:
                        icono = "📁" if tipo == "carpeta" else "📄"
                        print(f"  [{i}] {icono} {nombre} (ID: {node_id}, {cant} elementos)")
                else:
                    print(f"✓ {msg}")

            elif cmd == "restore":
                if len(args) < 1:
                    print("❌ Uso: restore <indice>")
                    return
                indice = int(args[0])
                exito, msg = self.arbol.restaurar_papelera(indice)
                if exito:
                    print(f"✓ {msg}")
                else:
                    print(f"❌ {msg}")
            
            elif cmd == "emptytrash":
                exito, msg = self.arbol.vaciar_papelera()
                print(f"✓ {msg}")
            
            elif cmd == "info":
                if len(args) < 1:
                    print("❌ Uso: info <id>")
                    return
                node_id = int(args[0])
                nodo = self.arbol.obtener_nodo_por_id(node_id)
                if nodo:
                    print(f"\nℹ️  Información del nodo:")
                    print(f"  ID: {nodo.id}")
                    print(f"  Nombre: {nodo.nombre}")
                    print(f"  Tipo: {nodo.tipo}")
                    print(f"  Ruta: {nodo.obtener_ruta()}")
                    if nodo.tipo == "archivo":
                        print(f"  Contenido: {nodo.contenido[:50]}...")
                    if nodo.es_carpeta():
                        print(f"  Hijos: {len(nodo.children)}")
                else:
                    print(f"❌ Nodo con ID {node_id} no encontrado")
            
            elif cmd == "cd":
                if len(args) < 1:
                    print("❌ Uso: cd <ruta>")
                    return
                ruta = args[0]
                exito, msg = self.arbol.cambiar_directorio(ruta)
                if exito:
                    print(f"✓ {msg}")
                else:
                    print(f"❌ {msg}")
            
            elif cmd == "pwd":
                print(f"📍 {self.arbol.obtener_directorio_actual()}")
            
            elif cmd == "exit" or cmd == "quit":
                print("\n👋 ¡Hasta luego!")
                self.running = False
            
            else:
                print(f"❌ Comando desconocido: '{cmd}'. Escribe 'help' para ver comandos.")
        
        except ValueError:
            print("❌ ID debe ser un número entero")
        except Exception as e:
            print(f"❌ Error: {str(e)}")
    
    def run(self):
        """Inicia el loop principal del CLI."""
        print("\n" + "=" * 50)
        print("🌳 SISTEMA DE ARCHIVOS - ÁRBOL GENERAL")
        print("=" * 50)
        self.mostrar_ayuda()
        print("\nEscribe 'help' para ver los comandos disponibles.\n")
        
        while self.running:
            try:
                prompt = f"{self.arbol.obtener_directorio_actual()} $ "
                comando = input(prompt)
                self.ejecutar_comando(comando)
            except KeyboardInterrupt:
                print("\n\n👋 Interrumpido. Usa 'exit' para salir.")
            except EOFError:
                print("\n\n👋 ¡Hasta luego!")
                break


def main():
    """Punto de entrada principal."""
    cli = CLI()
    cli.run()


if __name__ == "__main__":
    main()