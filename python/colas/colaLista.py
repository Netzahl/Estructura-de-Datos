class Node:
    def __init__(self):
        self.data = 0
        self.next = None

head = None
tail = None

def insertar():
    global head, tail
    
    elemento = int(input("\nIngrese el elemento: "))
    
    ptr = Node()
    
    if ptr is None:
        print("\nDESBORDAMIENTO (OVERFLOW)\n")
        return
    
    if head is None and tail is None:
        head = tail = ptr
    else:
        tail.next = ptr
        tail = ptr
    
    ptr.data = elemento
    print("\nElemento insertado correctamente.\n")

def eliminar():
    global head, tail
    
    if head is None:
        print("\nSUBDESBORDAMIENTO (UNDERFLOW)\n")
        return
    
    elemento = head.data
    
    if head == tail:
        head = tail = None
    else:
        head = head.next
    
    print(f"\nElemento eliminado: {elemento}\n")

def mostrar():
    ptr = head
    
    if ptr is None:
        print("\nNada que imprimir")
    else:
        print("\nImprimiendo valores . . . . . . ")
        while ptr is not None:
            print(ptr.data, end='')
            if ptr != tail:
                print(' | ', end='')
            ptr = ptr.next
        print()

def main():
    opcion = 0
    
    while opcion != 4:
        print("\n****************** MENÚ PRINCIPAL ******************\n")
        print("====================================================\n")
        print("1. Insertar un elemento\n")
        print("2. Eliminar un elemento\n")
        print("3. Mostrar la cola\n")
        print("4. Salir\n")
        
        opcion = int(input("Ingrese su opción: "))
        
        if opcion == 1:
            insertar()
        elif opcion == 2:
            eliminar()
        elif opcion == 3:
            mostrar()
        elif opcion == 4:
            print("\nSaliendo del programa...\n")
        else:
            print("\nOpción inválida. Intente nuevamente.\n")

if __name__ == "__main__":
    main()