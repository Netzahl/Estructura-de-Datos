class Bubble_Sort
{
    public static void Main(String[] args)
    {
        int[] numeros = { 33, 54, 66, 12, 64, 35, 47, 98, 5 };
        int adicional = 0;
        for (int i = 0; i < numeros.Length; i++)
        {
            Console.Write(numeros[i] + " ");
        }

        bool cambio = true;
        int j = numeros.Length;
        do
        {
            cambio = false;
            for (int i = 1; i < j; i++)
            {
                if (numeros[i - 1] > numeros[i])
                {
                    cambio = true;
                    adicional = numeros[i - 1];
                    numeros[i - 1] = numeros[i];
                    numeros[i] = adicional;
                }
            }
            j--;
        } while (cambio == true);

        Console.WriteLine(" ");
        for (int i = 0; i < numeros.Length; i++)
        {
            Console.Write(numeros[i] + " ");
        }

    }
}