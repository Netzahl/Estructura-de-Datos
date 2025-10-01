class OrdMerge
{

    public static void Merge(ref int[] a, int l, int m, int r)
    {
        int a1 = m - l + 1;
        int a2 = r - m;
        int[] L = new int[a1];
        int[] R = new int[a2];

        int i = l;
        int j = m + 1;

        for (int h = 0; h < a1; h++)
        {
            L[h] = a[i];
            i++;
        }

        for (int h = 0; h < a2; h++)
        {
            R[h] = a[j];
            j++;
        }

        i = 0;
        j = 0;
        int k = l;

        while (i < a1 && j < a2)
        {
            if (L[i] <= R[j])
            {
                a[k] = L[i];
                i++;
            }
            else
            {
                a[k] = R[j];
                j++;
            }
            k++;
        }

        while (i < a1)
        {
            a[k] = L[i];
            i++;
            k++;
        }

        while (j < a2)
        {
            a[k] = R[j];
            j++;
            k++;
        }
    }

    public static void MergeSort(ref int[] a, int l, int r)
    {
        int m;
        if (l < r)
        {
            m = l + (r - l) / 2;
            MergeSort(ref a, l, m);
            MergeSort(ref a, m + 1, r);
            Merge(ref a, l, m, r);
        }
    }

    public static void Show(in int[] a)
    {
        foreach (var x in a)
        {
            Console.Write(x + " ");
        }
        Console.WriteLine();
    }

    public static void Main(String[] args)
    {
        int[] a = [45, 67, 12, 5, 89, 4, 27, 48, 65, 19, 75];
        int tamaño = 0;
        tamaño = a.Length;

        Console.WriteLine("Antes de ordenar: ");
        Show(in a);
        MergeSort(ref a, 0, tamaño - 1);
        Console.WriteLine("Despues de ordenar: ");
        Show(in a);
    }
}