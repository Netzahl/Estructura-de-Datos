# Gestor de Árbol Binario de Búsqueda

## Descripción
Implementación de un BST (Binary Search Tree) con interfaz de consola para insertar, buscar, eliminar y visualizar datos.

## Compilación
```bash
g++ -o gestor main.cpp bst.cpp
```

## Ejecución
```bash
./gestor
```

## Comandos disponibles
- `insert <num>` - Insertar número
- `search <num>` - Buscar número
- `delete <num>` - Eliminar número
- `inorder` - Mostrar recorrido inorden
- `preorder` - Mostrar recorrido preorden
- `postorder` - Mostrar recorrido postorden
- `height` - Mostrar altura del árbol
- `size` - Mostrar cantidad de nodos
- `export <archivo>` - Exportar inorden a archivo
- `import <archivo>` - Importar números desde archivo
- `help` - Mostrar menú de comandos
- `exit` - Salir

## Complejidad temporal
- Inserción: O(h) donde h = altura
- Búsqueda: O(h)
- Eliminación: O(h)
- Recorridos: O(n) donde n = número de nodos

**Nota:** En el peor caso (árbol degenerado), h = n, resultando en O(n).
En promedio con valores aleatorios, h = log(n), resultando en O(log n).

## Autor
Mario David López Návarez
08/12/2025