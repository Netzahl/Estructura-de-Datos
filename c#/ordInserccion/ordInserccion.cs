using System.Reflection;
using System.Runtime.InteropServices;

class InsertionSort
{
    public static int[] InserccionSort(int[] a)
    {
        int temp = 0, j=0;
        for (int i = 1; i < a.Length; i++)
        {
            temp = a[i];
            j = i - 1;
            while (j >= 0 && temp < a[j])
            {
                a[j + 1] = a[j];
                j--;
            }
            a[j+1] = temp;
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
    public static void Main(string[] args)
    {
        int[] a = { 70, 15, 2, 51, 60 };
        PrintArr(a);
        a = InserccionSort(a);
        PrintArr(a);
    }
}