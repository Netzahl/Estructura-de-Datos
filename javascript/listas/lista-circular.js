const readline = require('readline');

class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

let head = null;

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function menu() {
    console.log("\n********** Menú principal **********");
    console.log("1. Insertar al principio");
    console.log("2. Insertar al final");
    console.log("3. Insertar en posición");
    console.log("4. Eliminar del principio");
    console.log("5. Eliminar del final");
    console.log("6. Eliminar nodo después de la ubicación");
    console.log("7. Buscar un elemento");
    console.log("8. Mostrar");
    console.log("9. Salir");

    rl.question("\nIngrese su opción: ", answer => {
        const choice = parseInt(answer);

        switch (choice) {
            case 1: begInsert(); break;
            case 2: lastInsert(); break;
            case 3: selectInsert(); break;
            case 4: beginDelete(); break;
            case 5: lastDelete(); break;
            case 6: selectDelete(); break;
            case 7: search(); break;
            case 8: display(); break;
            case 9:
                console.log("Saliendo...");
                rl.close();
                return;
            default:
                console.log("Opción no válida");
                menu();
        }
    });
}

// 1. Insertar al inicio
function begInsert() {
    rl.question("Ingrese valor: ", value => {
        const item = parseInt(value);
        const newNode = new Node(item);

        if (head === null) {
            head = newNode;
            newNode.next = head;
        } else {
            let temp = head;
            while (temp.next !== head) {
                temp = temp.next;
            }
            newNode.next = head;
            temp.next = newNode;
            head = newNode;
        }

        console.log("Nodo insertado al inicio");
        menu();
    });
}

// 2. Insertar al final
function lastInsert() {
    rl.question("Ingrese valor: ", value => {
        const item = parseInt(value);
        const newNode = new Node(item);

        if (head === null) {
            head = newNode;
            newNode.next = head;
        } else {
            let temp = head;
            while (temp.next !== head) {
                temp = temp.next;
            }
            temp.next = newNode;
            newNode.next = head;
        }

        console.log("Nodo insertado al final");
        menu();
    });
}

// 3. Insertar después de una ubicación
function selectInsert() {
    rl.question("Ingrese el valor a insertar: ", value => {
        const item = parseInt(value);
        const newNode = new Node(item);

        rl.question("Ingrese la posición después de la cual insertar: ", locStr => {
            const loc = parseInt(locStr);

            if (head === null || loc <= 0) {
                console.log("No se puede insertar");
                menu();
                return;
            }

            let temp = head;

            for (let i = 1; i < loc; i++) {
                temp = temp.next;
                if (temp === head) {
                    console.log("Ubicación fuera de rango");
                    menu();
                    return;
                }
            }

            newNode.next = temp.next;
            temp.next = newNode;

            console.log("Nodo insertado");
            menu();
        });
    });
}

// 4. Eliminar al inicio
function beginDelete() {
    if (head === null) {
        console.log("Lista vacía");
        menu();
        return;
    }

    if (head.next === head) {
        head = null;
    } else {
        let temp = head;
        while (temp.next !== head) {
            temp = temp.next;
        }
        head = head.next;
        temp.next = head;
    }

    console.log("Primer nodo eliminado");
    menu();
}

// 5. Eliminar al final
function lastDelete() {
    if (head === null) {
        console.log("Lista vacía");
        menu();
        return;
    }

    if (head.next === head) {
        head = null;
        console.log("Se eliminó el único nodo de la lista");
        menu();
        return;
    }

    let ptr = head;
    let prev = null;

    while (ptr.next !== head) {
        prev = ptr;
        ptr = ptr.next;
    }

    prev.next = head;
    console.log("Último nodo eliminado");
    menu();
}

// 6. Eliminar después de una posición
function selectDelete() {
    rl.question("Ingrese posición después de la cual desea eliminar: ", locStr => {
        const loc = parseInt(locStr);

        if (head === null || loc <= 0) {
            console.log("Lista vacía o posición inválida");
            menu();
            return;
        }

        let ptr1 = head;
        let ptr = head.next;

        for (let i = 2; i < loc; i++) {
            ptr1 = ptr;
            ptr = ptr.next;

            if (ptr === head) {
                console.log("Ubicación fuera de los límites");
                menu();
                return;
            }
        }

        if (ptr === head) {
            console.log("Ubicación fuera de los límites");
            menu();
            return;
        }

        ptr1.next = ptr.next;
        console.log(`Nodo eliminado en la posición ${loc + 1}`);
        menu();
    });
}

// 7. Buscar elemento
function search() {
    if (head === null) {
        console.log("Lista vacía");
        menu();
        return;
    }

    rl.question("Ingrese el elemento a buscar: ", val => {
        const item = parseInt(val);

        let ptr = head;
        let i = 1;
        let found = false;

        do {
            if (ptr.data === item) {
                console.log(`Elemento encontrado en la posición ${i}`);
                found = true;
            }
            ptr = ptr.next;
            i++;
        } while (ptr !== head);

        if (!found) {
            console.log("Elemento no encontrado");
        }

        menu();
    });
}

// 8. Mostrar lista
function display() {
    if (head === null) {
        console.log("Nada que imprimir");
        menu();
        return;
    }

    let ptr = head;

    console.log("\nMostrando lista circular:");
    do {
        console.log(ptr.data);
        ptr = ptr.next;
    } while (ptr !== head);

    menu();
}

// Iniciar programa
menu();
