using System;

public class Nodo
{
    public int Data;
    public Nodo Next;

    public Nodo(int data)
    {
        this.Data = data;
        this.Next = null;
    }
}

public class Menu
{
    public static void Main(string[] args)
    {
        ListaSimple lista = new ListaSimple();
        int choice = 0;
        while (choice != 9)
        {
            Console.WriteLine("\n**********Menú principal**********");
            Console.WriteLine("Elige una opción de la siguiente lista ...");
            Console.WriteLine("=========================================");
            Console.WriteLine("\n1. Insertar al principio\n2. Insertar al final\n3. Insertar\n4. Eliminar del principio\n" +
                            "5. Eliminar desde el último\n6. Eliminar nodo después de la ubicación especificada\n" +
                            "7. Buscar un elemento\n8. Mostrar\n9. Salir");
            Console.WriteLine("\nIngrese su opción");
            
            if (!int.TryParse(Console.ReadLine(), out choice))
            {
                Console.WriteLine("Por favor, ingrese un número válido.");
                continue;
            }

            switch (choice)
            {
                case 1:
                    lista.BegInsert();
                    break;
                case 2:
                    lista.LastInsert();
                    break;
                case 3:
                    lista.SelectInsert();
                    break;
                case 4:
                    lista.BeginDelete();
                    break;
                case 5:
                    lista.LastDelete();
                    break;
                case 6:
                    lista.SelectDelete();
                    break;
                case 7:
                    lista.Search();
                    break;
                case 8:
                    lista.Display();
                    break;
                case 9:
                    Console.WriteLine("Saliendo del programa...");
                    return;
                default:
                    Console.WriteLine("\nIntroduzca una opción válida..");
                    break;
            }
        }
    }
}

public class ListaSimple
{
    private Nodo head;

    public void BegInsert()
    {
        Console.WriteLine("\nIngrese valor: ");
        if (int.TryParse(Console.ReadLine(), out int item))
        {
            Nodo nuevoNodo = new Nodo(item);
            nuevoNodo.Next = head;
            head = nuevoNodo;
            Console.WriteLine("\nNodo insertado al principio");
        }
        else
        {
            Console.WriteLine("\nEntrada invalida");
        }
    }

    public void LastInsert()
    {
        Console.WriteLine("\nIngrese valor: ");
        if (int.TryParse(Console.ReadLine(), out int item))
        {
            Nodo nuevoNodo = new Nodo(item);

            if (head == null)
            {
                head = nuevoNodo;
            }
            else
            {
                Nodo temp = head;
                while (temp.Next != null)
                {
                    temp = temp.Next;
                }
                temp.Next = nuevoNodo;
            }
            Console.WriteLine("\nNodo insertado al final");
        }
        else
        {
            Console.WriteLine("\nEntrada invalida");
        }
    }

    public void SelectInsert()
    {
        Console.WriteLine("\nIngrese valor: ");
        if (!int.TryParse(Console.ReadLine(), out int item))
        {
            Console.WriteLine("\nEntrada invalida");
            return;
        }

        Console.WriteLine("\nIngrese ubicacion despues de la que se va a insertar: ");
        if (int.TryParse(Console.ReadLine(), out int ubi))
        {
            if (ubi <= 0)
            {
                Console.WriteLine("\nUbicacion invalida");
                return;
            }
        }
        else
        {
            Console.WriteLine("\nEntrada invalida");
            return;
        }

        if (head == null)
        {
            Console.WriteLine("\nLista vacia");
            return;
        }

        Nodo temp = head;

        for (int i = 1; i < ubi; i++)
        {
            temp = temp?.Next;
            if (temp == null)
            {
                Console.WriteLine("\nUbicacion no encontrada");
                return;
            }
        }

        Nodo nuevoNodo = new Nodo(item);

        nuevoNodo.Next = temp.Next;
        temp.Next = nuevoNodo;
        Console.WriteLine("\nNodo insertado despues de la ubicacion " + ubi);
    }

    public void BeginDelete()
    {
        if(head == null)
        {
            Console.WriteLine("\nLista vacia");
        }
        else
        {
            head = head.Next;
            Console.WriteLine("\nPrimer nodo eliminado");
        }
    }

    public void LastDelete()
    {
        if(head == null)
        {
            Console.WriteLine("\nLista vacia");
        }
        else
        {
            Nodo temp = head, temp2 = head;
            while(temp.Next != null)
            {
                temp2 = temp;
                temp = temp.Next;
            }
            temp2.Next = null;

            Console.WriteLine("\nUltimo nodo eliminado");
        }
    }

    public void SelectDelete()
    {
        Console.WriteLine("\nIngrese ubicacion despues de la que se va a eliminar: ");
        if (int.TryParse(Console.ReadLine(), out int ubi))
        {
            if (ubi <= 0)
            {
                Console.WriteLine("\nUbicacion invalida");
                return;
            }
        }
        else
        {
            Console.WriteLine("\nEntrada invalida");
            return;
        }

        if (head == null)
        {
            Console.WriteLine("\nLista vacia");
            return;
        }

        Nodo temp = head;

        for (int i = 1; i < ubi; i++)
        {
            temp = temp?.Next;
            if (temp == null)
            {
                Console.WriteLine("\nUbicacion no encontrada");
                return;
            }
        }

        if(temp.Next == null) Console.WriteLine("\nUbicacion no encontrada");

        temp.Next = temp.Next.Next;

        Console.WriteLine("\nNodo eliminado despues de la ubicacion " + ubi);
    }

    public void Display()
    {
        if(head == null)
        {
            Console.WriteLine("\nLista vacia");
        }
        else
        {
            Console.WriteLine("\nImprimiendo valores......");
            Nodo temp = head;
            while(temp != null)
            {
                Console.Write(temp.Data + " ");
                temp = temp?.Next;
            }
        }
    }

    public void Search()
    {
        Console.WriteLine("\nIngresa el valor a buscar");

        if(!int.TryParse(Console.ReadLine(), out int item))
        {
            item = 0;
        }

        if(head == null)
        {
            Console.WriteLine("\nLista vacia");
        }

        Nodo ptr = head;
        int i=0;
        bool encontrado = false;
        while(ptr != null)
        {
            i++;
            if(item == ptr.Data)
            {
                Console.WriteLine("\nElemento "+ item +" encontrado en la ubicacion "+ i);
                encontrado = true;
            }
            ptr = ptr.Next;
        }

        if(!encontrado) Console.WriteLine("\nElemento "+ item +" no encontrado en la lista");

    }

}