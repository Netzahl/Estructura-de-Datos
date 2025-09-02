#include <iostream>
#include <string>
using namespace std;

class Persona{
public:
    string nombre;
    int edad;

    Persona(){

        nombre = "Desconocido";
        edad = 0;

    }

    void mostrarDatos(){

        cout<<"Nombre: "<<nombre<<", Edad: "<<edad<<endl;

    }

};

int main(){

    Persona wey[3];

    wey[0].nombre = "David";
    wey[0].edad = 19;

    wey[0].mostrarDatos();

    return 0;

}