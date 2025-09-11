using System;

class BusqLineal
{
    public static void Main(string[] args)
    {
        Random rand = new Random();
        int[] numeros = new int[10];
        int numeroBus = rand.Next(0, 20);
        int posic = 0;
        bool bandera = false;

        for (int i = 0; i < 10; i++)
        {
            numeros[i] = rand.Next(0, 20);
        }

        for (int i = 0; i < 10; i++)
        {
            if (numeros[i] == numeroBus)
            {
                bandera = true;
                posic = i + 1;
            }
        }

        if (bandera == true)
        {
            Console.WriteLine("El numero " + numeroBus + ", se encuentra en la posicion " + posic + " del array");
        }
        else
        {
            Console.WriteLine("El numero " + numeroBus + " no se encuentra dentro del array");
        }

    }
}
