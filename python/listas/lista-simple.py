class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = None


# ========== INSERTAR AL INICIO ==========
def beg_insert():
    global head

    item = int(input("\nIngrese valor: "))
    new_node = Node(item)
    new_node.next = head
    head = new_node

    print("Nodo insertado al inicio")


# ========== INSERTAR AL FINAL ==========
def last_insert():
    global head

    item = int(input("\nIngrese valor: "))
    new_node = Node(item)

    if head is None:
        head = new_node
        print("Nodo insertado al final")
        return

    temp = head
    while temp.next is not None:
        temp = temp.next

    temp.next = new_node
    print("Nodo insertado al final")


# ========== INSERTAR EN POSICIÓN ==========
def select_insert():
    global head

    item = int(input("\nIngrese valor: "))
    loc = int(input("Ingrese ubicación (después de qué posición): "))

    if loc <= 0:
        print("Ubicación no válida")
        return

    if head is None:
        print("Lista vacía, no se puede insertar")
        return

    new_node = Node(item)
    temp = head

    for i in range(1, loc):
        temp = temp.next
        if temp is None:
            print("Ubicación no encontrada, no se puede insertar")
            return

    new_node.next = temp.next
    temp.next = new_node

    print("Nodo insertado correctamente")


# ========== ELIMINAR AL INICIO ==========
def begin_delete():
    global head

    if head is None:
        print("La lista está vacía")
        return

    head = head.next
    print("Primer nodo eliminado")


# ========== ELIMINAR AL FINAL ==========
def last_delete():
    global head

    if head is None:
        print("La lista está vacía")
        return

    if head.next is None:
        head = None
        print("Se eliminó el único nodo")
        return

    temp = head
    prev = None

    while temp.next is not None:
        prev = temp
        temp = temp.next

    prev.next = None
    print("Último nodo eliminado")


# ========== ELIMINAR EN POSICIÓN ==========
def select_delete():
    global head

    loc = int(input("\nIngrese ubicación (después de qué posición): "))

    if head is None:
        print("Lista vacía, no se puede eliminar")
        return

    if loc <= 0:
        print("Ubicación no válida")
        return

    temp = head
    prev = None

    for i in range(0, loc):
        prev = temp
        temp = temp.next

        if temp is None:
            print("Ubicación no encontrada, no se puede eliminar")
            return

    prev.next = temp.next
    print(f"Nodo eliminado en la posición {loc + 1}")


# ========== BUSCAR ==========
def search():
    global head

    if head is None:
        print("Lista vacía")
        return

    item = int(input("\nIngrese el elemento a buscar: "))
    temp = head
    pos = 1
    found = False

    while temp is not None:
        if temp.data == item:
            print(f"Elemento encontrado en la posición {pos}")
            found = True

        temp = temp.next
        pos += 1

    if not found:
        print("Elemento no encontrado")


# ========== MOSTRAR ==========
def display():
    global head

    if head is None:
        print("Nada que mostrar")
        return

    temp = head
    print("\nImprimiendo valores:\n")

    while temp is not None:
        print(temp.data)
        temp = temp.next


# ========== MENÚ ==========
def menu():
    while True:
        print("\n********** Menú principal **********")
        print("1. Insertar al principio")
        print("2. Insertar al final")
        print("3. Insertar en posición")
        print("4. Eliminar del principio")
        print("5. Eliminar del final")
        print("6. Eliminar después de posición")
        print("7. Buscar")
        print("8. Mostrar")
        print("9. Salir")

        choice = int(input("\nIngrese su opción: "))

        if choice == 1:
            beg_insert()
        elif choice == 2:
            last_insert()
        elif choice == 3:
            select_insert()
        elif choice == 4:
            begin_delete()
        elif choice == 5:
            last_delete()
        elif choice == 6:
            select_delete()
        elif choice == 7:
            search()
        elif choice == 8:
            display()
        elif choice == 9:
            print("\nSaliendo...")
            break
        else:
            print("\nOpción no válida...")


menu()
