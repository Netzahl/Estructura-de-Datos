import java.util.Scanner;

public class TresEnRaya {
    
    private static char[][] tablero = new char[3][3];
    private static char jugadorActual = 'X';
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        inicializarTablero();
        
        System.out.println("¡JUEGO DEL TRES EN RAYA!");
        System.out.println("Jugador 1: X | Jugador 2: O");
        
        boolean juegoTerminado = false;
        int jugadas = 0;
        
        while (!juegoTerminado) {
           
            dibujarTablero();
            
            System.out.println("Turno del jugador " + (jugadorActual == 'X' ? "1 (X)" : "2 (O)"));
            System.out.print("Ingresa fila (1-3): ");
            int fila = scanner.nextInt();
            System.out.print("Ingresa columna (1-3): ");
            int columna = scanner.nextInt();
            
            if (fila >= 1 && fila < 4 && columna >= 1 && columna < 4 && tablero[fila-1][columna-1] == ' ') {
                tablero[fila-1][columna-1] = jugadorActual;
                jugadas++;
                
                if (verificarGanador()) {
                    dibujarTablero();
                    System.out.println("¡El jugador " + (jugadorActual == 'X' ? "1 (X)" : "2 (O)") + " gana!");
                    juegoTerminado = true;
                } else if (jugadas == 9) {
                  
                    dibujarTablero();
                    System.out.println("¡Empate!");
                    juegoTerminado = true;
                } else {
                   
                    jugadorActual = (jugadorActual == 'X') ? 'O' : 'X';
                }
            } else {
                System.out.println("Movimiento inválido. Intenta de nuevo.");
            }
        }
        
        scanner.close();
    }
    
    public static void inicializarTablero() {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                tablero[i][j] = ' ';
            }
        }
    }
    
    public static void dibujarTablero() {
        System.out.println("-------------");
        for (int i = 0; i < 3; i++) {
            System.out.print("| ");
            for (int j = 0; j < 3; j++) {
                System.out.print(tablero[i][j] + " | ");
            }
            System.out.println();
            System.out.println("-------------");
        }
    }
    
    public static boolean verificarGanador() {

        for (int i = 0; i < 3; i++) {
            if (tablero[i][0] != ' ' && tablero[i][0] == tablero[i][1] && tablero[i][1] == tablero[i][2]) {
                return true;
            }
        }
        
        for (int j = 0; j < 3; j++) {
            if (tablero[0][j] != ' ' && tablero[0][j] == tablero[1][j] && tablero[1][j] == tablero[2][j]) {
                return true;
            }
        }
        
        if (tablero[0][0] != ' ' && tablero[0][0] == tablero[1][1] && tablero[1][1] == tablero[2][2]) {
            return true;
        }
        if (tablero[0][2] != ' ' && tablero[0][2] == tablero[1][1] && tablero[1][1] == tablero[2][0]) {
            return true;
        }
        
        return false;
    }
}