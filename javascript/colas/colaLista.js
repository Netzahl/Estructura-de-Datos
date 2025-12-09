const readline = require('readline');

class Node {
    constructor() {
        this.data = 0;
        this.next = null;
    }
}

let head = null;
let tail = null;

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function insertar() {
    rl.question('\nIngrese el elemento: ', (input) => {
        const elemento = parseInt(input);
        
        const ptr = new Node();
        
        if (ptr == null) {
            console.log('\nDESBORDAMIENTO (OVERFLOW)\n');
            mostrarMenu();
            return;
        }
        
        if (head == null && tail == null) {
            head = tail = ptr;
        } else {
            tail.next = ptr;
            tail = ptr;
        }
        
        ptr.data = elemento;
        console.log('\nElemento insertado correctamente.\n');
        mostrarMenu();
    });
}

function eliminar() {
    if (head == null) {
        console.log('\nSUBDESBORDAMIENTO (UNDERFLOW)\n');
        mostrarMenu();
        return;
    }
    
    const elemento = head.data;
    
    if (head == tail) {
        head = tail = null;
    } else {
        head = head.next;
    }
    
    console.log('\nElemento eliminado: ' + elemento + '\n');
    mostrarMenu();
}

function mostrar() {
    let ptr = head;
    
    if (ptr == null) {
        console.log('\nNada que imprimir');
    } else {
        process.stdout.write('\nImprimiendo valores . . . . . . \n');
        while (ptr != null) {
            process.stdout.write(ptr.data.toString());
            if (ptr != tail) {
                process.stdout.write(' | ');
            }
            ptr = ptr.next;
        }
        console.log();
    }
    mostrarMenu();
}

function mostrarMenu() {
    console.log('\n****************** MENÚ PRINCIPAL ******************\n');
    console.log('====================================================\n');
    console.log('1. Insertar un elemento\n');
    console.log('2. Eliminar un elemento\n');
    console.log('3. Mostrar la cola\n');
    console.log('4. Salir\n');
    
    rl.question('Ingrese su opción: ', (opcion) => {
        const opt = parseInt(opcion);
        
        switch (opt) {
            case 1:
                insertar();
                break;
            case 2:
                eliminar();
                break;
            case 3:
                mostrar();
                break;
            case 4:
                console.log('\nSaliendo del programa...\n');
                rl.close();
                break;
            default:
                console.log('\nOpción inválida. Intente nuevamente.\n');
                mostrarMenu();
        }
    });
}

// Iniciar el programa
mostrarMenu();