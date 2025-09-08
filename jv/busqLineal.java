import java.util.Random;

public class busqLineal {
    
    public static void main(String[] args){

        int[] array = new  int[10];
        Random rand = new Random();

        for (int i = 0; i < 10; i++){

            array[i] = rand.nextInt(30);
            
        }

        int numeroABuscar = rand.nextInt(30);
        boolean encontrado = false;
        int posicion = 0;

        for (int i = 0; i < 10; i++) {

            if(array[i] == numeroABuscar){

                encontrado = true;
                posicion = i+1;

            }

        }

        if (encontrado == true) {

            System.out.print("El numero "+numeroABuscar+", fue encontrado en la posicion "+posicion+" del array");
            
        }
        else{

            System.out.print("El numero "+numeroABuscar+", no fue encontrado dentro del array");

        }

    }

}
