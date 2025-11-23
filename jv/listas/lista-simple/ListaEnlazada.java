import java.util.Scanner;

class Node {
    int data;
    Node next;

    Node(int data) {
        this.data = data;
        this.next = null;
    }
}

public class ListaEnlazada {

    static Node head = null;
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {

        int choice = 0;

        while (choice != 9) {
            System.out.println("\n********** Menú principal **********");
            System.out.println("1. Insertar al principio");
            System.out.println("2. Insertar al final");
            System.out.println("3. Insertar en posición");
            System.out.println("4. Eliminar del principio");
            System.out.println("5. Eliminar del final");
            System.out.println("6. Eliminar después de una posición");
            System.out.println("7. Buscar");
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
                    System.out.println("\nSaliendo...");
                    break;

                default:
                    System.out.println("\nIntroduzca una opción válida...");
            }
        }
    }

    // ========== INSERTAR AL INICIO ==========
    public static void begInsert() {
        System.out.print("\nIngrese valor: ");
        int item = sc.nextInt();

        Node newNode = new Node(item);
        newNode.next = head;
        head = newNode;

        System.out.println("Nodo insertado al inicio");
    }

    // ========== INSERTAR AL FINAL ==========
    public static void lastInsert() {
        System.out.print("\nIngrese valor: ");
        int item = sc.nextInt();

        Node newNode = new Node(item);

        if (head == null) {
            head = newNode;
        } else {
            Node temp = head;

            while (temp.next != null) {
                temp = temp.next;
            }

            temp.next = newNode;
        }

        System.out.println("Nodo insertado al final");
    }

    // ========== INSERTAR EN UNA POSICIÓN ==========
    public static void selectInsert() {
        System.out.print("\nIngrese valor: ");
        int item = sc.nextInt();

        System.out.print("Ingrese ubicación: ");
        int loc = sc.nextInt();

        if (loc <= 0) {
            System.out.println("Ubicación no válida");
            return;
        }

        if (head == null) {
            System.out.println("Lista vacía, no se puede insertar");
            return;
        }

        Node newNode = new Node(item);
        Node temp = head;

        for (int i = 1; i < loc; i++) {
            temp = temp.next;

            if (temp == null) {
                System.out.println("No se puede insertar. Posición no encontrada");
                return;
            }
        }

        newNode.next = temp.next;
        temp.next = newNode;

        System.out.println("Nodo insertado correctamente");
    }

    // ========== ELIMINAR AL INICIO ==========
    public static void beginDelete() {
        if (head == null) {
            System.out.println("La lista está vacía");
            return;
        }

        head = head.next;
        System.out.println("Primer nodo eliminado");
    }

    // ========== ELIMINAR AL FINAL ==========
    public static void lastDelete() {
        if (head == null) {
            System.out.println("La lista está vacía");
            return;
        }

        if (head.next == null) {
            head = null;
            System.out.println("Se eliminó el único nodo");
            return;
        }

        Node ptr = head;
        Node prev = null;

        while (ptr.next != null) {
            prev = ptr;
            ptr = ptr.next;
        }

        prev.next = null;
        System.out.println("Último nodo eliminado");
    }

    // ========== ELIMINAR DESPUÉS DE POSICIÓN ==========
    public static void selectDelete() {
        System.out.print("\nIngrese ubicación: ");
        int loc = sc.nextInt();

        if (head == null) {
            System.out.println("Lista vacía, no se puede eliminar");
            return;
        }

        if (loc <= 0) {
            System.out.println("Ubicación no válida");
            return;
        }

        Node ptr = head;
        Node prev = null;

        for (int i = 0; i < loc; i++) {
            prev = ptr;
            ptr = ptr.next;

            if (ptr == null) {
                System.out.println("Ubicación no encontrada, no se puede eliminar");
                return;
            }
        }

        prev.next = ptr.next;
        System.out.println("Nodo eliminado en la posición " + (loc + 1));
    }

    // ========== BUSCAR ==========
    public static void search() {
        if (head == null) {
            System.out.println("Lista vacía");
            return;
        }

        System.out.print("Ingrese el valor a buscar: ");
        int item = sc.nextInt();

        Node temp = head;
        int pos = 1;
        boolean found = false;

        while (temp != null) {
            if (temp.data == item) {
                System.out.println("Elemento encontrado en la posición " + pos);
                found = true;
            }
            temp = temp.next;
            pos++;
        }

        if (!found) {
            System.out.println("Elemento no encontrado");
        }
    }

    // ========== MOSTRAR ==========
    public static void display() {
        if (head == null) {
            System.out.println("Nada que mostrar");
            return;
        }

        Node temp = head;
        System.out.println("\nImprimiendo valores:");

        while (temp != null) {
            System.out.println(temp.data);
            temp = temp.next;
        }
    }
}
