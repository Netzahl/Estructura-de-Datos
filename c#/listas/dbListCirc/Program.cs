using System;

class Node
{
    public int data;
    public Node next;
    public Node ant;

    public Node(int data)
    {
        this.data = data;
        this.next = null;
        this.ant = null;
    }
}

class Program
{
    static Node head = null;
    static Node tail = null;

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
            Console.WriteLine("5. Eliminar desde el último");
            Console.WriteLine("6. Eliminar después de la ubicación");
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
                    Console.WriteLine("Introduzca una opción válida");
                    break;
            }
        }
    }

    // Insertar al principio
    static void BegInsert()
    {
        Console.Write("\nIngrese valor: ");
        int item = int.Parse(Console.ReadLine());

        Node ptr = new Node(item);

        if (head == null)
        {
            head = ptr;
            tail = ptr;
            ptr.next = ptr;
            ptr.ant = ptr;
        }
        else
        {
            ptr.next = head;
            ptr.ant = tail;
            head.ant = ptr;
            tail.next = ptr;
            head = ptr;
        }

        Console.WriteLine("Nodo insertado");
    }

    // Insertar al final
    static void LastInsert()
    {
        Console.Write("\nIngrese valor: ");
        int item = int.Parse(Console.ReadLine());

        Node ptr = new Node(item);

        if (head == null)
        {
            head = ptr;
            ptr.next = ptr;
            ptr.ant = ptr;
            tail = ptr;
        }
        else
        {
            tail.next = ptr;
            ptr.ant = tail;
            ptr.next = head;
            head.ant = ptr;
            tail = ptr;
        }

        Console.WriteLine("Nodo insertado");
    }

    // Insertar después de una posición
    static void SelectInsert()
    {
        if (head == null)
        {
            Console.WriteLine("La lista está vacía");
            return;
        }

        Console.Write("\nIntroduzca el valor: ");
        int item = int.Parse(Console.ReadLine());

        Console.Write("Introduce la ubicación después de la cual deseas ingresar: ");
        int loc = int.Parse(Console.ReadLine());

        if (loc <= 0)
        {
            Console.WriteLine("Ubicación no válida.");
            return;
        }

        Node temp = head;
        for (int i = 1; i < loc; i++)
        {
            temp = temp.next;
            if (temp == head)
            {
                Console.WriteLine("No se puede insertar");
                return;
            }
        }

        Node ptr = new Node(item);

        ptr.next = temp.next;
        ptr.ant = temp;
        temp.next = ptr;
        ptr.next.ant = ptr;

        if (ptr.next == head)
        {
            tail = ptr;
        }

        Console.WriteLine("Nodo insertado");
    }

    // Eliminar al inicio
    static void BeginDelete()
    {
        if (head == null)
        {
            Console.WriteLine("La lista está vacía");
        }
        else if (head.next == head)
        {
            head = null;
            tail = null;
            Console.WriteLine("Único nodo eliminado...");
        }
        else
        {
            Node ptr = head;
            head = ptr.next;
            head.ant = tail;
            tail.next = head;
            Console.WriteLine("Primer nodo eliminado...");
        }
    }

    // Eliminar al final
    static void LastDelete()
    {
        if (head == null)
        {
            Console.WriteLine("La lista está vacía");
        }
        else if (tail.ant == tail)
        {
            head = null;
            tail = null;
            Console.WriteLine("Único nodo eliminado...");
        }
        else
        {
            Node ptr = tail;
            tail = tail.ant;
            tail.next = head;
            Console.WriteLine("Último nodo eliminado...");
        }
    }

    // Eliminar después de cierta posición
    static void SelectDelete()
    {
        if (head == null)
        {
            Console.WriteLine("Lista vacía");
            return;
        }

        Console.Write("\nIntroduce la ubicación después de la cual deseas eliminar: ");
        int loc = int.Parse(Console.ReadLine());

        if (loc <= 0)
        {
            Console.WriteLine("Ubicación no válida");
            return;
        }

        Node ptr = head;
        Node prev = null;

        for (int i = 0; i < loc; i++)
        {
            prev = ptr;
            ptr = ptr.next;

            if (ptr == head)
            {
                Console.WriteLine("No se puede eliminar, ubicación no encontrada");
                return;
            }
        }

        prev.next = ptr.next;
        ptr.next.ant = prev;

        if (ptr.next == head)
        {
            tail = prev;
        }

        Console.WriteLine("Nodo eliminado en posición " + (loc + 1));
    }

    // Buscar elemento
    static void Search()
    {
        if (head == null)
        {
            Console.WriteLine("Lista vacía");
            return;
        }

        Console.Write("\nIntroduce el elemento a buscar: ");
        int item = int.Parse(Console.ReadLine());

        Node ptr = head;
        int pos = 1;
        bool found = false;

        do
        {
            if (ptr.data == item)
            {
                Console.WriteLine("Elemento encontrado en la posición " + pos);
                found = true;
            }
            pos++;
            ptr = ptr.next;

        } while (ptr != head);

        if (!found)
        {
            Console.WriteLine("Elemento no encontrado");
        }
    }

    // Mostrar lista
    static void Display()
    {
        if (head == null)
        {
            Console.WriteLine("Nada que imprimir");
            return;
        }

        Console.WriteLine("\nMostrando lista:");
        Node ptr = head;

        do
        {
            Console.WriteLine(ptr.data);
            ptr = ptr.next;

        } while (ptr != head);
    }
}
