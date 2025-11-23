class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.ant = None


head = None
tail = None


def begInsert():
    global head, tail

    item = int(input("\nIngrese valor: "))
    ptr = Node(item)

    if head is None:
        head = ptr
        tail = ptr
        ptr.next = ptr
        ptr.ant = ptr
    else:
        ptr.next = head
        ptr.ant = tail
        head.ant = ptr
        tail.next = ptr
        head = ptr

    print("\nNodo insertado")


def lastInsert():
    global head, tail

    item = int(input("\nIngrese valor: "))
    ptr = Node(item)

    if head is None:
        head = ptr
        tail = ptr
        ptr.next = ptr
        ptr.ant = ptr
    else:
        tail.next = ptr
        ptr.ant = tail
        ptr.next = head
        head.ant = ptr
        tail = ptr

    print("\nNodo insertado")


def selectInsert():
    global head, tail

    item = int(input("\nIntroduzca el valor del elemento: "))
    loc = int(input("Introduzca la posición después de la cual desea insertar: "))

    if loc <= 0:
        print("\nUbicación no válida")
        return

    if head is None:
        print("\nNo se puede insertar, lista vacía")
        return

    ptr = Node(item)
    temp = head

    for i in range(1, loc):
        temp = temp.next
        if temp == head:
            print("\nUbicación no encontrada")
            return

    ptr.next = temp.next
    ptr.ant = temp
    temp.next.ant = ptr
    temp.next = ptr

    if temp == tail:
        tail = ptr

    print("\nNodo insertado")


def beginDelete():
    global head, tail

    if head is None:
        print("\nLa lista está vacía")
    elif head.next == head:
        head = None
        tail = None
        print("\nÚnico nodo eliminado...")
    else:
        head = head.next
        head.ant = tail
        tail.next = head
        print("\nPrimer nodo eliminado...")


def lastDelete():
    global head, tail

    if head is None:
        print("\nLa lista está vacía")
    elif head.next == head:
        head = None
        tail = None
        print("\nÚnico nodo eliminado...")
    else:
        tail = tail.ant
        tail.next = head
        head.ant = tail
        print("\nÚltimo nodo eliminado...")


def selectDelete():
    global head, tail

    if head is None:
        print("\nLista vacía, no se puede eliminar")
        return

    loc = int(input("\nIntroduzca la posición después de la cual desea eliminar: "))

    if loc <= 0:
        print("\nUbicación no válida")
        return

    ptr = head
    prev = None

    for i in range(loc):
        prev = ptr
        ptr = ptr.next

        if ptr == head:
            print("\nUbicación no encontrada")
            return

    prev.next = ptr.next
    ptr.next.ant = prev

    if ptr == tail:
        tail = prev

    print("\nNodo eliminado")


def search():
    if head is None:
        print("\nLista vacía")
        return

    item = int(input("\nIntroduce el elemento que deseas buscar: "))
    temp = head
    pos = 1
    found = False

    while True:
        if temp.data == item:
            print(f"\nElemento encontrado en la posición {pos}")
            found = True

        temp = temp.next
        pos += 1

        if temp == head:
            break

    if not found:
        print("\nElemento no encontrado")


def display():
    if head is None:
        print("\nNada que imprimir")
        return

    print("\nMostrando valores de la lista:")

    temp = head
    while True:
        print(temp.data)
        temp = temp.next

        if temp == head:
            break


def menu():
    while True:
        print("\n********** Menú principal **********")
        print("1. Insertar al principio")
        print("2. Insertar al final")
        print("3. Insertar después de una posición")
        print("4. Eliminar del principio")
        print("5. Eliminar desde el último")
        print("6. Eliminar después de una posición")
        print("7. Buscar un elemento")
        print("8. Mostrar")
        print("9. Salir")

        try:
            choice = int(input("\nIngrese su opción: "))
        except ValueError:
            print("Opción inválida")
            continue

        if choice == 1:
            begInsert()
        elif choice == 2:
            lastInsert()
        elif choice == 3:
            selectInsert()
        elif choice == 4:
            beginDelete()
        elif choice == 5:
            lastDelete()
        elif choice == 6:
            selectDelete()
        elif choice == 7:
            search()
        elif choice == 8:
            display()
        elif choice == 9:
            print("\nAdiós...")
            break
        else:
            print("\nIntroduzca una opción válida...")


menu()
