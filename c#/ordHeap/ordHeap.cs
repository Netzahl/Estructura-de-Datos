class OrdMerge
{

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

    public static void Main(String[] args)
    {
        int[] a = [12, 94, 32, 5, 48, 64, 26, 57];
        int tamaño = a.Length;
        Console.WriteLine("Antes de ordenar: ");
        Show(a);
        HeapSort(ref a,tamaño-1);
        Console.WriteLine("Despues de ordenar: ");
        Show(a);
    }
}
