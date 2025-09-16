using System;

class ConectaCuatro
{
    public static string[,] Inicializar_tablero(string[,] tablero)
    {
        for (int i = 0; i < 6; i++)
        {
            for (int j = 0; j < 7; j++)
            {
                tablero[i, j] = " ";
            }
        }
        return tablero;
    }

    public static void Dibujar_tablero(string[,] tablero)
    {
        Console.WriteLine("-------------------------------------------------");
        for (int i = 0; i < 6; i++)
        {
            for (int j = 0; j < 7; j++)
            {
                console.write(" | ");
                console.write(tablero[i, j]);
            }
            Console.WriteLine("\n-------------------------------------------------");
        }
    }
    public static void Main(String[] args)
    {
        string[,] tablero = new string[6, 7];
        tablero = inicializar_tablero(tablero);
        Dibujar_tablero(tablero);
    }
}
