public class ordHeap{

    public static void heapSort(int[] a, int h){
        while(h>0){
            int adicional =0, j=0;
            for(int i = h; i>0;i--){
                j = i/2;
                if(a[i] > a[j]){
                    adicional = a[i];
                    a[i] = a[j];
                    a[j] = adicional;
                }
            }
            adicional = a[0];
            a[0] = a[h];
            a[h] = adicional;
            h--;
        }
    }

    public static void show(int[] a){
        for (Object x : a) {
            System.out.print(x + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        int[] a = {12, 94, 32, 5, 48, 64, 26, 57};
        int tamaño = a.length;

        System.out.println("Antes de ordenar: ");
        show(a);
        heapSort(a, tamaño-1);
        System.out.println("Despues de ordenar: ");
        show(a);
    }
}