import java.util.Scanner;

class Node {
    int data;
    Node next = null;
}

public class ColaList {
    private static Node head = null;
    private static Node tail = null;
    
    public static void insertar() {
        Scanner sc = new Scanner(System.in);
        int elemento;
        
        System.out.print("\nIngrese el elemento: ");
        elemento = sc.nextInt();
        
        Node ptr = new Node();
        
        if (ptr == null) {
            System.out.println("\nDESBORDAMIENTO (OVERFLOW)\n");
            return;
        }
        
        if (head == null && tail == null) {
            head = tail = ptr;
        } else {
            tail.next = ptr;
            tail = ptr;
        }
        
        ptr.data = elemento;
        System.out.println("\nElemento insertado correctamente.\n");
    }
    
    public static void eliminar() {
        if (head == null) {
            System.out.println("\nSUBDESBORDAMIENTO (UNDERFLOW)\n");
            return;
        }
        
        int elemento = head.data;
        
        if (head == tail) {
            head = tail = null;
        } else {
            head = head.next;
        }
        
        System.out.println("\nElemento eliminado: " + elemento + "\n");
    }
    
    public static void mostrar() {
        Node ptr = head;
        
        if (ptr == null) {
            System.out.println("\nNada que imprimir");
        } else {
            System.out.println("\nImprimiendo valores . . . . . . \n");
            while (ptr != null) {
                System.out.print(ptr.data);
                if (ptr != tail) {
                    System.out.print(" | ");
                }
                ptr = ptr.next;
            }
            System.out.println();
        }
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int opcion = 0;
        
        while (opcion != 4) {
            System.out.println("\n****************** MENÚ PRINCIPAL ******************\n");
            System.out.println("====================================================\n");
            System.out.println("1. Insertar un elemento\n");
            System.out.println("2. Eliminar un elemento\n");
            System.out.println("3. Mostrar la cola\n");
            System.out.println("4. Salir\n");
            System.out.print("Ingrese su opción: ");
            opcion = sc.nextInt();
            
            switch (opcion) {
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
                    System.out.println("\nSaliendo del programa...\n");
                    break;
                default:
                    System.out.println("\nOpción inválida. Intente nuevamente.\n");
            }
        }
        
        sc.close();
    }
}