#include "raylib.h"
#include <iostream>

const int screenWidth = 600;
const int screenHeight = 600;
const int cellSize = 200;

int board[3][3] = {0}; // 0 = vacío, 1 = X, 2 = O
int turn = 1;          // empieza jugador X
bool gameOver = false;
int winner = 0;

void DrawBoard() {
    ClearBackground(RAYWHITE);
    // líneas del tablero
    for (int i = 1; i < 3; i++) {
        DrawLine(i * cellSize, 0, i * cellSize, screenHeight, BLACK);
        DrawLine(0, i * cellSize, screenWidth, i * cellSize, BLACK);
    }

    // dibujar las fichas
    for (int y = 0; y < 3; y++) {
        for (int x = 0; x < 3; x++) {
            int value = board[y][x];
            int posX = x * cellSize + cellSize / 2;
            int posY = y * cellSize + cellSize / 2;

            if (value == 1)
                DrawText("X", posX - 30, posY - 40, 80, RED);
            else if (value == 2)
                DrawText("O", posX - 30, posY - 40, 80, BLUE);
        }
    }

    if (gameOver) {
        DrawText(winner == 0 ? "Empate!" : winner == 1 ? "Gana X!" : "Gana O!",
                  200, 550, 40, DARKGREEN);
    }
}

int CheckWinner() {
    for (int i = 0; i < 3; i++) {
        if (board[i][0] && board[i][0] == board[i][1] && board[i][1] == board[i][2])
            return board[i][0];
        if (board[0][i] && board[0][i] == board[1][i] && board[1][i] == board[2][i])
            return board[0][i];
    }
    if (board[0][0] && board[0][0] == board[1][1] && board[1][1] == board[2][2])
        return board[0][0];
    if (board[0][2] && board[0][2] == board[1][1] && board[1][1] == board[2][0])
        return board[0][2];
    return 0;
}

int main() {
    InitWindow(screenWidth, screenHeight, "Tic Tac Toe con Raylib");
    SetTargetFPS(60);

    while (!WindowShouldClose()) {
        if (!gameOver && IsMouseButtonPressed(MOUSE_LEFT_BUTTON)) {
            int x = GetMouseX() / cellSize;
            int y = GetMouseY() / cellSize;

            if (board[y][x] == 0) {
                board[y][x] = turn;
                turn = (turn == 1) ? 2 : 1;
            }

            winner = CheckWinner();
            if (winner != 0) gameOver = true;

            // Verifica empate
            bool full = true;
            for (int i = 0; i < 3; i++)
                for (int j = 0; j < 3; j++)
                    if (board[i][j] == 0) full = false;
            if (full && winner == 0) gameOver = true;
        }

        BeginDrawing();
        DrawBoard();
        EndDrawing();
    }

    CloseWindow();
    return 0;
}