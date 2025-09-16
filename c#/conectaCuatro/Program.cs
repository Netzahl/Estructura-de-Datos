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

        for (int i = 0; i < 6; i++)
        {
            Console.WriteLine("-------------------------------");
            for (int j = 0; j < 7; j++)
            {
                Console.Write(" | ");
                Console.Write(tablero[i, j]);
            }
            Console.WriteLine(" | ");
        }
        Console.WriteLine("-------------------------------");
    }

    public static string[,] Colocar_ficha(string[,] tablero, string ficha)
    {
        int numero = 0;
        bool esValido = false;

        do
        {
            try
            {
                Console.Write("Ingresa un número entre 1 y 7: ");
                string entrada = Console.ReadLine();

                // Intentar convertir a entero
                numero = Convert.ToInt32(entrada);

                // Validar que esté en el rango correcto
                if (numero < 1 || numero > 7)
                {
                    throw new Exception("El número debe estar entre 1 y 7.");
                }

                esValido = true;
            }
            catch (FormatException)
            {
                Console.WriteLine("Error: Debes ingresar un número entero válido.");
            }
            catch (OverflowException)
            {
                Console.WriteLine("Error: El número es demasiado grande o pequeño.");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error: {ex.Message}");
            }


            switch (numero)
            {
                case 1:
                    for (int i = 5; i >= 0; i--)
                    {
                        if (tablero[i, 0] == " ")
                        {
                            tablero[i, 0] = ficha;
                            return tablero;
                        }
                    }
                    Console.WriteLine("Columna Llena, Elija otra columna");
                    esValido = false;
                    break;
                case 2:
                    for (int i = 5; i >= 0; i--)
                    {
                        if (tablero[i, 1] == " ")
                        {
                            tablero[i, 1] = ficha;
                            return tablero;
                        }
                    }
                    Console.WriteLine("Columna Llena, Elija otra columna");
                    esValido = false;
                    break;
                case 3:
                    for (int i = 5; i >= 0; i--)
                    {
                        if (tablero[i, 2] == " ")
                        {
                            tablero[i, 2] = ficha;
                            return tablero;
                        }
                    }
                    Console.WriteLine("Columna Llena, Elija otra columna");
                    esValido = false;
                    break;
                case 4:
                    for (int i = 5; i >= 0; i--)
                    {
                        if (tablero[i, 3] == " ")
                        {
                            tablero[i, 3] = ficha;
                            return tablero;
                        }
                    }
                    Console.WriteLine("Columna Llena, Elija otra columna");
                    esValido = false;
                    break;
                case 5:
                    for (int i = 5; i >= 0; i--)
                    {
                        if (tablero[i, 4] == " ")
                        {
                            tablero[i, 4] = ficha;
                            return tablero;
                        }
                    }
                    Console.WriteLine("Columna Llena, Elija otra columna");
                    esValido = false;
                    break;
                case 6:
                    for (int i = 5; i >= 0; i--)
                    {
                        if (tablero[i, 5] == " ")
                        {
                            tablero[i, 5] = ficha;
                            return tablero;
                        }
                    }
                    Console.WriteLine("Columna Llena, Elija otra columna");
                    esValido = false;
                    break;
                case 7:
                    for (int i = 5; i >= 0; i--)
                    {
                        if (tablero[i, 6] == " ")
                        {
                            tablero[i, 6] = ficha;
                            return tablero;
                        }
                    }
                    Console.WriteLine("Columna Llena, Elija otra columna");
                    esValido = false;
                    break;
                default:
                    Console.WriteLine("Ingrese de nuevo");
                    break;
            }
        } while (!esValido);
        return tablero;
    }

    public static void Juego_en_marcha(string[,] tablero)
    {
        int contador = 0;
        for (int h = 0; h < 42; h++)
        {
            //Verificacion de Filas
            for (int i = 0; i < 6; i++)
            {
                for (int j = 0; j < 4; j++)
                {
                    if (tablero[i, j] != " " && tablero[i, j] == tablero[i, j + 1] && tablero[i, j] == tablero[i, j + 2] && tablero[i, j] == tablero[i, j + 3])
                    {
                        if (tablero[i, j] == "X")
                        {
                            Console.WriteLine("¡¡¡¡ Ha ganado el jugador 1: 'X' !!!!");
                            return;
                        }
                        else
                        {
                            Console.WriteLine("¡¡¡¡ Ha ganado el jugador 2: 'O' !!!!");
                            return;
                        }
                    }
                }
            }

            //Verificacion de Columnas
            for (int i = 0; i < 7; i++)
            {
                for (int j = 0; j < 3; j++)
                {
                    if (tablero[j, i] != " " && tablero[j, i] == tablero[j + 1, i] && tablero[j, i] == tablero[j + 2, i] && tablero[j, i] == tablero[j + 3, i])
                    {
                        if (tablero[j, i] == "X")
                        {
                            Console.WriteLine("¡¡¡¡ Ha ganado el jugador 1: 'X' !!!!");
                            return;
                        }
                        else
                        {
                            Console.WriteLine("¡¡¡¡ Ha ganado el jugador 2: 'O' !!!!");
                            return;
                        }
                    }
                }
            }

            //Verificacion de diagonales
            for (int i = 0; i < 3; i++)
            {
                for (int j = 0; j < 4; j++)
                {
                    if (tablero[i, j] != " " && tablero[i, j] == tablero[i + 1, j + 1] && tablero[i, j] == tablero[i + 2, j + 2] && tablero[i, j] == tablero[i + 3, j + 3])
                    {
                        if (tablero[i, j] == "X")
                        {
                            Console.WriteLine("¡¡¡¡ Ha ganado el jugador 1: 'X' !!!!");
                            return;
                        }
                        else
                        {
                            Console.WriteLine("¡¡¡¡ Ha ganado el jugador 2: 'O' !!!!");
                            return;
                        }
                    }
                }
            }

            for (int i = 3; i < 6; i++)
            {
                for (int j = 0; j < 4; j++)
                {
                    if (tablero[i, j] != " " && tablero[i, j] == tablero[i - 1, j + 1] && tablero[i, j] == tablero[i - 2, j + 2] && tablero[i, j] == tablero[i - 3, j + 3])
                    {
                        if (tablero[i, j] == "X")
                        {
                            Console.WriteLine("¡¡¡¡ Ha ganado el jugador 1: 'X' !!!!");
                            return;
                        }
                        else
                        {
                            Console.WriteLine("¡¡¡¡ Ha ganado el jugador 2: 'O' !!!!");
                            return;
                        }
                    }
                }
            }

            if (contador == 42)
            {
                Console.WriteLine("Los jugadores han empatado!!!");
            }
            else
            {
                if (contador % 2 != 0)
                {
                    Console.WriteLine("Turno del jugador 1: 'X'\nElija la columna (1-7):");
                    tablero = Colocar_ficha(tablero, "X");
                    Dibujar_tablero(tablero);
                }
                else
                {
                    Console.WriteLine("Turno del jugador 2: 'O'\nElija la columna (1-7):");
                    tablero = Colocar_ficha(tablero, "O");
                    Dibujar_tablero(tablero);
                }
            }
            contador++;


        }
    }
    public static void Main(String[] args)
    {
        string[,] tablero = new string[6, 7];
        string op = "";
        Console.WriteLine("¡¡¡Conecta Cuatrooo!!!");
        Console.WriteLine("Instrucciones:\nColoca tus fichas en la columna que desees\npara conectar 4 de tus fichas de manera seguida\ncolumnas a elegir (1-7)");
        Console.WriteLine("\n | 1 | 2 | 3 | 4 | 5 | 6 | 7 |");
        for (int i = 0; i < 6; i++)
        {
            Console.WriteLine("-------------------------------");
            for (int j = 0; j < 7; j++)
            {
                Console.Write(" | ");
                Console.Write(" ");
            }
            Console.WriteLine(" | ");
        }
        Console.WriteLine("-------------------------------");
        
        do
        {
            Console.WriteLine("\nInicio del Juego!!\n");
            tablero = Inicializar_tablero(tablero);
            Dibujar_tablero(tablero);
            Juego_en_marcha(tablero);
            Console.WriteLine("Desea seguir jugando?\n| 1) Si | 2) No |");
            op = Console.ReadLine();
        } while (op == "1");
    }
}
