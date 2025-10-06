#include "raylib.h"
#include <iostream>

using namespace std;

// --- Configuración del Tablero ---
const int SCREEN_WIDTH = 800;
const int SCREEN_HEIGHT = 800;
const int GRID_SIZE = 10;
const int MARGIN = 100;
const int DRAWABLE_SIZE = SCREEN_WIDTH - 2 * MARGIN;
const int CELL_SIZE = DRAWABLE_SIZE / GRID_SIZE;

// --- Estado del Juego ---
// 0: Agua (No Disparado)
// 1: Barco
// 2: Fallo
// 3: Golpe
int playerBoard[GRID_SIZE][GRID_SIZE] = {0};

// --- Colocación de Barcos (Simplificado para el ejemplo) ---
void SetupShips() {
    // Colocamos un pequeño barco 1x3 en la fila 2, columnas 3, 4, 5
    for (int i = 3; i < 6; i++) {
        playerBoard[2][i] = 1; 
    }
    // Barco individual 1x1
    playerBoard[7][1] = 1;
}

// --- Funciones de Lógica ---
void HandleInput() {
    if (IsMouseButtonPressed(MOUSE_LEFT_BUTTON)) {
        Vector2 mousePos = GetMousePosition();
        
        // 1. Asegurarse de que el clic esté dentro del área de la cuadrícula
        if (mousePos.x >= MARGIN && mousePos.x <= SCREEN_WIDTH - MARGIN &&
            mousePos.y >= MARGIN && mousePos.y <= SCREEN_HEIGHT - MARGIN) {
            
            // 2. Convertir coordenadas de píxeles a índices de cuadrícula (0-9)
            int col = (int)(mousePos.x - MARGIN) / CELL_SIZE;
            int row = (int)(mousePos.y - MARGIN) / CELL_SIZE;
            
            cout << "Disparo en Fila: " << row << ", Columna: " << col << endl;

            // 3. Procesar el Disparo si la celda no ha sido disparada
            if (playerBoard[row][col] < 2) { // Si es Agua (0) o Barco (1)
                
                if (playerBoard[row][col] == 1) {
                    playerBoard[row][col] = 3; // ¡Golpe!
                    cout << "¡GOLPE!" << endl;
                } else {
                    playerBoard[row][col] = 2; // Fallo
                    cout << "Fallo." << endl;
                }
            }
        }
    }
}

// --- Funciones de Dibujado ---
void DrawBoard() {
    // 1. Dibujar el marco exterior
    DrawRectangleLines(MARGIN, MARGIN, DRAWABLE_SIZE, DRAWABLE_SIZE, BLACK);

    // 2. Dibujar las celdas y el contenido
    for (int r = 0; r < GRID_SIZE; r++) {
        for (int c = 0; c < GRID_SIZE; c++) {
            
            int posX = MARGIN + c * CELL_SIZE;
            int posY = MARGIN + r * CELL_SIZE;
            
            // Dibuja el borde de la celda (líneas de la cuadrícula)
            DrawRectangleLines(posX, posY, CELL_SIZE, CELL_SIZE, DARKGRAY);

            // Dibuja el contenido (basado en el estado de la matriz)
            switch (playerBoard[r][c]) {
                case 0: 
                    // No hace nada (Agua sin disparar)
                    break;
                case 1:
                    // ¡Importante!: En el juego real, solo dibujarías el barco en tu vista,
                    // no en la vista del enemigo. Aquí lo dibujamos para verificar la ubicación.
                    DrawRectangle(posX, posY, CELL_SIZE, CELL_SIZE, GREEN);
                    break;
                case 2: // Fallo
                    DrawCircle(posX + CELL_SIZE / 2, posY + CELL_SIZE / 2, CELL_SIZE / 4, SKYBLUE);
                    break;
                case 3: // Golpe
                    DrawCircle(posX + CELL_SIZE / 2, posY + CELL_SIZE / 2, CELL_SIZE / 4, RED);
                    // Opcional: Dibuja una "X"
                    DrawLine(posX, posY, posX + CELL_SIZE, posY + CELL_SIZE, RED);
                    DrawLine(posX + CELL_SIZE, posY, posX, posY + CELL_SIZE, RED);
                    break;
            }
        }
    }
}

// --- Bucle Principal ---
int main() {
    // Configuración Inicial
    SetupShips();
    InitWindow(SCREEN_WIDTH, SCREEN_HEIGHT, "Raylib Battleship Basico");
    SetTargetFPS(60);

    // Game Loop
    while (!WindowShouldClose()) {

        // 1. Actualización de Lógica (Input, Colisiones, Turnos, etc.)
        HandleInput();

        // 2. Dibujado (Rendering)
        BeginDrawing();
        
        ClearBackground(RAYWHITE);
        
        // Mensaje de título
        DrawText("Haga clic para Disparar", 10, 10, 20, BLACK);
        
        DrawBoard();
        
        EndDrawing();
    }

    // Cierre
    CloseWindow();
    return 0;
}