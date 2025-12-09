using System;

class Node
{
    public int data;
    public Node next = null;
}

class ColaLista
{
    private static Node head = null;
    private static Node tail = null;
    
    static void Insertar()
    {
        int elemento;
        
        Console.Write("\nIngrese el elemento: ");
        elemento = int.Parse(Console.ReadLine());
        
        Node ptr = new Node();
        
        if (ptr == null)
        {
            Console.WriteLine("\nDESBORDAMIENTO (OVERFLOW)\n");
            return;
        }
        
        if (head == null && tail == null)
        {
            head = tail = ptr;
        }
        else
        {
            tail.next = ptr;
            tail = ptr;
        }
        
        ptr.data = elemento;
        Console.WriteLine("\nElemento insertado correctamente.\n");
    }
    
    static void Eliminar()
    {
        if (head == null)
        {
            Console.WriteLine("\nSUBDESBORDAMIENTO (UNDERFLOW)\n");
            return;
        }
        
        int elemento = head.data;
        
        if (head == tail)
        {
            head = tail = null;
        }
        else
        {
            head = head.next;
        }
        
        Console.WriteLine("\nElemento eliminado: " + elemento + "\n");
    }
    
    static void Mostrar()
    {
        Node ptr = head;
        
        if (ptr == null)
        {
            Console.WriteLine("\nNada que imprimir");
        }
        else
        {
            Console.WriteLine("\nImprimiendo valores . . . . . . ");
            while (ptr != null)
            {
                Console.Write(ptr.data);
                if (ptr != tail)
                {
                    Console.Write(" | ");
                }
                ptr = ptr.next;
            }
            Console.WriteLine();
        }
    }
    
    static void Main()
    {
        int opcion = 0;
        
        while (opcion != 4)
        {
            Console.WriteLine("\n****************** MENÚ PRINCIPAL ******************\n");
            Console.WriteLine("====================================================\n");
            Console.WriteLine("1. Insertar un elemento\n");
            Console.WriteLine("2. Eliminar un elemento\n");
            Console.WriteLine("3. Mostrar la cola\n");
            Console.WriteLine("4. Salir\n");
            Console.Write("Ingrese su opción: ");
            opcion = int.Parse(Console.ReadLine());
            
            switch (opcion)
            {
                case 1:
                    Insertar();
                    break;
                case 2:
                    Eliminar();
                    break;
                case 3:
                    Mostrar();
                    break;
                case 4:
                    Console.WriteLine("\nSaliendo del programa...\n");
                    break;
                default:
                    Console.WriteLine("\nOpción inválida. Intente nuevamente.\n");
                    break;
            }
        }
    }
}