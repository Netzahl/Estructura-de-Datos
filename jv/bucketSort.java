import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class bucketSort {
    static void Insort(List<Double> bukt)
    {
        for (int i = 0; i < bukt.size(); i++)
        {
            double val = bukt.get(i);
            int k = i - 1;
            while(k >= 0 && bukt.get(k) > val)
            {
                bukt.set(k + 1, bukt.get(k));
                k--;
            }
            bukt.set(k + 1, val);
        }
    }

    static void BucketOrd(double[] arr)
    {
        int s = arr.length;
        List<List<Double>> buckts = new ArrayList<>();
        for (int i = 0; i < s; i++)
        {
            buckts.add(new ArrayList<>());
        }

        for (Double x : arr) {
            int bi = (int)(x * s);
            buckts.get(bi).add(x);
        }

        for (List<Double> bukt : buckts) {
            Insort(bukt);
        }

        int idx = 0;
        for (List<Double> bukt : buckts) {
            for(Double x : bukt)
            {
                arr[idx] = x;
                idx++;
            }
        }

    }

    public static void main(String[] args) {
        double[] arr = {0.77, 0.16, 0.38, 0.25, 0.71, 0.93, 0.22, 0.11, 0.24, 0.67};

        System.out.println("Arreglo desordenado: ");
        System.out.println(Arrays.toString(arr));
        BucketOrd(arr);
        System.out.println("Arreglo ordenado: ");
        System.out.println(Arrays.toString(arr));
    }
}
