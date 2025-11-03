using System;
using System.Linq;

class RadixSort
{
    static void CountingSort(int[] arr, int exp)
    {
        int n = arr.Length;
        int[] output = new int[n];
        int[] count = new int[10];
        
        // Contar ocurrencias
        for (int i = 0; i < n; i++)
        {
            count[(arr[i] / exp) % 10]++;
        }
        
        // Posiciones acumulativas
        for (int i = 1; i < 10; i++)
        {
            count[i] += count[i - 1];
        }
        
        // Construir array de salida
        for (int i = n - 1; i >= 0; i--)
        {
            output[count[(arr[i] / exp) % 10] - 1] = arr[i];
            count[(arr[i] / exp) % 10]--;
        }
        
        // Copiar a array original
        for (int i = 0; i < n; i++)
        {
            arr[i] = output[i];
        }
    }
    
    static void RadixSortAlgorithm(int[] arr)
    {
        // Encontrar el máximo
        int max = arr.Max();
        
        // Aplicar counting sort para cada dígito
        for (int exp = 1; max / exp > 0; exp *= 10)
        {
            CountingSort(arr, exp);
        }
    }
    
    static void Main(string[] args)
    {
        int[] arr = { 170, 45, 75, 90, 802, 24, 2, 66 };
        
        Console.WriteLine("Array original: " + string.Join(", ", arr));
        RadixSortAlgorithm(arr);
        Console.WriteLine("Array ordenado: " + string.Join(", ", arr));
    }
}