class Persona{

    constructor(){
        this.nombre = "";
        this.edad=0;
    }
    mostrarDatos(){
        console.log(`Nombre: ${this.nombre}, Edad: ${this.edad}`);
    }

}

let personas = [new Persona(),new Persona(),new Persona()];

personas[0].nombre = "David";
personas[0].edad = 19;
personas[0].mostrarDatos();