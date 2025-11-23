using System;

class Node
{
    public int data;
    public Node next;

    public Node(int data)
    {
        this.data = data;
        this.next = null;
    }
}

class CircularList
{
    static Node head = null;
    static void Main()
    {
        int choice = 0;
        while (choice != 9)
        {
            Console.WriteLine("\n********** Menú **********");
            Console.WriteLine("1. Insertar al inicio");
            Console.WriteLine("2. Insertar al final");
            Console.WriteLine("3. Insertar después de posición");
            Console.WriteLine("4. Eliminar primero");
            Console.WriteLine("5. Eliminar último");
            Console.WriteLine("6. Eliminar después de posición");
            Console.WriteLine("7. Buscar");
            Console.WriteLine("8. Mostrar");
            Console.WriteLine("9. Salir");

            choice = int.Parse(Console.ReadLine());

            switch (choice)
            {
                case 1: BegInsert(); break;
                case 2: LastInsert(); break;
                case 3: SelectInsert(); break;
                case 4: BeginDelete(); break;
                case 5: LastDelete(); break;
                case 6: SelectDelete(); break;
                case 7: Search(); break;
                case 8: Display(); break;
            }
        }
    }

    static void BegInsert()
    {
        Console.Write("\nIngrese valor: ");
        int item = int.Parse(Console.ReadLine());
        Node ptr = new Node(item);

        if (head == null)
        {
            head = ptr;
            ptr.next = head;
        }
        else
        {
            Node temp = head;
            while (temp.next != head) temp = temp.next;

            ptr.next = head;
            temp.next = ptr;
            head = ptr;
        }
        Console.WriteLine("Nodo insertado");
    }

    static void LastInsert()
    {
        Console.Write("\nIngrese valor: ");
        int item = int.Parse(Console.ReadLine());
        Node ptr = new Node(item);

        if (head == null)
        {
            head = ptr;
            ptr.next = head;
        }
        else
        {
            Node temp = head;
            while (temp.next != head) temp = temp.next;

            temp.next = ptr;
            ptr.next = head;
        }
        Console.WriteLine("Nodo insertado");
    }

    static void SelectInsert()
    {
        Console.Write("\nIngrese valor: ");
        int item = int.Parse(Console.ReadLine());
        Console.Write("Posición: ");
        int loc = int.Parse(Console.ReadLine());

        Node ptr = new Node(item);
        Node temp = head;

        for (int i = 1; i < loc; i++)
        {
            temp = temp.next;
            if (temp == head)
            {
                Console.WriteLine("Posición inválida");
                return;
            }
        }

        ptr.next = temp.next;
        temp.next = ptr;
        Console.WriteLine("Nodo insertado");
    }

    static void BeginDelete()
    {
        if (head == null) return;

        if (head.next == head)
            head = null;
        else
        {
            Node temp = head;
            while (temp.next != head) temp = temp.next;

            head = head.next;
            temp.next = head;
        }
        Console.WriteLine("Nodo eliminado");
    }

    static void LastDelete()
    {
        if (head == null) return;

        if (head.next == head)
        {
            head = null;
        }
        else
        {
            Node temp = head, prev = null;
            while (temp.next != head)
            {
                prev = temp;
                temp = temp.next;
            }
            prev.next = head;
        }
        Console.WriteLine("Nodo eliminado");
    }

    static void SelectDelete()
    {
        Console.Write("\nPosición: ");
        int loc = int.Parse(Console.ReadLine());

        Node ptr = head, prev = null;

        for (int i = 1; i < loc; i++)
        {
            prev = ptr;
            ptr = ptr.next;

            if (ptr == head)
            {
                Console.WriteLine("Posición inválida");
                return;
            }
        }

        prev.next = ptr.next;
        Console.WriteLine("Nodo eliminado");
    }

    static void Search()
    {
        if (head == null) return;

        Console.Write("\nBuscar valor: ");
        int item = int.Parse(Console.ReadLine());

        Node temp = head;
        int i = 1;
        do
        {
            if (temp.data == item)
                Console.WriteLine("Encontrado en posición: " + i);

            temp = temp.next;
            i++;
        } while (temp != head);
    }

    static void Display()
    {
        if (head == null) return;

        Node temp = head;
        do
        {
            Console.WriteLine(temp.data);
            temp = temp.next;
        } while (temp != head);
    }
}
