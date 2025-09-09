using System;

class RecorridoMatriz
{
    static void Main()
    {

        int[,] matriz = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };

        Console.WriteLine("Recorrido por filas:");

        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                Console.Write(matriz[i, j] + " ");
            }

        }

        Console.WriteLine();
        Console.WriteLine("Recorrido por columnas:");

        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                Console.Write(matriz[j, i] + " ");
            }

        }

    }
}