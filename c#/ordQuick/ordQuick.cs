using System.Globalization;
using Microsoft.VisualBasic;

class Ord_Quick
{
    public static (int[],int) Partition(int[] a, int l, int h)
    {
        int pvt = a[h];
        int j = l - 1;
        for (int k = l; k < h; k++)
        {
            if (a[k] < pvt)
            {
                j++;
                a = Swap(a, j, k);
            }
        }
        a = Swap(a, j + 1, h);

        return (a, j+1);

    }

    public static int[] Swap(int[] a, int j, int k)
    {
        int adicional = 0;
        adicional = a[j];
        a[j] = a[k];
        a[k] = adicional;
        return a;
    }

    public static int[] OrdQuick(int[] a, int l, int h)
    {
        if (l < h)
        {
            var valores = Partition(a, l, h);
            a = OrdQuick(valores.Item1, l, valores.Item2 - 1);
            a = OrdQuick(valores.Item1, valores.Item2 + 1, h);
        }
        return a;
    }

    public static void Mostrar(int[] a)
    {
        for (int i = 0; i < a.Length; i++)
        {
            Console.Write(a[i] + " ");
        }
        Console.WriteLine();
    }
    public static void Main(String[] args)
    {
        int[] a = [10, 7, 8, 9, 1, 5];
        Mostrar(a);
        OrdQuick(a, 0, a.Length - 1);
        Mostrar(a);
    }
}
