# Sistema de Archivos con Árbol General

Proyecto de Estructuras de Datos - Implementación de un sistema de archivos jerárquico usando árboles generales, con búsqueda eficiente mediante Trie y persistencia en JSON.

## 📋 Características

- **Árbol General**: Estructura jerárquica de carpetas y archivos
- **Operaciones CRUD**: Crear, mover, renombrar y eliminar nodos
- **Búsqueda Eficiente**: Trie para autocompletado y búsqueda por prefijo O(m)
- **Persistencia**: Guardar y cargar el árbol completo en JSON
- **Papelera**: Sistema de eliminación con recuperación
- **CLI Interactiva**: Interfaz de comandos intuitiva tipo Unix
- **Export**: Recorrido en preorden exportable

## 🚀 Instalación

### Prerrequisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Configuración

1. Clonar el repositorio:
```bash
git clone https://github.com/Netzahl/Estructura-de-Datos/tree/main/python/ProyectoArbol
cd ProyectoArbol
```

2. Crear entorno virtual (recomendado):
```bash
python -m venv venv

# Windows (Git Bash)
source venv/Scripts/activate

# Windows (PowerShell)
venv\Scripts\Activate.ps1

# Linux/Mac
source venv/bin/activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## 💻 Uso

### Iniciar la aplicación
```bash
python main.py
```

### Comandos Disponibles

#### Gestión de Archivos y Carpetas

- `mkdir <nombre>` - Crear carpeta en directorio actual
- `mkdir <ruta> <nombre>` - Crear carpeta en ruta específica
- `touch <nombre> [contenido]` - Crear archivo en directorio actual
- `touch <ruta> <nombre> [contenido]` - Crear archivo en ruta específica

#### Navegación

- `cd <ruta>` - Cambiar directorio actual
- `pwd` - Mostrar directorio actual
- `ls` - Listar contenido del directorio actual
- `ls <ruta>` - Listar contenido de una ruta
- `tree` - Mostrar árbol completo

#### Operaciones sobre Nodos

- `mv <id> <ruta_destino>` - Mover nodo
- `rename <id> <nuevo_nombre>` - Renombrar nodo
- `rm <id>` - Eliminar nodo (va a papelera)
- `info <id>` - Mostrar información detallada de un nodo

#### Búsqueda

- `search <prefijo>` - Buscar nodos por prefijo (autocompletado)

#### Papelera

- `trash` - Ver contenido de la papelera
- `restore <indice>` - Restaurar nodo desde papelera
- `emptytrash` - Vaciar papelera permanentemente

#### Persistencia y Export

- `save <archivo>` - Guardar árbol en JSON
- `load <archivo>` - Cargar árbol desde JSON
- `export` - Mostrar recorrido preorden
- `export <archivo>` - Exportar recorrido a JSON

#### Otros

- `help` - Mostrar ayuda
- `exit` - Salir de la aplicación

## 📁 Estructura del Proyecto
```
ProyectoArbol/
├── src/
│   ├── __init__.py
│   ├── node.py          # Clase Nodo
│   ├── tree.py          # Clase Árbol con operaciones
│   ├── trie.py          # Clase Trie para búsqueda
│   └── cli.py           # Interfaz de línea de comandos
├── tests/
│   ├── __init__.py
│   ├── test_node.py
│   ├── test_tree_basic.py
│   ├── test_tree_operations.py
│   ├── test_persistence.py
│   └── test_trie.py
├── data/                # Archivos JSON (generados)
├── main.py              # Punto de entrada
├── requirements.txt     # Dependencias
└── README.md
```

## 🧪 Ejecutar Tests
```bash
# Todos los tests
pytest tests/ -v

# Tests específicos
pytest tests/test_tree_basic.py -v

# Con cobertura
pytest tests/ --cov=src
```

## 🎬 Demo Automatizada

Para ver una demostración completa de todas las funcionalidades:
```bash
python demo.py
```

La demo muestra:
- Creación de estructura jerárquica
- Búsqueda con Trie (exacta, prefijo, autocompletado)
- Operaciones CRUD completas
- Sistema de papelera y restauración
- Persistencia JSON (guardar/cargar)
- Export de recorrido preorden
- Cálculos sobre el árbol

## 📖 Ejemplos de Uso

### Ejemplo 1: Crear Estructura Básica
```bash
$ python main.py
/root $ mkdir proyectos
✓ Carpeta 'proyectos' creada con ID 1 en /root

/root $ cd /root/proyectos
✓ Directorio cambiado a /root/proyectos

/root/proyectos $ touch README.md # Proyecto de ejemplo
✓ Archivo 'README.md' creado con ID 2 en /root/proyectos

/root/proyectos $ mkdir src
✓ Carpeta 'src' creada con ID 3 en /root/proyectos

/root/proyectos $ tree
🌳 Árbol completo:
[0] root (carpeta)
  [1] proyectos (carpeta)
    [2] README.md (archivo)
    [3] src (carpeta)
```

### Ejemplo 2: Búsqueda y Autocompletado
```bash
/root $ mkdir documentos
/root $ mkdir descargas
/root $ mkdir desktop

/root $ search do
🔍 Resultados para 'do':
  📁 [1] documentos - /root/documentos

/root $ search de
🔍 Resultados para 'de':
  📁 [2] descargas - /root/descargas
  📁 [3] desktop - /root/desktop
```

### Ejemplo 3: Persistencia
```bash
/root $ save data/mi_sistema.json
✓ Árbol guardado en data/mi_sistema.json

# En otra sesión...
/root $ load data/mi_sistema.json
✓ Árbol cargado desde data/mi_sistema.json

/root $ tree
# Estructura restaurada completa
```

### Ejemplo 4: Papelera y Recuperación
```bash
/root $ mkdir temporal
✓ Carpeta 'temporal' creada con ID 1

/root $ rm 1
✓ Eliminados 1 nodo(s)

/root $ trash
🗑️  Papelera:
  [0] 📁 temporal (ID: 1, 1 elementos)

/root $ restore 0
✓ Nodo 'temporal' restaurado exitosamente

/root $ tree
[0] root (carpeta)
  [1] temporal (carpeta)
```

## 🏗️ Arquitectura Técnica

### Estructuras de Datos

1. **Árbol General**
   - Cada nodo tiene referencia a padre y lista de hijos
   - Operaciones: O(1) para crear, O(n) para buscar por ruta

2. **Hash Map (dict)**
   - Mapeo `id → nodo` para búsqueda O(1) por ID
   - Mantiene sincronización con el árbol

3. **Trie**
   - Búsqueda por prefijo: O(m) donde m = longitud del prefijo
   - Autocompletado eficiente
   - Se actualiza automáticamente con cambios en el árbol

### Persistencia

- Serialización recursiva a JSON usando `to_dict()`
- Deserialización reconstruye árbol, hash map y Trie
- Formato JSON legible y portable

### Recorridos

- **Preorden**: Raíz → Hijos (implementado para export)
- Recursivo y eficiente

## 👥 Autores

- López Návarez Mario David
- Osuna De La Cruz Victor Leonardo

## 📄 Licencia

Este proyecto es parte del curso de Estructuras de Datos.
