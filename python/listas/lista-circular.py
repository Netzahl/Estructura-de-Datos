class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = None


def menu():
    print("\n********** Menú principal **********")
    print("1. Insertar al principio")
    print("2. Insertar al final")
    print("3. Insertar en posición")
    print("4. Eliminar del principio")
    print("5. Eliminar del final")
    print("6. Eliminar nodo después de la ubicación")
    print("7. Buscar un elemento")
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
        print("Saliendo...")
        exit()
    else:
        print("Opción no válida")


# 1. Insertar al inicio
def beg_insert():
    global head
    item = int(input("Ingrese valor: "))
    new_node = Node(item)

    if head is None:
        head = new_node
        new_node.next = head
    else:
        temp = head
        while temp.next != head:
            temp = temp.next

        new_node.next = head
        temp.next = new_node
        head = new_node

    print("Nodo insertado al inicio")


# 2. Insertar al final
def last_insert():
    global head
    item = int(input("Ingrese valor: "))
    new_node = Node(item)

    if head is None:
        head = new_node
        new_node.next = head
    else:
        temp = head
        while temp.next != head:
            temp = temp.next

        temp.next = new_node
        new_node.next = head

    print("Nodo insertado al final")


# 3. Insertar después de una ubicación
def select_insert():
    global head
    item = int(input("Ingrese el valor a insertar: "))
    loc = int(input("Ingrese la posición después de la cual insertar: "))

    if head is None or loc <= 0:
        print("No se puede insertar")
        return

    new_node = Node(item)
    temp = head

    for i in range(1, loc):
        temp = temp.next
        if temp == head:
            print("Ubicación fuera de rango")
            return

    new_node.next = temp.next
    temp.next = new_node

    print("Nodo insertado")


# 4. Eliminar al inicio
def begin_delete():
    global head

    if head is None:
        print("Lista vacía")
        return

    if head.next == head:
        head = None
    else:
        temp = head
        while temp.next != head:
            temp = temp.next

        head = head.next
        temp.next = head

    print("Primer nodo eliminado")


# 5. Eliminar al final
def last_delete():
    global head

    if head is None:
        print("Lista vacía")
        return

    if head.next == head:
        head = None
        print("Se eliminó el único nodo de la lista")
        return

    prev = None
    ptr = head

    while ptr.next != head:
        prev = ptr
        ptr = ptr.next

    prev.next = head

    print("Último nodo eliminado")


# 6. Eliminar después de una posición
def select_delete():
    global head

    loc = int(input("Ingrese posición después de la cual desea eliminar: "))

    if head is None or loc <= 0:
        print("Lista vacía o posición inválida")
        return

    ptr1 = head
    ptr = head.next

    for i in range(2, loc):
        ptr1 = ptr
        ptr = ptr.next

        if ptr == head:
            print("Ubicación fuera de los límites")
            return

    if ptr == head:
        print("Ubicación fuera de los límites")
        return

    ptr1.next = ptr.next
    print(f"Nodo eliminado en la posición {loc + 1}")


# 7. Buscar elemento
def search():
    global head

    if head is None:
        print("Lista vacía")
        return

    item = int(input("Ingrese el elemento a buscar: "))

    ptr = head
    i = 1
    found = False

    while True:
        if ptr.data == item:
            print(f"Elemento encontrado en la posición {i}")
            found = True

        ptr = ptr.next
        i += 1

        if ptr == head:
            break

    if not found:
        print("Elemento no encontrado")


# 8. Mostrar lista
def display():
    global head

    if head is None:
        print("Nada que imprimir")
        return

    ptr = head
    print("\nMostrando lista circular:")

    while True:
        print(ptr.data)
        ptr = ptr.next

        if ptr == head:
            break


# Programa principal
while True:
    menu()
