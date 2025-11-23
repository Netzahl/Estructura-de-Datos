import java.util.Scanner;

class Node {
    int data;
    Node next;
    Node ant;

    public Node(int data) {
        this.data = data;
        this.next = null;
        this.ant = null;
    }
}

public class ListaDoble {

    static Node head = null;
    static Node tail = null;
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        int choice = 0;

        while (choice != 9) {
            System.out.println("\n********** Menú principal **********");
            System.out.println("1. Insertar al principio");
            System.out.println("2. Insertar al final");
            System.out.println("3. Insertar después de una ubicación");
            System.out.println("4. Eliminar del principio");
            System.out.println("5. Eliminar desde el último");
            System.out.println("6. Eliminar nodo después de una ubicación");
            System.out.println("7. Buscar un elemento");
            System.out.println("8. Mostrar");
            System.out.println("9. Salir");
            System.out.print("\nIngrese su opción: ");

            choice = sc.nextInt();

            switch (choice) {
                case 1:
                    begInsert();
                    break;
                case 2:
                    lastInsert();
                    break;
                case 3:
                    selectInsert();
                    break;
                case 4:
                    beginDelete();
                    break;
                case 5:
                    lastDelete();
                    break;
                case 6:
                    selectDelete();
                    break;
                case 7:
                    search();
                    break;
                case 8:
                    display();
                    break;
                case 9:
                    System.out.println("Saliendo...");
                    break;
                default:
                    System.out.println("Opción inválida...");
            }
        }
    }

    // INSERTAR AL INICIO
    public static void begInsert() {
        System.out.print("\nIngrese valor: ");
        int item = sc.nextInt();

        Node newNode = new Node(item);

        newNode.next = head;
        newNode.ant = null;

        if (head != null) {
            head.ant = newNode;
        } else {
            tail = newNode;
        }

        head = newNode;
        System.out.println("Nodo insertado al inicio");
    }

    // INSERTAR AL FINAL
    public static void lastInsert() {
        System.out.print("\nIngrese valor: ");
        int item = sc.nextInt();

        Node newNode = new Node(item);

        if (head == null) {
            head = newNode;
            tail = newNode;
        } else {
            tail.next = newNode;
            newNode.ant = tail;
            tail = newNode;
        }

        System.out.println("Nodo insertado al final");
    }

    // INSERTAR DESPUÉS DE UNA POSICIÓN
    public static void selectInsert() {
        System.out.print("\nIngrese el valor: ");
        int item = sc.nextInt();

        System.out.print("Ingrese la ubicación: ");
        int loc = sc.nextInt();

        if (loc <= 0) {
            System.out.println("Ubicación no válida");
            return;
        }

        Node temp = head;

        if (temp == null) {
            System.out.println("No se puede insertar");
            return;
        }

        for (int i = 1; i < loc; i++) {
            temp = temp.next;
            if (temp == null) {
                System.out.println("No se puede insertar");
                return;
            }
        }

        Node newNode = new Node(item);

        newNode.next = temp.next;
        newNode.ant = temp;

        if (temp.next != null) {
            temp.next.ant = newNode;
        } else {
            tail = newNode;
        }

        temp.next = newNode;

        System.out.println("Nodo insertado");
    }

    // ELIMINAR DEL INICIO
    public static void beginDelete() {
        if (head == null) {
            System.out.println("Lista vacía");
        } 
        else if (head.next == null) {
            head = null;
            tail = null;
            System.out.println("Único nodo eliminado");
        } 
        else {
            head = head.next;
            head.ant = null;
            System.out.println("Primer nodo eliminado");
        }
    }

    // ELIMINAR DEL FINAL
    public static void lastDelete() {
        if (head == null) {
            System.out.println("Lista vacía");
        } 
        else if (tail.ant == null) {
            head = null;
            tail = null;
            System.out.println("Único nodo eliminado");
        } 
        else {
            tail = tail.ant;
            tail.next = null;
            System.out.println("Último nodo eliminado");
        }
    }

    // ELIMINAR DESPUÉS DE UNA UBICACIÓN
    public static void selectDelete() {
        System.out.print("\nIngrese ubicación: ");
        int loc = sc.nextInt();

        if (head == null) {
            System.out.println("Lista vacía");
            return;
        }

        if (loc <= 0) {
            System.out.println("Ubicación inválida");
            return;
        }

        Node ptr = head;
        Node prev = null;

        for (int i = 0; i < loc; i++) {
            prev = ptr;
            ptr = ptr.next;

            if (ptr == null) {
                System.out.println("Ubicación no encontrada");
                return;
            }
        }

        prev.next = ptr.next;

        if (ptr.next != null) {
            ptr.next.ant = prev;
        } else {
            tail = prev;
        }

        System.out.println("Nodo eliminado en ubicación: " + (loc + 1));
    }

    // BUSCAR UN ELEMENTO
    public static void search() {
        if (head == null) {
            System.out.println("Lista vacía");
            return;
        }

        System.out.print("\nIngrese elemento a buscar: ");
        int item = sc.nextInt();

        Node ptr = head;
        int pos = 1;
        boolean found = false;

        while (ptr != null) {
            if (ptr.data == item) {
                System.out.println("Elemento encontrado en la posición " + pos);
                found = true;
            }
            ptr = ptr.next;
            pos++;
        }

        if (!found) {
            System.out.println("Elemento no encontrado");
        }
    }

    // MOSTRAR LISTA
    public static void display() {
        Node ptr = head;

        if (ptr == null) {
            System.out.println("Nada que imprimir");
        } else {
            System.out.println("\nImprimiendo valores...");
            while (ptr != null) {
                System.out.println(ptr.data);
                ptr = ptr.next;
            }
        }
    }
}
