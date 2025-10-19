using System;
class Hashell
{
    public static void DisplayArr(int[] arr)
    {
        foreach (int x in arr)
        {
            Console.Write(x + " ");
        }
        Console.WriteLine();
    }

    public int Sort(int[] arr)
    {
        int size = arr.Length;
        int gapsize = size / 2;

        while (gapsize > 0)
        {
            for (int j = gapsize; j < size; j++)
            {
                int val = arr[j];
                int k = j;
                while (k >= gapsize && arr[k - gapsize] > val)
                {
                    arr[k] = arr[k - gapsize];
                    k -= gapsize;
                }
                arr[k] = val;
            }
            gapsize /= 2;
        }
        return 0;
    }
}

class Program
{
    static void Main(string[] args)
    {
        int[] arr = [36, 34, 43, 11, 15, 20, 28, 45, 25];
        Console.WriteLine("Arreglo desordenado: ");
        Hashell.DisplayArr(arr);
        Hashell obj = new Hashell();
        obj.Sort(arr);
        Console.WriteLine("Arreglo ordenado: ");
        Hashell.DisplayArr(arr);
    }
}