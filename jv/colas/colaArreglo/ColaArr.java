import java.util.Scanner;

public class ColaArr {
    private static final int MAXSIZE = 5;
    private static int[] queue = new int[MAXSIZE];
    private static int front = -1, rear = -1;
    
    public static void insertar() {
        Scanner sc = new Scanner(System.in);
        int elemento;
        System.out.print("\nIngrese el elemento: ");
        elemento = sc.nextInt();
        
        if (rear == MAXSIZE - 1) {
            System.out.println("\nDESBORDAMIENTO (OVERFLOW)\n");
            return;
        }
        
        if (front == -1 && rear == -1) {
            front = rear = 0;
        } else {
            rear++;
        }
        
        queue[rear] = elemento;
        System.out.println("\nElemento insertado correctamente.\n");
    }
    
    public static void eliminar() {
        if (front == -1 || front > rear) {
            System.out.println("\nSUBDESBORDAMIENTO (UNDERFLOW)\n");
            return;
        }
        
        int elemento = queue[front];
        
        if (front == rear) {
            front = rear = -1;
        } else {
            front++;
        }
        
        System.out.println("\nElemento eliminado: " + elemento + "\n");
    }
    
    public static void mostrar() {
        if (rear == -1 || front == -1 || front > rear) {
            System.out.println("\nLa cola está vacía.\n");
        } else {
            System.out.println("\nElementos en la cola:\n");
            for (int i = front; i <= rear; i++) {
                System.out.println(queue[i] + "\n");
            }
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