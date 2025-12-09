const readline = require('readline');

const MAXSIZE = 5;
let queue = new Array(MAXSIZE);
let front = -1, rear = -1;

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function insertar() {
    rl.question('\nIngrese el elemento: ', (input) => {
        const elemento = parseInt(input);
        
        if (rear == MAXSIZE - 1) {
            console.log('\nDESBORDAMIENTO (OVERFLOW)\n');
            mostrarMenu();
            return;
        }
        
        if (front == -1 && rear == -1) {
            front = rear = 0;
        } else {
            rear++;
        }
        
        queue[rear] = elemento;
        console.log('\nElemento insertado correctamente.\n');
        mostrarMenu();
    });
}

function eliminar() {
    if (front == -1 || front > rear) {
        console.log('\nSUBDESBORDAMIENTO (UNDERFLOW)\n');
        mostrarMenu();
        return;
    }
    
    const elemento = queue[front];
    
    if (front == rear) {
        front = rear = -1;
    } else {
        front++;
    }
    
    console.log('\nElemento eliminado: ' + elemento + '\n');
    mostrarMenu();
}

function mostrar() {
    if (rear == -1 || front == -1 || front > rear) {
        console.log('\nLa cola está vacía.\n');
    } else {
        console.log('\nElementos en la cola:\n');
        for (let i = front; i <= rear; i++) {
            console.log(queue[i] + '\n');
        }
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