using System;
using System.Collections.Generic;

class BucketSort
{
    static void Insort(List<double> buckt)
    {
        for (int i = 0; i < buckt.Count; i++)
        {
            double val = buckt[i];
            int k = i - 1;
            while (k >= 0 && buckt[k] > val)
            {
                buckt[k + 1] = buckt[k];
                k--;
            }
            buckt[k + 1] = val;
        }
    }

    static void Bucket(double[] arr)
    {
        int s = arr.Length;
        List<double>[] bucketArr = new List<double>[s];

        for (int i = 0; i < s; i++)
        {
            bucketArr[i] = new List<double>();
        }

        foreach (double j in arr)
        {
            int bi = (int)(s * j);
            bucketArr[bi].Add(j);
        }

        foreach (var buckt in bucketArr)
        {
            Insort(buckt);
        }

        int idx = 0;
        foreach (var buckt in bucketArr)
        {
            foreach (double j in buckt)
            {
                arr[idx] = j;
                idx++;
            }
        }
    }

    static void Main()
    {
        double[] arr = [0.77, 0.16, 0.38, 0.25, 0.71, 0.93, 0.22, 0.11, 0.24, 0.67];

        Console.WriteLine("Antes de ordenar: ");
        Console.WriteLine(string.Join(" ", arr));
        Bucket(arr);
        Console.WriteLine("Despues de ordenar");
        Console.WriteLine(string.Join(" ", arr));
    }

}
