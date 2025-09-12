using System;

class Insertar
{
    public static void Main(string[] args)
    {
        Random rand = new Random();
        int numeroAdd = rand.Next(1, 50);
        int[] numeros = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
        int[] newnum = new int[10];
        int posicion = 5, j = 0;

        for (int i = 0; i < 10; i++)
        {
            if (i == posicion)
            {
                newnum[i] = numeroAdd;
                j++;
            }
            else
            {
                newnum[i] = numeros[i - j];
            }
        }

        for (int i = 0; i < 10; i++)
        {
            Console.WriteLine(newnum[i]);
        }

    }
}
