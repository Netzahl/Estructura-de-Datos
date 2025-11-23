import java.util.Scanner;

class Node {
    int data;
    Node next;
    Node(int d) {
        data = d;
        next = null;
    }
}

public class CircularList {
    static Node head = null;
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        int choice;
        do {
            System.out.println("\n1.Insertar inicio \n2.Final \n3.Posición");
            System.out.println("4.Borrar inicio \n5.Borrar final");
            System.out.println("6.Borrar posición \n7.Buscar \n8.Mostrar \n9.Salir");
            choice = sc.nextInt();

            switch (choice) {
                case 1 -> begInsert();
                case 2 -> lastInsert();
                case 3 -> selectInsert();
                case 4 -> beginDelete();
                case 5 -> lastDelete();
                case 6 -> selectDelete();
                case 7 -> search();
                case 8 -> display();
            }

        } while (choice != 9);
    }

    static void begInsert() {
        System.out.print("Valor: ");
        int item = sc.nextInt();
        Node ptr = new Node(item);

        if (head == null) {
            head = ptr;
            ptr.next = head;
        } else {
            Node temp = head;
            while (temp.next != head) temp = temp.next;
            ptr.next = head;
            temp.next = ptr;
            head = ptr;
        }
    }

    static void lastInsert() {
        System.out.print("Valor: ");
        int item = sc.nextInt();
        Node ptr = new Node(item);

        if (head == null) {
            head = ptr;
            ptr.next = head;
        } else {
            Node temp = head;
            while (temp.next != head) temp = temp.next;
            temp.next = ptr;
            ptr.next = head;
        }
    }

    static void selectInsert() {
        System.out.print("Valor: ");
        int item = sc.nextInt();
        System.out.print("Posición: ");
        int loc = sc.nextInt();

        Node ptr = new Node(item);
        Node temp = head;

        for (int i = 1; i < loc; i++) {
            temp = temp.next;
            if (temp == head) return;
        }

        ptr.next = temp.next;
        temp.next = ptr;
    }

    static void beginDelete() {
        if (head == null) return;

        if (head.next == head) head = null;
        else {
            Node temp = head;
            while (temp.next != head) temp = temp.next;
            head = head.next;
            temp.next = head;
        }
    }

    static void lastDelete() {
        if (head == null) return;

        if (head.next == head) head = null;
        else {
            Node temp = head, prev = null;
            while (temp.next != head) {
                prev = temp;
                temp = temp.next;
            }
            prev.next = head;
        }
    }

    static void selectDelete() {
        System.out.print("Posición: ");
        int loc = sc.nextInt();

        Node temp = head, prev = null;

        for (int i = 1; i < loc; i++) {
            prev = temp;
            temp = temp.next;
            if (temp == head) return;
        }

        prev.next = temp.next;
    }

    static void search() {
        if (head == null) return;
        System.out.print("Buscar: ");
        int x = sc.nextInt();

        Node temp = head;
        int i = 1;

        do {
            if (temp.data == x)
                System.out.println("Encontrado en: " + i);

            temp = temp.next;
            i++;
        } while (temp != head);
    }

    static void display() {
        if (head == null) return;

        Node temp = head;
        do {
            System.out.println(temp.data);
            temp = temp.next;
        } while (temp != head);
    }
}
