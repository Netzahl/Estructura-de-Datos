class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.ant = None


head = None
tail = None


def beg_insert():
    global head, tail

    item = int(input("\nIngrese valor: "))
    new_node = Node(item)

    new_node.next = head
    new_node.ant = None

    if head is not None:
        head.ant = new_node
    else:
        tail = new_node

    head = new_node
    print("Nodo insertado al inicio")


def last_insert():
    global head, tail

    item = int(input("\nIngrese valor: "))
    new_node = Node(item)

    if head is None:
        head = new_node
        tail = new_node
    else:
        tail.next = new_node
        new_node.ant = tail
        tail = new_node

    print("Nodo insertado al final")


def select_insert():
    global head, tail

    item = int(input("\nIngrese el valor: "))
    loc = int(input("Introduce la ubicación después de la cual deseas ingresar: "))

    if loc <= 0:
        print("Ubicación no válida")
        return

    if head is None:
        print("No se puede insertar")
        return

    temp = head
    for i in range(1, loc):
        if temp.next is None:
            print("No se puede insertar")
            return
        temp = temp.next

    new_node = Node(item)

    new_node.next = temp.next
    new_node.ant = temp

    if temp.next is not None:
        temp.next.ant = new_node
    else:
        tail = new_node

    temp.next = new_node
    print("Nodo insertado")


def begin_delete():
    global head, tail

    if head is None:
        print("Lista vacía")
    elif head.next is None:
        head = None
        tail = None
        print("Único nodo eliminado")
    else:
        head = head.next
        head.ant = None
        print("Primer nodo eliminado")


def last_delete():
    global head, tail

    if head is None:
        print("Lista vacía")
    elif tail.ant is None:
        head = None
        tail = None
        print("Único nodo eliminado")
    else:
        tail = tail.ant
        tail.next = None
        print("Último nodo eliminado")


def select_delete():
    global head, tail

    loc = int(input("\nIntroduce la ubicación después de la cual deseas eliminar: "))

    if head is None:
        print("Lista vacía, no se puede eliminar")
        return

    if loc <= 0:
        print("Ubicación inválida")
        return

    ptr = head
    prev = None

    for i in range(loc):
        prev = ptr
        ptr = ptr.next
        if ptr is None:
            print("Ubicación no encontrada")
            return

    prev.next = ptr.next

    if ptr.next is not None:
        ptr.next.ant = prev
    else:
        tail = prev

    print(f"Nodo eliminado en la posición {loc+1}")


def search():
    if head is None:
        print("Lista vacía")
        return

    item = int(input("\nIntroduce el elemento que deseas buscar: "))

    ptr = head
    pos = 1
    found = False

    while ptr is not None:
        if ptr.data == item:
            print(f"Elemento encontrado en la ubicación {pos}")
            found = True
        ptr = ptr.next
        pos += 1

    if not found:
        print("Elemento no encontrado")


def display():
    if head is None:
        print("Nada que imprimir")
        return

    print("\nImprimiendo valores...")
    ptr = head
    while ptr is not None:
        print(ptr.data)
        ptr = ptr.next


# -------- MENÚ PRINCIPAL --------
def menu():
    choice = 0

    while choice != 9:
        print("\n********** Menú principal **********")
        print("1. Insertar al principio")
        print("2. Insertar al final")
        print("3. Insertar después de una ubicación")
        print("4. Eliminar del principio")
        print("5. Eliminar desde el último")
        print("6. Eliminar después de una ubicación")
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
        else:
            print("Opción inválida")


# Ejecutar el programa
menu()
