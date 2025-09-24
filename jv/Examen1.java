import java.util.Scanner;
public class Examen1{
    
    public static int[] matriz(){
        int a[] = new int[10]; 
        Scanner scan = new Scanner(System.in);

        for (int idx = 0; idx < a.length; idx++) {
            System.err.println("Dame el numero " + (idx+1) + " del array: ");
            a[idx] = scan.nextInt();
        }
        return a;
    }

    public static void mostrar(int[] a){
        for (int idx = 0; idx < a.length; idx++) {
            System.out.print(a[idx] + " ");
        }
        System.out.println();
    }

    public static void mostrarInverso(int[] a){
        for (int idx = (a.length)-1; idx >=0; idx--) {
            System.out.print(a[idx] + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        int a[] = matriz();
        mostrar(a);
        mostrarInverso(a);
    }

}

