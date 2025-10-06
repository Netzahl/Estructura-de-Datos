#include <raylib.h>
#include <iostream>
#include <vector>

using namespace std;

const int SCREEN_WIDTH = 400;
const int SCREEN_HEIGHT = 750;
const int GRID_SIZE = 10;
const int MARGIN = 50;
const int DRAWABLE_SIZE = SCREEN_WIDTH - 2 * MARGIN;
const int CELL_SIZE = DRAWABLE_SIZE / GRID_SIZE;
int juegoTerminado=false;
int hundido = 0;
int contjuego=0;
int fallo=0;

//vector<vector<int>> tableroj1a(GRID_SIZE, vector<int>(GRID_SIZE, 0));
vector<vector<int>> tableroj1b(GRID_SIZE, vector<int>(GRID_SIZE, 0));
//vector<vector<int>> tableroj2a(GRID_SIZE, vector<int>(GRID_SIZE, 0));
vector<vector<int>> tableroj2b(GRID_SIZE, vector<int>(GRID_SIZE, 0));

int ori = 1, barco = 0, barcosPuestos=0;
int contIni=0;
vector<int> bar(6,0);
//Color transparente = {0,0,0,0};
//vector<Color> colors = {transparente,RED,SKYBLUE,GREEN,YELLOW,VIOLET,ORANGE,BROWN};

bool isTurnTransition;
bool isTurnHundir;
int currentPlayer = 1;
// 1. Duración deseada de la pausa (ej: 2.0 segundos)
const float PAUSE_DURATION = 2.0f; 

// 2. Bandera que indica que el juego debe estar en pausa.
bool isPausedByTimer = false;
bool isPausedByHundir = false;

// 3. Contador de tiempo restante.
float pauseTimer = 0.0f; 
/**
 * @brief Inicia la transición de turno, pausa el juego y prepara el cambio de jugador.
 */

void StartHundir() {
    
    isTurnHundir = true; 
    currentPlayer = (currentPlayer == 1) ? 2 : 1; 
    cout << "Transicion iniciada. El siguiente turno es para el Jugador: " << currentPlayer << endl;
}

void StartTurnTransition() {
    // 1. Activa el flag de transición/pausa.
    isTurnTransition = true; 
    
    // 2. Aquí PUEDES cambiar el jugador si quieres que la pantalla muestre
    //    el turno del *siguiente* jugador (el que está por comenzar).
    //    Si prefieres que la pantalla muestre el turno del jugador *actual* (el que acaba de terminar),
    //    entonces mueve esta línea al UpdateTurnTransition().
    currentPlayer = (currentPlayer == 1) ? 2 : 1; 
    
    // Opcional: Muestra en consola quién está por jugar
    cout << "Transicion iniciada. El siguiente turno es para el Jugador: " << currentPlayer << endl;
}

void UpdateHundir() {
    // Si NO estamos en modo transición, no hagas nada.
    if (!isTurnHundir) {
        return;
    }
    
    ClearBackground(GRAY);
    DrawText("Has hundido una\n nave enemiga\nCambio de turno\nPresione E", MARGIN, SCREEN_HEIGHT/2, 38, BLACK);
    fallo = 0;
    // Si estamos en transición, el juego está pausado y esperamos 'E'.
    if (IsKeyPressed(KEY_E)) {
        
        // 1. Termina la transición (quita la pantalla de pausa)
        isTurnHundir = false;
        
        // 2. NOTA: Ya no cambiamos el jugador aquí, porque se hizo en StartTurnTransition()
        cout << "Teclado E presionado. Turno activo para el Jugador: " << currentPlayer << endl;
    }
}

void UpdateTurnTransition() {
    // Si NO estamos en modo transición, no hagas nada.
    if (!isTurnTransition) {
        return;
    }
    
    ClearBackground(GRAY);
    DrawText("Cambio de turno\nPresione E", MARGIN, SCREEN_HEIGHT/2, 38, BLACK);
    fallo = 0;
    // Si estamos en transición, el juego está pausado y esperamos 'E'.
    if (IsKeyPressed(KEY_E)) {
        
        // 1. Termina la transición (quita la pantalla de pausa)
        isTurnTransition = false;
        
        // 2. NOTA: Ya no cambiamos el jugador aquí, porque se hizo en StartTurnTransition()
        cout << "Teclado E presionado. Turno activo para el Jugador: " << currentPlayer << endl;
    }
}

void UpdatePausehundir() {
    // Solo actualiza si la bandera de pausa está activa
    if (isPausedByHundir) {
        
        // Descuenta el tiempo que tomó renderizar el último fotograma.
        // GetFrameTime() da el tiempo exacto en segundos.
        pauseTimer -= GetFrameTime(); 

        // Cuando el contador llega a cero o menos, la pausa termina.
        if (pauseTimer <= 0.0f) {
            
            // 1. Desactiva la bandera de pausa. El juego se reanuda.
            isPausedByHundir = false;
            
            // 2. ✨ Aquí llamas a la función que debe ejecutarse al terminar la pausa ✨
            // Por ejemplo: iniciar un cambio de turno, o mover a la IA.
            StartHundir();
        }
    }
}

void UpdatePauseTimer() {
    // Solo actualiza si la bandera de pausa está activa
    if (isPausedByTimer) {
        
        // Descuenta el tiempo que tomó renderizar el último fotograma.
        // GetFrameTime() da el tiempo exacto en segundos.
        pauseTimer -= GetFrameTime(); 

        // Cuando el contador llega a cero o menos, la pausa termina.
        if (pauseTimer <= 0.0f) {
            
            // 1. Desactiva la bandera de pausa. El juego se reanuda.
            isPausedByTimer = false;
            
            // 2. ✨ Aquí llamas a la función que debe ejecutarse al terminar la pausa ✨
            // Por ejemplo: iniciar un cambio de turno, o mover a la IA.
            StartTurnTransition();
        }
    }
}

void verificacion_de_colocacion(int a, int b,vector<vector<int>>& arr) {
    if (IsMouseButtonPressed(MOUSE_LEFT_BUTTON)) {
        Vector2 mousePos = GetMousePosition();
        
        // 1. Asegurarse de que el clic esté dentro del área de la cuadrícula
        if (mousePos.x >= MARGIN && mousePos.x <= SCREEN_WIDTH - MARGIN &&
            mousePos.y >= MARGIN+350 && mousePos.y <= SCREEN_HEIGHT - MARGIN+350) {
            
            // 2. Convertir coordenadas de píxeles a índices de cuadrícula (0-9)
            int col = (int)(mousePos.x - MARGIN) / CELL_SIZE;
            int row = (int)(mousePos.y - MARGIN - 350) / CELL_SIZE;
            
            cout << "Disparo en Fila: " << row << ", Columna: " << col << endl;
            int cont = 0;

            if (row >= 0 && row < GRID_SIZE && 
                col >= 0 && col < GRID_SIZE) {
                    if (ori == 1){
                if(col+a <= 10){

                    for(int i = col; i < col+a; i++){
                        if(arr[row][i] != 0){
                            cont ++;
                        }
                    }

                    if(cont==0 && bar[b] == 0){
                        for(int i = col; i < col+a; i++){
                        arr[row][i] = b+2;
                        }
                        bar[b]++;
                        barcosPuestos++;
                    }
                    else{
                        cont=0;
                    }
                }
            }
            else if(ori == 2)
            {
                if(row+a <= 10){
                    for(int i = row; i < row+a; i++){
                        if(arr[i][col] != 0){
                            cont++;
                        }
                    }

                    if(cont == 0 && bar[b] == 0){
                        for(int i = row; i < row+a; i++){
                        arr[i][col] = b+2;
                        }
                        bar[b]++;
                        barcosPuestos++;
                    }
                    else{
                        cont = 0;
                    }
                }
            }
                }
        }
    }
}

void Colocacion(){
    switch (barco)
    {
        case 1:
        if(barcosPuestos<5){
            verificacion_de_colocacion(2,1,tableroj1b);
        }
        else{
            verificacion_de_colocacion(2,1,tableroj2b);
        }
        break;
        case 2:
        if(barcosPuestos<5){
            verificacion_de_colocacion(3,2,tableroj1b);
        }
        else{
            verificacion_de_colocacion(3,2,tableroj2b);
        }
        
        break;
        case 3:
        if(barcosPuestos<5){
            verificacion_de_colocacion(3,3,tableroj1b);
        }
        else{
            verificacion_de_colocacion(3,3,tableroj2b);
        }
        break;
        case 4:
        if(barcosPuestos<5){
            verificacion_de_colocacion(4,4,tableroj1b);
        }
        else{
            verificacion_de_colocacion(4,4,tableroj2b);
        }
        break;
        case 5:
        if(barcosPuestos<5){
            verificacion_de_colocacion(5,5,tableroj1b);
        }
        else{
            verificacion_de_colocacion(5,5,tableroj2b);
        }
        break;
    default:
        break;
    }
}

void Orientacion(){
    if(IsKeyPressed(KEY_R)){
        if(ori == 1){
            ori = 2;
        }
        else{
            ori = 1;
        }
    }
}

void Posicionamiento() {
    if (IsMouseButtonPressed(MOUSE_LEFT_BUTTON)) {
        Vector2 mousePos = GetMousePosition();
        
        // 1. Asegurarse de que el clic esté dentro del área de la cuadrícula
        if (mousePos.x >= MARGIN && mousePos.x <= MARGIN + CELL_SIZE * 5 &&
            mousePos.y >= MARGIN + 80 && mousePos.y <= MARGIN + 80 + CELL_SIZE && bar[5]==0) {
                barco = 5;
        }

        if (mousePos.x >= MARGIN && mousePos.x <= MARGIN + CELL_SIZE * 4 &&
            mousePos.y >= MARGIN + 120 && mousePos.y <= MARGIN + 120 + CELL_SIZE && bar[4]==0) {
                barco = 4;
        }

        if (mousePos.x >= MARGIN && mousePos.x <= MARGIN + CELL_SIZE * 3 &&
            mousePos.y >= MARGIN + 160 && mousePos.y <= MARGIN + 160 + CELL_SIZE && bar[3]==0) {
                barco = 3;
        }

        if (mousePos.x >= MARGIN && mousePos.x <= MARGIN + CELL_SIZE * 3 &&
            mousePos.y >= MARGIN + 200 && mousePos.y <= MARGIN + 200 + CELL_SIZE && bar[2] == 0) {
                barco = 2;
        }

        if (mousePos.x >= MARGIN && mousePos.x <= MARGIN + CELL_SIZE * 2 &&
            mousePos.y >= MARGIN + 240 && mousePos.y <= MARGIN + 240 + CELL_SIZE && bar[1]==0) {
                barco = 1;
        }

    }
}

void SeleccionBarcos(){
    if(bar[5]==0){
        DrawRectangle(MARGIN, MARGIN+80,CELL_SIZE * 5 , CELL_SIZE, BROWN);
        DrawRectangleLines(MARGIN , MARGIN+80,CELL_SIZE * 5 , CELL_SIZE, BLACK);
    }
    if(bar[4]==0){
        DrawRectangle(MARGIN, MARGIN+120,CELL_SIZE * 4 , CELL_SIZE, ORANGE);
        DrawRectangleLines(MARGIN , MARGIN+120,CELL_SIZE * 4 , CELL_SIZE, BLACK);
    }
    if(bar[3]==0){
        DrawRectangle(MARGIN, MARGIN+160,CELL_SIZE * 3 , CELL_SIZE, VIOLET);
        DrawRectangleLines(MARGIN , MARGIN+160,CELL_SIZE * 3 , CELL_SIZE, BLACK);
    }
    if(bar[2]==0){
        DrawRectangle(MARGIN, MARGIN+200,CELL_SIZE * 3 , CELL_SIZE, YELLOW);
        DrawRectangleLines(MARGIN , MARGIN+200,CELL_SIZE * 3 , CELL_SIZE, BLACK);

    }
    if(bar[1]==0){
        DrawRectangle(MARGIN, MARGIN+240,CELL_SIZE * 2 , CELL_SIZE, GREEN);
        DrawRectangleLines(MARGIN , MARGIN+240,CELL_SIZE * 2 , CELL_SIZE, BLACK);
    }
}

void DrawBoardA(vector<vector<int>>& a) {

    // 2. Dibujar las celdas y el contenido
    for (int r = 0; r < GRID_SIZE; r++) {
        for (int c = 0; c < GRID_SIZE; c++) {
            
            int posX = MARGIN + c * CELL_SIZE;
            int posY = MARGIN + r * CELL_SIZE;
            
            // Dibuja el borde de la celda (líneas de la cuadrícula)
            DrawRectangleLines(posX, posY, CELL_SIZE, CELL_SIZE, DARKGRAY);

            // Dibuja el contenido (basado en el estado de la matriz)
            switch (a[r][c]) {
                case 0: 
                    break;
                case 1:
                    DrawCircle(posX + CELL_SIZE / 2, posY + CELL_SIZE / 2, CELL_SIZE / 4, RED);
                    DrawLine(posX, posY, posX + CELL_SIZE, posY + CELL_SIZE, RED);
                    DrawLine(posX + CELL_SIZE, posY, posX, posY + CELL_SIZE, RED);
                    break;
                case 2: // Fallo
                    DrawCircle(posX + CELL_SIZE / 2, posY + CELL_SIZE / 2, CELL_SIZE / 4, SKYBLUE);
                    break;
            }
        }
    }
    DrawRectangleLines(MARGIN, MARGIN, DRAWABLE_SIZE, DRAWABLE_SIZE, BLACK);
}

void DrawBoardB(vector<vector<int>>& a) {

    // 2. Dibujar las celdas y el contenido
    for (int r = 0; r < GRID_SIZE; r++) {
        for (int c = 0; c < GRID_SIZE; c++) {
            
            int posX = MARGIN + c * CELL_SIZE;
            int posY = MARGIN + r * CELL_SIZE + 350;
            
            // Dibuja el borde de la celda (líneas de la cuadrícula)
            DrawRectangleLines(posX, posY, CELL_SIZE, CELL_SIZE, DARKGRAY);

            // Dibuja el contenido (basado en el estado de la matriz)
            switch (a[r][c]) {
                case 0: 
                    break;
                case 1:
                    DrawCircle(posX + CELL_SIZE / 2, posY + CELL_SIZE / 2, CELL_SIZE / 4, RED);
                    DrawLine(posX, posY, posX + CELL_SIZE, posY + CELL_SIZE, RED);
                    DrawLine(posX + CELL_SIZE, posY, posX, posY + CELL_SIZE, RED);
                    break;
                case 2: // Fallo
                    DrawCircle(posX + CELL_SIZE / 2, posY + CELL_SIZE / 2, CELL_SIZE / 4, SKYBLUE);
                    break;
                case 3: 
                    DrawRectangle(posX, posY, CELL_SIZE, CELL_SIZE, GREEN);
                    break;
                case 4: 
                    DrawRectangle(posX, posY, CELL_SIZE, CELL_SIZE, YELLOW);
                    break;
                case 5: 
                    DrawRectangle(posX, posY, CELL_SIZE, CELL_SIZE, VIOLET);
                    break;
                case 6: 
                    DrawRectangle(posX, posY, CELL_SIZE, CELL_SIZE, ORANGE);
                    break;
                case 7: 
                    DrawRectangle(posX, posY, CELL_SIZE, CELL_SIZE, BROWN);
                    break;
            }
        }
    }
    DrawRectangleLines(MARGIN, MARGIN + 350, DRAWABLE_SIZE, DRAWABLE_SIZE, BLACK);
}

void Inicializar()
{

    if(barcosPuestos==5 && contIni==0){
        ClearBackground(GRAY);
        DrawText("Cambio de turno\nPresione E", MARGIN, SCREEN_HEIGHT/2, 38, BLACK);
        bar[1] = 0; bar[2] = 0; bar[3] = 0; bar[4] = 0; bar[5] = 0;
        if(IsKeyPressed(KEY_E)==true){
            contIni++;
        }
    }
    else
    {
    DrawText("Haga clic en barco deseado y\nluego en la posicion a colocar:", 10, 10, 20, BLACK);
    DrawText("Presione R para intercambiar \nentre horizontal y vertical", 10, 55, 20, BLACK);
    SeleccionBarcos();
    Posicionamiento();
    Orientacion();
    Colocacion();

    if(barcosPuestos<5){
        DrawBoardB(tableroj1b);
    }
    else{
        DrawBoardB(tableroj2b);
    }
    }

    if(barcosPuestos == 10){
        contIni = 0;
    }

}

void HandleInput(vector<vector<int>>& arr) {
    if (IsMouseButtonPressed(MOUSE_LEFT_BUTTON) && fallo == 0) {
        Vector2 mousePos = GetMousePosition();
        
        // 1. Asegurarse de que el clic esté dentro del área de la cuadrícula
        if (mousePos.x >= MARGIN && mousePos.x <= SCREEN_WIDTH - MARGIN &&
            mousePos.y >= MARGIN && mousePos.y <= SCREEN_HEIGHT - MARGIN) {
            
            // 2. Convertir coordenadas de píxeles a índices de cuadrícula (0-9)
            int col = (int)(mousePos.x - MARGIN) / CELL_SIZE;
            int row = (int)(mousePos.y - MARGIN) / CELL_SIZE;
            
            cout << "Disparo en Fila: " << row << ", Columna: " << col << endl;
            int contador =0;
            contjuego = 0;
            
            if (row >= 0 && row < GRID_SIZE && 
                col >= 0 && col < GRID_SIZE){
                    if (arr[row][col] ==0 || (arr[row][col] > 2 && arr[row][col]<8)) { 
                        if (arr[row][col] > 2 && arr[row][col]<8) {
                            
                            hundido = arr[row][col];
                            arr[row][col] = 1; // ¡Golpe!

                            for(int i = 0;i<10;i++){
                                for(int j=0;j<10;j++){
                                    if(arr[i][j] == hundido){
                                        contador++;
                                    }
                                }
                            }

                            for(int i = 0;i<10;i++){
                                for(int j=0;j<10;j++){
                                    if(arr[i][j] > 2){
                                        contjuego++;
                                    }
                                }
                            }
                            
                            if(contjuego == 0){
                                juegoTerminado = true;
                                cout << "Juego terminado, gano el jugador " << currentPlayer << endl;
                            }

                            if(contador == 0){
                                isPausedByHundir = true;
                                pauseTimer = PAUSE_DURATION;
                                
                                fallo++;
                            }

                        cout << "¡GOLPE!" << endl;
                        }else if(arr[row][col] == 0){
                        arr[row][col] = 2; // Fallo
                        fallo++;
                        cout << "Fallo." << endl;
                        isPausedByTimer = true;
                        pauseTimer = PAUSE_DURATION;
                        }
                    }
            }
            
            
        }
    }
}

void Disparos(){
    if (currentPlayer == 1)
    {
        DrawBoardA(tableroj2b);
        DrawBoardB(tableroj1b);
        HandleInput(tableroj2b);
    }
    else
    {
        DrawBoardA(tableroj1b);
        DrawBoardB(tableroj2b);
        HandleInput(tableroj1b);
    }
}

void juego(){
    if(contIni==0){
        ClearBackground(GRAY);
        DrawText("Cambio de turno\nPresione E", MARGIN, SCREEN_HEIGHT/2, 38, BLACK);
        if(IsKeyPressed(KEY_E)==true){
            contIni++;
        }
    }
    else
    {
        UpdatePausehundir();
        UpdatePauseTimer();
        UpdateHundir();
        UpdateTurnTransition();
        if(isTurnTransition == false && isTurnHundir == false){
            if(juegoTerminado==false)
            {
            Disparos();
            }
        }
        
    }

}

int main(){

    InitWindow(SCREEN_WIDTH,SCREEN_HEIGHT,"Batalla Naval");
    SetTargetFPS(60);

    while(WindowShouldClose() == false)
    {
        BeginDrawing();
        ClearBackground(BLUE);
        if(barcosPuestos<10)
        {
            Inicializar();
        }
        else if(juegoTerminado==false)
        {
            juego();
        }
        else{
            if(currentPlayer == 1){
                DrawText("Ha ganado el \njugador 1", MARGIN, SCREEN_HEIGHT/2, 30, BLACK);
            }
            else
            {
                DrawText("Ha ganado el \njugador 2", MARGIN, SCREEN_HEIGHT/2, 30, BLACK);
            }
        }
        
        EndDrawing();
    }

    CloseWindow();
    return 0;
}