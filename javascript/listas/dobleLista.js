const readline = require("readline");

class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
    this.ant = null; // anterior
  }
}

let head = null;
let tail = null;

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function menu() {
  console.log("\n********** Menú principal **********");
  console.log("1. Insertar al principio");
  console.log("2. Insertar al final");
  console.log("3. Insertar después de ubicación");
  console.log("4. Eliminar del principio");
  console.log("5. Eliminar desde el último");
  console.log("6. Eliminar nodo después de la ubicación");
  console.log("7. Buscar un elemento");
  console.log("8. Mostrar");
  console.log("9. Salir");

  rl.question("\nIngrese su opción: ", (choice) => {
    switch (parseInt(choice)) {
      case 1: return begInsert();
      case 2: return lastInsert();
      case 3: return selectInsert();
      case 4: return beginDelete();
      case 5: return lastDelete();
      case 6: return selectDelete();
      case 7: return search();
      case 8: return display();
      case 9:
        rl.close();
        return;
      default:
        console.log("Opción inválida");
        return menu();
    }
  });
}

// INSERTAR AL INICIO
function begInsert() {
  rl.question("Ingrese valor: ", (value) => {
    const newNode = new Node(parseInt(value));

    newNode.next = head;
    newNode.ant = null;

    if (head !== null) {
      head.ant = newNode;
    } else {
      tail = newNode;
    }

    head = newNode;
    console.log("Nodo insertado al inicio");
    menu();
  });
}

// INSERTAR AL FINAL
function lastInsert() {
  rl.question("Ingrese valor: ", (value) => {
    const newNode = new Node(parseInt(value));

    if (head === null) {
      head = newNode;
      tail = newNode;
    } else {
      tail.next = newNode;
      newNode.ant = tail;
      tail = newNode;
    }

    console.log("Nodo insertado al final");
    menu();
  });
}

// INSERTAR DESPUÉS DE POSICIÓN
function selectInsert() {
  rl.question("Ingrese valor: ", (value) => {
    const item = parseInt(value);

    rl.question("Ingrese ubicación (posición): ", (loc) => {
      const position = parseInt(loc);

      if (position <= 0) {
        console.log("Ubicación no válida");
        return menu();
      }

      let temp = head;
      for (let i = 1; i < position; i++) {
        if (!temp) {
          console.log("No se puede insertar");
          return menu();
        }
        temp = temp.next;
      }

      if (!temp) {
        console.log("No se puede insertar");
        return menu();
      }

      const newNode = new Node(item);

      newNode.next = temp.next;
      newNode.ant = temp;

      if (temp.next !== null) {
        temp.next.ant = newNode;
      } else {
        tail = newNode;
      }

      temp.next = newNode;

      console.log("Nodo insertado");
      menu();
    });
  });
}

// ELIMINAR PRIMERO
function beginDelete() {
  if (head === null) {
    console.log("Lista vacía");
  } 
  else if (head.next === null) {
    head = null;
    tail = null;
    console.log("Único nodo eliminado");
  } 
  else {
    head = head.next;
    head.ant = null;
    console.log("Primer nodo eliminado");
  }
  menu();
}

// ELIMINAR ÚLTIMO
function lastDelete() {
  if (head === null) {
    console.log("Lista vacía");
  } 
  else if (tail.ant === null) {
    head = null;
    tail = null;
    console.log("Único nodo eliminado");
  } 
  else {
    tail = tail.ant;
    tail.next = null;
    console.log("Último nodo eliminado");
  }

  menu();
}

// ELIMINAR DESPUÉS DE POSICIÓN
function selectDelete() {
  rl.question("Ingrese posición: ", (value) => {
    const loc = parseInt(value);

    if (head === null) {
      console.log("Lista vacía");
      return menu();
    }

    if (loc <= 0) {
      console.log("La ubicación debe ser mayor que 0");
      return menu();
    }

    let ptr = head;
    let prev = null;

    for (let i = 0; i < loc; i++) {
      prev = ptr;
      ptr = ptr.next;

      if (ptr == null) {
        console.log("Ubicación no encontrada");
        return menu();
      }
    }

    prev.next = ptr.next;

    if (ptr.next !== null) {
      ptr.next.ant = prev;
    } else {
      tail = prev;
    }

    console.log("Nodo eliminado en la posición", loc + 1);
    menu();
  });
}

// BUSCAR
function search() {
  if (head === null) {
    console.log("Lista vacía");
    return menu();
  }

  rl.question("Ingrese valor a buscar: ", (value) => {
    const item = parseInt(value);

    let ptr = head;
    let pos = 1;
    let found = false;

    while (ptr !== null) {
      if (ptr.data === item) {
        console.log(`Elemento encontrado en la posición ${pos}`);
        found = true;
      }
      ptr = ptr.next;
      pos++;
    }

    if (!found) {
      console.log("Elemento no encontrado");
    }

    menu();
  });
}

// MOSTRAR
function display() {
  let ptr = head;

  if (ptr === null) {
    console.log("Nada que imprimir");
  } else {
    console.log("\nMostrando lista:");
    while (ptr !== null) {
      console.log(ptr.data);
      ptr = ptr.next;
    }
  }
  menu();
}

// Ejecutar
menu();
