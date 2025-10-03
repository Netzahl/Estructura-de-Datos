class Examen1
{

    public static void ValorMaximo(int[,] a)
    {
        int max = 0;
        for (int i = 0; i < 6; i++)
        {
            for (int j = 0; j < 6; j++)
            {
                if (a[i, j] >= max)
                {
                    max = a[i, j];
                }
            }
        }

        Console.WriteLine("El valor maximo del arreglo 2 es: " + max);

    }

    public static void Busqueda(ref int[] a, int b)
    {
        int posicion = -1;
        for (int i = 0; i < a.Length; i++)
        {
            if (a[i] == b)
            {
                posicion = i;
                break;
            }
        }

        if (posicion >= 0)
        {
            Console.WriteLine("El numero " + b + " fue encontrado en la posicion " + (posicion + 1) + " del array 1");
        }
        else
        {
            Console.WriteLine("El numero " + b + " no fue encontrado en el array 1");
        }

    }

    public static void HeapSort(ref int[] a, int h)
    {
        while (h >= 0)
        {
            int adicional = 0, j = 0;
            for (int i = h; i >= 0; i--)
            {
                j = i / 2;
                if (a[i] > a[j])
                {
                    adicional = a[i];
                    a[i] = a[j];
                    a[j] = adicional;
                }
            }
            adicional = a[h];
            a[h] = a[0];
            a[0] = adicional;
            h--;
        }
    }

    public static void Show(int[] a)
    {
        foreach (var x in a)
        {
            Console.Write(x + " ");
        }
        Console.WriteLine();
    }

    public static void Main()
    {

        int[] a = [12, 94, 32, 5, 48, 64, 26, 57];
        int tamaño = a.Length;
        Console.WriteLine("Antes de ordenar: ");
        Show(a);
        HeapSort(ref a, tamaño - 1);
        Console.WriteLine("Despues de ordenar: ");
        Show(a);

        int buscar = 32;
        Console.WriteLine("Numero a buscar: " + buscar);
        Busqueda(ref a, buscar);
        buscar = 27;
        Console.WriteLine("Numero a buscar: " + buscar);
        Busqueda(ref a, buscar);

        int[,] a2 = new int[6, 6];
        int cont = 0;
        for (int i = 0; i < 6; i++)
        {
            for (int j = 0; j < 6; j++)
            {
                a2[i, j] = cont;
                cont++;
            }
        }

        ValorMaximo(a2);

        int[,,] a3 = new int[5, 5, 5];

        cont = 0;
        for (int i = 4; i >= 0; i--)
        {
            for (int j = 4; j >= 0; j--)
            {
                for (int h = 4; h >= 0; h--)
                {
                    a3[i, j, h] = cont;
                    cont++;
                }
            }
        }

        int[,] temp1 = new int[5, 5];
        int[,] temp2 = new int[5, 5];
        int[,] temp3 = new int[5, 5];
        int[,] temp4 = new int[5, 5];
        int[,] temp5 = new int[5, 5];

        int[] t1 = new int[25];
        int[] t2 = new int[25];
        int[] t3 = new int[25];
        int[] t4 = new int[25];
        int[] t5 = new int[25];

        for (int i = 0; i < 5; i++)
        {
            for (int g = 0; g < 5; g++)
            {
                for (int h = 0; h < 5; h++)
                {
                    if (i == 0)
                    {
                        temp1[g, h] = a3[i, g, h];
                    }
                    if (i == 1)
                    {
                        temp2[g, h] = a3[i, g, h];
                    }
                    if (i == 2)
                    {
                        temp3[g, h] = a3[i, g, h];
                    }
                    if (i == 3)
                    {
                        temp4[g, h] = a3[i, g, h];
                    }
                    if (i == 4)
                    {
                        temp5[g, h] = a3[i, g, h];
                    }
                }
            }
        }

        cont = 0;

        for (int g = 0; g < 5; g++)
        {
            for (int h = 0; h < 5; h++)
            {
                t1[cont] = temp1[g, h];
                t2[cont] = temp2[g, h];
                t3[cont] = temp3[g, h];
                t4[cont] = temp4[g, h];
                t5[cont] = temp5[g, h];
                cont++;
            }
        }

        HeapSort(ref t1, 24);
        HeapSort(ref t2, 24);
        HeapSort(ref t3, 24);
        HeapSort(ref t4, 24);
        HeapSort(ref t5, 24);

        cont = 0;

        for (int g = 0; g < 5; g++)
        {
            for (int h = 0; h < 5; h++)
            {
                temp1[g, h] = t1[cont];
                temp2[g, h] = t2[cont];
                temp3[g, h] = t3[cont];
                temp4[g, h] = t4[cont];
                temp5[g, h] = t5[cont];
                cont++;
            }
        }

        for (int i = 0; i < 5; i++)
        {
            for (int g = 0; g < 5; g++)
            {
                for (int h = 0; h < 5; h++)
                {
                    if (i == 0)
                    {
                        a3[i, g, h] = temp1[g, h];
                    }
                    if (i == 1)
                    {
                        a3[i, g, h] = temp2[g, h];
                    }
                    if (i == 2)
                    {
                        a3[i, g, h] = temp3[g, h];
                    }
                    if (i == 3)
                    {
                        a3[i, g, h] = temp4[g, h];
                    }
                    if (i == 4)
                    {
                        a3[i, g, h] = temp5[g, h];
                    }
                }
            }
        }

        for (int i = 0; i < 5; i++)
        {
            for (int g = 0; g < 5; g++)
            {
                for (int h = 0; h < 5; h++)
                {
                    Console.Write(a3[i, g, h] + " ");
                }
            }
            Console.WriteLine();
        }

    }
}