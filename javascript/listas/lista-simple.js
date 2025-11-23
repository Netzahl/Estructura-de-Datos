const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}

let head = null;

// ========== INSERTAR AL INICIO ==========
function begInsert(item) {
  let newNode = new Node(item);
  newNode.next = head;
  head = newNode;
  console.log("\nNodo insertado al inicio");
}

// ========== INSERTAR AL FINAL ==========
function lastInsert(item) {
  let newNode = new Node(item);

  if (head === null) {
    head = newNode;
  } else {
    let temp = head;
    while (temp.next !== null) {
      temp = temp.next;
    }
    temp.next = newNode;
  }

  console.log("\nNodo insertado al final");
}

// ========== INSERTAR EN POSICIÓN ==========
function selectInsert(item, loc) {
  if (loc <= 0) {
    console.log("\nUbicación no válida");
    return;
  }

  let newNode = new Node(item);

  if (head === null) {
    console.log("\nNo se puede insertar. Lista vacía");
    return;
  }

  let temp = head;

  for (let i = 1; i < loc; i++) {
    temp = temp.next;
    if (temp === null) {
      console.log("\nNo se puede insertar. Ubicación no encontrada");
      return;
    }
  }

  newNode.next = temp.next;
  temp.next = newNode;
  console.log("\nNodo insertado");
}

// ========== ELIMINAR AL INICIO ==========
function beginDelete() {
  if (head === null) {
    console.log("\nLa lista está vacía");
    return;
  }

  head = head.next;
  console.log("\nPrimer nodo eliminado");
}

// ========== ELIMINAR AL FINAL ==========
function lastDelete() {
  if (head === null) {
    console.log("\nLa lista está vacía");
    return;
  }

  if (head.next === null) {
    head = null;
    console.log("\nSe eliminó el único nodo");
    return;
  }

  let ptr = head;
  let prev = null;

  while (ptr.next !== null) {
    prev = ptr;
    ptr = ptr.next;
  }

  prev.next = null;
  console.log("\nÚltimo nodo eliminado");
}

// ========== ELIMINAR EN POSICIÓN ==========
function selectDelete(loc) {
  if (head === null) {
    console.log("\nLista vacía");
    return;
  }

  if (loc <= 0) {
    console.log("\nUbicación no válida");
    return;
  }

  let ptr = head;
  let prev = null;

  for (let i = 0; i < loc; i++) {
    prev = ptr;
    ptr = ptr.next;

    if (ptr === null) {
      console.log("\nNo se puede eliminar. Ubicación no encontrada");
      return;
    }
  }

  prev.next = ptr.next;
  console.log(`\nNodo eliminado en posición ${loc + 1}`);
}

// ========== BUSCAR ==========
function search(item) {
  if (head === null) {
    console.log("\nLista vacía");
    return;
  }

  let ptr = head;
  let i = 0;
  let found = false;

  while (ptr !== null) {
    if (ptr.data === item) {
      console.log(`\nElemento encontrado en la posición ${i + 1}`);
      found = true;
    }
    ptr = ptr.next;
    i++;
  }

  if (!found) {
    console.log("\nElemento no encontrado");
  }
}

// ========== MOSTRAR ==========
function display() {
  if (head === null) {
    console.log("\nNada que imprimir");
    return;
  }

  let ptr = head;
  console.log("\nImprimiendo valores:\n");

  while (ptr !== null) {
    console.log(ptr.data);
    ptr = ptr.next;
  }
}

// ========== MENÚ ==========
function menu() {
  console.log("\n********** Menú principal **********");
  console.log("1. Insertar al principio");
  console.log("2. Insertar al final");
  console.log("3. Insertar en posición");
  console.log("4. Eliminar del principio");
  console.log("5. Eliminar del final");
  console.log("6. Eliminar después de posición");
  console.log("7. Buscar");
  console.log("8. Mostrar");
  console.log("9. Salir\n");

  rl.question("Elige una opción: ", function (choice) {

    switch (parseInt(choice)) {
      case 1:
        rl.question("Ingrese el valor: ", val => {
          begInsert(parseInt(val));
          menu();
        });
        break;

      case 2:
        rl.question("Ingrese el valor: ", val => {
          lastInsert(parseInt(val));
          menu();
        });
        break;

      case 3:
        rl.question("Ingrese valor: ", val => {
          rl.question("Ingrese ubicación: ", loc => {
            selectInsert(parseInt(val), parseInt(loc));
            menu();
          });
        });
        break;

      case 4:
        beginDelete();
        menu();
        break;

      case 5:
        lastDelete();
        menu();
        break;

      case 6:
        rl.question("Ingrese ubicación: ", loc => {
          selectDelete(parseInt(loc));
          menu();
        });
        break;

      case 7:
        rl.question("Ingrese valor a buscar: ", val => {
          search(parseInt(val));
          menu();
        });
        break;

      case 8:
        display();
        menu();
        break;

      case 9:
        console.log("\nSaliendo...");
        rl.close();
        break;

      default:
        console.log("\nOpción no válida...");
        menu();
    }
  });
}

// INICIAR PROGRAMA
menu();
