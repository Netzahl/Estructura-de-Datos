class Persona {
    String nombre;
    int edad;

    public Persona() {

        nombre = "";
        edad = 0;

    }

    public void mostrarDatos(){

        System.out.print("Nombre: "+nombre+", Edad: "+edad);

    }

}

public class datAbs {

    public static void main(String[] args) {

        Persona[] people = new Persona[3];
        people[0] = new Persona();
        people[0].nombre = "David";
        people[0].edad = 19;
        people[0].mostrarDatos(); 

    }
    
}
