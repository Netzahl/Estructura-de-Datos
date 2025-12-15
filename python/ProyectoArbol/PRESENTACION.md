# Presentación: Sistema de Archivos con Árbol General

## 📌 Resumen Ejecutivo

Sistema de gestión de archivos jerárquico implementado con árboles generales, búsqueda eficiente mediante Trie, y persistencia JSON.

## 🎯 Objetivos Cumplidos

- ✅ Implementación completa de árbol general
- ✅ Todas las operaciones CRUD funcionales
- ✅ Trie para búsqueda O(m) por prefijo
- ✅ Persistencia JSON completa
- ✅ CLI interactiva con 16 comandos
- ✅ Sistema de papelera con restauración
- ✅ 30 tests unitarios (100% pasando)

## 🏗️ Arquitectura

### Estructuras de Datos Principales

1. **Árbol General**
   - Nodos con referencias padre-hijos
   - Operaciones O(1) inserción, O(n) búsqueda

2. **Hash Map (dict)**
   - Búsqueda por ID en O(1)
   - Sincronizado con el árbol

3. **Trie**
   - Búsqueda por prefijo: O(m)
   - Autocompletado eficiente

## 💡 Funcionalidades Destacadas

### 1. Operaciones Básicas
- Crear carpetas y archivos
- Mover nodos manteniendo jerarquía
- Renombrar con validación de duplicados
- Eliminar recursivamente

### 2. Búsqueda Avanzada
- Búsqueda exacta por nombre
- Búsqueda por prefijo
- Autocompletado con sugerencias
- Case-insensitive

### 3. Persistencia
- Serialización completa a JSON
- Deserialización reconstruye árbol + índices
- Formato legible y portable

### 4. CLI Profesional
- 16 comandos estilo Unix
- Navegación con cd/pwd
- Feedback visual con iconos
- Manejo robusto de errores

## 📊 Complejidades

| Operación | Complejidad | Estructura |
|-----------|-------------|------------|
| Buscar por ID | O(1) | Hash Map |
| Buscar por prefijo | O(m) | Trie |
| Crear nodo | O(1) | Árbol |
| Eliminar subárbol | O(n) | Árbol |
| Mover nodo | O(h) | Árbol |

## 🧪 Testing

- 30 tests unitarios con pytest
- Cobertura de todos los módulos
- Tests de integración
- Validación de casos límite

## 🚀 Demo en Vivo

Ejecutar: `python demo.py`

Muestra:
1. Creación de estructura
2. Búsqueda con Trie
3. Operaciones CRUD
4. Papelera y restauración
5. Persistencia JSON
6. Export preorden

## 📈 Mejoras Futuras (Opcional)

- Sistema de permisos por nodo
- Búsqueda por contenido
- Historial de cambios (git-like)
- Compresión de archivos grandes
- Interfaz gráfica (GUI)

## 🎓 Conclusiones

Proyecto cumple y excede los requisitos:
- Implementación robusta de árbol general
- Estructuras auxiliares eficientes (Trie, Hash Map)
- Código bien documentado y probado
- CLI profesional y usable
- Extensible para mejoras futuras

---

**Integrantes:**
- López Návarez Mario David
- Osuna De La Cruz Victor Leonardo

**Fecha:** 15 de Diciembre, 2025