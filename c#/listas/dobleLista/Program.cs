using System;

class Node
{
    public int Data;
    public Node Next;

    public Node(int data)
    {
        Data = data;
        Next = null;
    }
}

class CircularLinkedList
{
    private static Node head = null;

    static void Main(string[] args)
    {
        int choice = 0;

        while (choice != 9)
        {
            Console.WriteLine("\n********** Menú principal **********");
            Console.WriteLine("1. Insertar al principio");
            Console.WriteLine("2. Insertar al final");
            Console.WriteLine("3. Insertar después de una posición");
            Console.WriteLine("4. Eliminar del principio");
            Console.WriteLine("5. Eliminar del final");
            Console.WriteLine("6. Eliminar nodo después de la ubicación");
            Console.WriteLine("7. Buscar un elemento");
            Console.WriteLine("8. Mostrar");
            Console.WriteLine("9. Salir");

            Console.Write("\nIngrese su opción: ");
            choice = int.Parse(Console.ReadLine());

            switch (choice)
            {
                case 1:
                    BegInsert();
                    break;
                case 2:
                    LastInsert();
                    break;
                case 3:
                    SelectInsert();
                    break;
                case 4:
                    BeginDelete();
                    break;
                case 5:
                    LastDelete();
                    break;
                case 6:
                    SelectDelete();
                    break;
                case 7:
                    Search();
                    break;
                case 8:
                    Display();
                    break;
                case 9:
                    Console.WriteLine("Saliendo...");
                    break;
                default:
                    Console.WriteLine("Opción inválida");
                    break;
            }
        }
    }

    // 1. Insertar al principio
    static void BegInsert()
    {
        Console.Write("\nIngrese valor: ");
        int item = int.Parse(Console.ReadLine());

        Node newNode = new Node(item);

        if (head == null)
        {
            head = newNode;
            newNode.Next = head;
        }
        else
        {
            Node temp = head;
            while (temp.Next != head)
            {
                temp = temp.Next;
            }

            newNode.Next = head;
            temp.Next = newNode;
            head = newNode;
        }

        Console.WriteLine("Nodo insertado al inicio");
    }

    // 2. Insertar al final
    static void LastInsert()
    {
        Console.Write("\nIngrese valor: ");
        int item = int.Parse(Console.ReadLine());

        Node newNode = new Node(item);

        if (head == null)
        {
            head = newNode;
            newNode.Next = head;
        }
        else
        {
            Node temp = head;
            while (temp.Next != head)
            {
                temp = temp.Next;
            }

            temp.Next = newNode;
            newNode.Next = head;
        }

        Console.WriteLine("Nodo insertado al final");
    }

    // 3. Insertar después de una posición
    static void SelectInsert()
    {
        if (head == null)
        {
            Console.WriteLine("Lista vacía");
            return;
        }

        Console.Write("\nIngrese valor: ");
        int item = int.Parse(Console.ReadLine());

        Console.Write("Ingrese la posición después de la cual insertar: ");
        int loc = int.Parse(Console.ReadLine());

        if (loc <= 0)
        {
            Console.WriteLine("Posición inválida");
            return;
        }

        Node newNode = new Node(item);
        Node temp = head;

        for (int i = 1; i < loc; i++)
        {
            temp = temp.Next;
            if (temp == head)
            {
                Console.WriteLine("Ubicación fuera de los límites");
                return;
            }
        }

        newNode.Next = temp.Next;
        temp.Next = newNode;

        Console.WriteLine("Nodo insertado");
    }

    // 4. Eliminar al principio
    static void BeginDelete()
    {
        if (head == null)
        {
            Console.WriteLine("Lista vacía");
            return;
        }

        if (head.Next == head)
        {
            head = null;
        }
        else
        {
            Node temp = head;
            while (temp.Next != head)
            {
                temp = temp.Next;
            }

            head = head.Next;
            temp.Next = head;
        }

        Console.WriteLine("Primer nodo eliminado");
    }

    // 5. Eliminar al final
    static void LastDelete()
    {
        if (head == null)
        {
            Console.WriteLine("Lista vacía");
            return;
        }

        if (head.Next == head)
        {
            head = null;
            Console.WriteLine("Se eliminó el único nodo");
            return;
        }

        Node prev = null;
        Node temp = head;

        while (temp.Next != head)
        {
            prev = temp;
            temp = temp.Next;
        }

        prev.Next = head;

        Console.WriteLine("Último nodo eliminado");
    }

    // 6. Eliminar después de una posición
    static void SelectDelete()
    {
        if (head == null)
        {
            Console.WriteLine("Lista vacía");
            return;
        }

        Console.Write("\nIngrese la posición después de la cual eliminar: ");
        int loc = int.Parse(Console.ReadLine());

        if (loc <= 0)
        {
            Console.WriteLine("Posición inválida");
            return;
        }

        Node ptr1 = head;
        Node ptr = head.Next;

        for (int i = 2; i < loc; i++)
        {
            ptr1 = ptr;
            ptr = ptr.Next;

            if (ptr == head)
            {
                Console.WriteLine("Ubicación fuera de rango");
                return;
            }
        }

        if (ptr == head)
        {
            Console.WriteLine("Ubicación fuera de rango");
            return;
        }

        ptr1.Next = ptr.Next;

        Console.WriteLine($"Nodo eliminado en la posición {loc + 1}");
    }

    // 7. Buscar
    static void Search()
    {
        if (head == null)
        {
            Console.WriteLine("Lista vacía");
            return;
        }

        Console.Write("\nIngrese el elemento a buscar: ");
        int item = int.Parse(Console.ReadLine());

        Node temp = head;
        int pos = 1;
        bool found = false;

        do
        {
            if (temp.Data == item)
            {
                Console.WriteLine($"Elemento encontrado en la posición {pos}");
                found = true;
            }

            temp = temp.Next;
            pos++;

        } while (temp != head);

        if (!found)
        {
            Console.WriteLine("Elemento no encontrado");
        }
    }

    // 8. Mostrar
    static void Display()
    {
        if (head == null)
        {
            Console.WriteLine("Nada que imprimir");
            return;
        }

        Node temp = head;

        Console.WriteLine("\nMostrando lista circular:");

        do
        {
            Console.WriteLine(temp.Data);
            temp = temp.Next;
        } while (temp != head);
    }
}
