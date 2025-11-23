const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function pregunta(texto) {
  return new Promise(resolve => {
    rl.question(texto, respuesta => {
      resolve(respuesta);
    });
  });
}

class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
    this.ant = null;
  }
}

let head = null;
let tail = null;

// 1. Insertar al principio
async function begInsert() {
  let item = parseInt(await pregunta("\nIngrese valor: "));
  let ptr = new Node(item);

  if (head === null) {
    head = ptr;
    tail = ptr;
    ptr.next = ptr;
    ptr.ant = ptr;
  } else {
    ptr.next = head;
    ptr.ant = tail;
    head.ant = ptr;
    tail.next = ptr;
    head = ptr;
  }

  console.log("Nodo insertado");
}

// 2. Insertar al final
async function lastInsert() {
  let item = parseInt(await pregunta("\nIngrese valor: "));
  let ptr = new Node(item);

  if (head === null) {
    head = ptr;
    tail = ptr;
    ptr.next = ptr;
    ptr.ant = ptr;
  } else {
    tail.next = ptr;
    head.ant = ptr;
    ptr.ant = tail;
    ptr.next = head;
    tail = ptr;
  }

  console.log("Nodo insertado");
}

// 3. Insertar después de ubicación
async function selectInsert() {
  let item = parseInt(await pregunta("\nIntroduzca el valor del elemento: "));
  let loc = parseInt(await pregunta("Introduce la ubicación después de la cual deseas ingresar: "));

  if (loc <= 0) {
    console.log("Ubicación no válida");
    return;
  }

  if (head === null) {
    console.log("No se puede insertar");
    return;
  }

  let ptr = new Node(item);
  let temp = head;

  for (let i = 1; i < loc; i++) {
    temp = temp.next;

    if (temp === head) {
      console.log("No se puede insertar");
      return;
    }
  }

  ptr.next = temp.next;
  ptr.ant = temp;
  temp.next = ptr;
  ptr.next.ant = ptr;

  if (ptr.next === head) {
    tail = ptr;
  }

  console.log("Nodo insertado");
}

// 4. Eliminar al inicio
function beginDelete() {
  if (head === null) {
    console.log("Lista vacía");
  } else if (head.next === head) {
    head = null;
    tail = null;
    console.log("Único nodo eliminado...");
  } else {
    let ptr = head;
    head = ptr.next;
    head.ant = tail;
    tail.next = head;
    console.log("Primer nodo eliminado...");
  }
}

// 5. Eliminar al final
function lastDelete() {
  if (head === null) {
    console.log("Lista vacía");
  } else if (tail.ant === tail) {
    head = null;
    tail = null;
    console.log("Único nodo eliminado...");
  } else {
    let ptr = tail;
    tail = tail.ant;
    tail.next = head;
    head.ant = tail;
    console.log("Último nodo eliminado...");
  }
}

// 6. Eliminar después de ubicación
async function selectDelete() {
  let loc = parseInt(await pregunta("\nIntroduce la ubicación después de la cual deseas eliminar: "));

  if (head === null) {
    console.log("Lista vacía, no se puede eliminar");
    return;
  }

  if (loc <= 0) {
    console.log("Ubicación inválida");
    return;
  }

  let ptr = head;
  let prev = null;

  for (let i = 0; i < loc; i++) {
    prev = ptr;
    ptr = ptr.next;

    if (ptr === head) {
      console.log("No se puede eliminar, ubicación no encontrada");
      return;
    }
  }

  prev.next = ptr.next;
  ptr.next.ant = prev;

  if (ptr.next === head) {
    tail = prev;
  }

  console.log(`Nodo eliminado en la posición ${loc + 1}`);
}

// 7. Buscar
async function search() {
  if (head === null) {
    console.log("Lista vacía");
    return;
  }

  let item = parseInt(await pregunta("\nIntroduce el elemento que deseas buscar: "));

  let ptr = head;
  let i = 0;
  let flag = false;

  do {
    if (ptr.data === item) {
      console.log(`Elemento encontrado en la ubicación ${i + 1}`);
      flag = true;
    }
    ptr = ptr.next;
    i++;
  } while (ptr !== head);

  if (!flag) {
    console.log("Elemento no encontrado");
  }
}

// 8. Mostrar
function display() {
  if (head === null) {
    console.log("Nada que imprimir");
    return;
  }

  console.log("\nImprimiendo valores...\n");
  let ptr = head;

  do {
    console.log(ptr.data);
    ptr = ptr.next;
  } while (ptr !== head);
}

// MENÚ PRINCIPAL
async function menu() {
  let choice = 0;

  while (choice !== 9) {
    console.log("\n********** Menú principal **********");
    console.log("1. Insertar al principio");
    console.log("2. Insertar al final");
    console.log("3. Insertar después de ubicación");
    console.log("4. Eliminar del principio");
    console.log("5. Eliminar desde el último");
    console.log("6. Eliminar después de la ubicación");
    console.log("7. Buscar un elemento");
    console.log("8. Mostrar");
    console.log("9. Salir");

    choice = parseInt(await pregunta("\nIngrese su opción: "));

    switch (choice) {
      case 1:
        await begInsert();
        break;
      case 2:
        await lastInsert();
        break;
      case 3:
        await selectInsert();
        break;
      case 4:
        beginDelete();
        break;
      case 5:
        lastDelete();
        break;
      case 6:
        await selectDelete();
        break;
      case 7:
        await search();
        break;
      case 8:
        display();
        break;
      case 9:
        console.log("Saliendo...");
        break;
      default:
        console.log("Opción inválida");
    }
  }

  rl.close();
}

// Ejecutar
menu();
