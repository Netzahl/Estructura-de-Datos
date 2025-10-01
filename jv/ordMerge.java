public class ordMerge{

    public static void merge(int[] a, int l, int m, int r){
        int a1 = m - l + 1;
        int a2 = r - m;
        int[] L = new int[a1];
        int[] R = new int[a2];

        int i = l;
        int j = m +1;

        for(int h = 0; h < a1;h++){
            L[h] = a[i];
            i++;
        }

        for(int h = 0; h < a2;h++){
            R[h] = a[j];
            j++;
        }

        i = 0;
        j = 0;
        int k = l;

        while(i<a1 && j<a2){
            if(L[i] <= R[j]){
                a[k] = L[i];
                i++;
            }
            else
            {
                a[k] = R[j];
                j++;
            }
            k++;
        }

        while(i<a1){
            a[k] = L[i];
            i++;
            k++;
        }

        while(j<a2){
            a[k] = R[j];
            j++;
            k++;
        }
    }

    public static void mergeSort(int[] a, int l, int r){
        if(l<r){
            int m = l + (r - l) / 2;
            mergeSort(a, l, m);
            mergeSort(a, m+1, r);
            merge(a,l,m,r);
        }
    }

    public static void show(int[] a){
        for (Object x : a) {
            System.err.print(x + " ");
        }
        System.err.println();
    }

    public static void main(String[] args) {
        int[] a = {45, 67, 12, 5, 89, 4, 27, 48, 65, 19, 75};
        int tamaño = a.length;

        System.err.println("Antes de ordenar: ");
        show(a);
        mergeSort(a, 0, tamaño-1);
        System.err.println("Despues de ordenar: ");
        show(a);

    }
}