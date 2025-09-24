public class ordSelection {
    public static int[] selectionSort(int a[]){
        int small =0,adicional=0;
        for (int i = 0; i < a.length; i++) {
            small = i;
            for (int j = i+1;j<a.length;j++){
                if(a[small]>a[j]){
                    small = j;
                }
            }
            adicional = a[small];
            a[small] = a[i];
            a[i] = adicional;
        }
        return a;
    }

    public static void printArr(int a[]){
        for (int i = 0; i < a.length; i++) {
            System.out.print(a[i] + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        int a[] = {65,26,13,23,12};
        printArr(a);
        a = selectionSort(a);
        printArr(a);
    }
}
