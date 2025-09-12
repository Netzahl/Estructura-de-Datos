using System;
using System.ComponentModel;

class Persona
{
    public string nombre;
    public int edad;

    public Persona()
    {
        nombre = "";
        edad = 0;
    }

    public void mostrarDatos()
    {
        Console.WriteLine($"Nombre: {nombre}, Edad:{edad}");
    }

}

class Program
{
    static void Main()
    {
        Persona[] personas = new Persona[3];
        personas[0] = new Persona();
        personas[0].nombre = "David";
        personas[0].edad = 19;
        personas[0].mostrarDatos();
    }
}
