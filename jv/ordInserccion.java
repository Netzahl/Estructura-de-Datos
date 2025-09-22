
public class ordInserccion {

    public static int[] insertionSort(int a[]){
        int temp =0,j=0;
        for (int i = 1; i < a.length; i++) {
            temp = a[i];
            j = i-1;
            while(j>=0 && temp < a[j]){
                a[j+1] = a[j];
                j--;
            }
            a[j+1] = temp;
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
        int a[] = {70, 15, 2, 51, 60};
        printArr(a);
        a = insertionSort(a);
        printArr(a);
    }
}
