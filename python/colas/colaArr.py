MAXSIZE = 5
queue = [0] * MAXSIZE
front = -1
rear = -1

def insertar():
    global front, rear
    
    elemento = int(input("\nIngrese el elemento: "))
    
    if rear == MAXSIZE - 1:
        print("\nDESBORDAMIENTO (OVERFLOW)\n")
        return
    
    if front == -1 and rear == -1:
        front = rear = 0
    else:
        rear += 1
    
    queue[rear] = elemento
    print("\nElemento insertado correctamente.\n")

def eliminar():
    global front, rear
    
    if front == -1 or front > rear:
        print("\nSUBDESBORDAMIENTO (UNDERFLOW)\n")
        return
    
    elemento = queue[front]
    
    if front == rear:
        front = rear = -1
    else:
        front += 1
    
    print(f"\nElemento eliminado: {elemento}\n")

def mostrar():
    if rear == -1 or front == -1 or front > rear:
        print("\nLa cola está vacía.\n")
    else:
        print("\nElementos en la cola:\n")
        for i in range(front, rear + 1):
            print(f"{queue[i]}\n")

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