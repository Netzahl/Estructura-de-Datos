import java.util.Scanner;

public class ListaDobleCircular {

    static class Node {
        int data;
        Node next;
        Node ant;

        Node(int data) {
            this.data = data;
            this.next = null;
            this.ant = null;
        }
    }

    static Node head = null;
    static Node tail = null;
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {

        int choice = 0;

        while (choice != 9) {
            System.out.println("\n********** Menú principal **********");
            System.out.println("1. Insertar al principio");
            System.out.println("2. Insertar al final");
            System.out.println("3. Insertar después de una posición");
            System.out.println("4. Eliminar del principio");
            System.out.println("5. Eliminar desde el último");
            System.out.println("6. Eliminar después de una posición");
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
                    System.exit(0);
                default:
                    System.out.println("\nIntroduzca una opción válida...");
            }
        }
    }

    static void begInsert() {
        System.out.print("\nIngrese valor: ");
        int item = sc.nextInt();

        Node ptr = new Node(item);

        if (head == null) {
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

        System.out.println("\nNodo insertado");
    }

    static void lastInsert() {
        System.out.print("\nIngrese valor: ");
        int item = sc.nextInt();

        Node ptr = new Node(item);

        if (head == null) {
            head = ptr;
            tail = ptr;
            ptr.next = ptr;
            ptr.ant = ptr;
        } else {
            tail.next = ptr;
            ptr.ant = tail;
            ptr.next = head;
            head.ant = ptr;
            tail = ptr;
        }

        System.out.println("\nNodo insertado");
    }

    static void selectInsert() {
        System.out.print("\nIntroduzca el valor del elemento: ");
        int item = sc.nextInt();

        System.out.print("\nIntroduzca la posición después de la cual desea insertar: ");
        int loc = sc.nextInt();

        if (loc <= 0) {
            System.out.println("\nUbicación no válida");
            return;
        }

        if (head == null) {
            System.out.println("\nNo se puede insertar, lista vacía");
            return;
        }

        Node ptr = new Node(item);
        Node temp = head;

        for (int i = 1; i < loc; i++) {
            temp = temp.next;
            if (temp == head) {
                System.out.println("\nUbicación no encontrada");
                return;
            }
        }

        ptr.next = temp.next;
        ptr.ant = temp;
        temp.next.ant = ptr;
        temp.next = ptr;

        if (temp == tail) {
            tail = ptr;
        }

        System.out.println("\nNodo insertado");
    }

    static void beginDelete() {
        if (head == null) {
            System.out.println("\nLa lista está vacía");
        } else if (head.next == head) {
            head = null;
            tail = null;
            System.out.println("\nÚnico nodo eliminado...");
        } else {
            head = head.next;
            head.ant = tail;
            tail.next = head;
            System.out.println("\nPrimer nodo eliminado...");
        }
    }

    static void lastDelete() {
        if (head == null) {
            System.out.println("\nLa lista está vacía");
        } else if (head.next == head) {
            head = null;
            tail = null;
            System.out.println("\nÚnico nodo eliminado...");
        } else {
            tail = tail.ant;
            tail.next = head;
            head.ant = tail;
            System.out.println("\nÚltimo nodo eliminado...");
        }
    }

    static void selectDelete() {
        if (head == null) {
            System.out.println("\nLista vacía, no se puede eliminar");
            return;
        }

        System.out.print("\nIntroduzca la posición después de la cual desea eliminar: ");
        int loc = sc.nextInt();

        if (loc <= 0) {
            System.out.println("\nUbicación no válida");
            return;
        }

        Node ptr = head;
        Node prev = null;

        for (int i = 0; i < loc; i++) {
            prev = ptr;
            ptr = ptr.next;

            if (ptr == head) {
                System.out.println("\nUbicación no encontrada");
                return;
            }
        }

        prev.next = ptr.next;
        ptr.next.ant = prev;

        if (ptr == tail) {
            tail = prev;
        }

        System.out.println("\nNodo eliminado");
    }

    static void search() {
        if (head == null) {
            System.out.println("\nLista vacía");
            return;
        }

        System.out.print("\nIntroduce el elemento que deseas buscar: ");
        int item = sc.nextInt();

        Node temp = head;
        int pos = 1;
        boolean found = false;

        do {
            if (temp.data == item) {
                System.out.println("\nElemento encontrado en la posición: " + pos);
                found = true;
            }
            temp = temp.next;
            pos++;
        } while (temp != head);

        if (!found) {
            System.out.println("\nElemento no encontrado");
        }
    }

    static void display() {
        if (head == null) {
            System.out.println("\nNada que imprimir");
            return;
        }

        System.out.println("\nMostrando valores de la lista:");

        Node temp = head;

        do {
            System.out.println(temp.data);
            temp = temp.next;
        } while (temp != head);
    }
}
