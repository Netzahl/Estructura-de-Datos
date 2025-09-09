public class recorridoMatriz {
    public static void main(String[] args) {
        int[][] matriz ={
            {1,2,3},
            {4,5,6},
            {7,8,9}
        };

        System.out.println("Recorrido por filas");

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                System.out.print(matriz[i][j]);
            }
        }
        
        System.out.print("\n");

        System.out.println("Recorrido por columnas");

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                System.out.print(matriz[j][i]);
            }
        }
        
    }
}
