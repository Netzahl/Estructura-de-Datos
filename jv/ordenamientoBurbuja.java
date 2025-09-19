

public class ordenamientoBurbuja {
    public static void main(String[] args) {
        int[] numeros = {56,87,52,49,20,14,32,79,68};
        int adicional = 0; 

        for (int idx = 0; idx < numeros.length; idx++) {
            System.out.print(numeros[idx] + " ");       
        }

        boolean cambio = true;
        int j = numeros.length;
        do { 
            cambio = false;
            for (int i = 1; i < j; i++) {
                if(numeros[i-1] > numeros[i]){
                    adicional = numeros[i-1];
                    numeros[i-1] = numeros[i];
                    numeros[i] = adicional;
                    cambio = true;
                }
            }
            j--;
        } while (cambio);

        System.out.println();
        for (int idx = 0; idx < numeros.length; idx++) {
            System.out.print(numeros[idx] + " ");       
        }
    }
}
