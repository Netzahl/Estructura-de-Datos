import java.util.Arrays;

public class radixSort {
    
    static void countingSort(int arr[], int n, int exp) {
        int output[] = new int[n];
        int count[] = new int[10];
        
        // Contar ocurrencias
        for (int i = 0; i < n; i++) {
            count[(arr[i] / exp) % 10]++;
        }
        
        // Posiciones acumulativas
        for (int i = 1; i < 10; i++) {
            count[i] += count[i - 1];
        }
        
        // Construir array de salida
        for (int i = n - 1; i >= 0; i--) {
            output[count[(arr[i] / exp) % 10] - 1] = arr[i];
            count[(arr[i] / exp) % 10]--;
        }
        
        // Copiar a array original
        for (int i = 0; i < n; i++) {
            arr[i] = output[i];
        }
    }
    
    static void radixSort(int arr[], int n) {
        // Encontrar el máximo
        int max = arr[0];
        for (int i = 1; i < n; i++) {
            if (arr[i] > max) {
                max = arr[i];
            }
        }
        
        // Aplicar counting sort para cada dígito
        for (int exp = 1; max / exp > 0; exp *= 10) {
            countingSort(arr, n, exp);
        }
    }
    
    public static void main(String[] args) {
        int arr[] = {170, 45, 75, 90, 802, 24, 2, 66};
        int n = arr.length;
        
        System.out.println("Array original: " + Arrays.toString(arr));
        radixSort(arr, n);
        System.out.println("Array ordenado: " + Arrays.toString(arr));
    }
}