public class hashell 
{
    public static void DisplayArr(int[] arr)
    {
        for(int x : arr){
            System.out.print(x + " ");
        }
        System.out.println("");
    }

    public int Sort(int[] arr)
    {
        int size = arr.length;
        int gapsize = size / 2;
        while(gapsize > 0)
        {
            for(int j = gapsize; j < size; j++)
            {
                int val = arr[j];
                int k = j;
                while(k >= gapsize && arr[k - gapsize] > val)
                {
                    arr[k] = arr[k - gapsize];
                    k -= gapsize;
                }
                arr[k] = val;
            }
            gapsize /= 2;
        }
        return 0;
    }

    public static void main(String[] args) {
        int[] arr = {36, 34, 43, 11, 15, 20, 28, 45};
        System.out.println("Arreglo desordenado: ");
        hashell.DisplayArr(arr);
        hashell obj = new hashell();
        obj.Sort(arr);
        System.out.println("Arreglo ordenado: ");
        hashell.DisplayArr(arr);
    }
}
