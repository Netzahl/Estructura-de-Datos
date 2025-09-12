using System;

class Recorrido
{
    public static void Main(string[] args)
    {
        Random rand = new Random();
        int[] num = new int[10];

        for (int i = 0; i < 10; i++)
        {
            num[i] = rand.Next(100) + 1;
        }

        for (int i = 0; i < 10; i++)
        {
            Console.WriteLine(num[i]);
        }
    }
}
