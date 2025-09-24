class Ord_Seleccion
{
    public static int[] SelectionSort(int[] a)
    {
        int small = 0, adicional = 0;
        for (int i = 0; i < a.Length; i++)
        {
            small = i;
            for (int j = i + 1; j < a.Length; j++)
            {
                if (a[small] > a[j])
                {
                    small = j;
                }
            }
            adicional = a[small];
            a[small] = a[i];
            a[i] = adicional;
        }
        return a;
    }

    public static void PrintArr(int[] a)
    {
        for (int i = 0; i < a.Length; i++)
        {
            Console.Write(a[i] + " ");
        }
        Console.WriteLine();
    }

    public static void Main(String[] args)
    {
        int[] a = { 65,26,13,23,12 };
        PrintArr(a);
        a = SelectionSort(a);
        PrintArr(a);
    }
}