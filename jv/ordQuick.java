public class ordQuick{
    public static void show(int[] a){
        for (Object x : a) {
            System.out.print(x + " ");
        }
        System.out.println("");
    }

    public static void swap(int[] a, int k, int j){
        int adicional = a[k];
        a[k] = a[j];
        a[j] = adicional;
    }

    public static int partition(int[] a, int l, int h){
        int pvt = a[h];
        int j = l-1;

        for(int k=l;k<h;k++){
            if(a[k]<pvt){
                j++;
                swap(a,k,j);
            }
        }
        swap(a, j+1, h);
        return j+1;
    }

    public static int[] qckSort(int[] a, int l, int h){
        
        if(l<h){
            int piv = partition(a, l, h);

            qckSort(a, l, piv-1);
            qckSort(a, piv+1, h);
        }
        return a;
    }

    public static void main(String[] args) {
        int[] a = {10, 7, 8, 9, 1, 5};
        int l = 0, h= a.length-1;
        show(a);
        a = qckSort(a, l, h);
        show(a);
    }

}