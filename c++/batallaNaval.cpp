#include <iostream>
#include <vector>
#include <string>

using namespace std;

//Muestra el estado actual del tablero
void mostrarTablero(const vector<vector<string>> &matriz){
    string letras[] = {"A","B","C","D","E","F","G","H","I","J"};
    vector<int> num = {1,2,3,4,5,6,7,8,9,10};
    cout << "      ---------------------------------------------------------------" << endl << "      ";
    for(int i=0;i < num.size();i++){
        cout << " |  " << num[i] << " ";
    }
    cout << "| " << endl << "---------------------------------------------------------------------" << endl;
    for(int i=0;i<matriz.size();i++){
        cout << " |  " << letras[i] << " ";
        for(int j=0;j<matriz[i].size();j++){
            cout << " | " << matriz[i][j];
        }
        cout << " | " << endl << "---------------------------------------------------------------------" << endl;
    }
}

//Modifica el tablero al agregar los barcos mediante los datos recibidos
void modificarTablero(vector<vector<string>> &matriz, int x,int y, int barco,int orientacion){
    if(orientacion == 1){
        for(int i = x; i < x+barco; i++){
            matriz[y][i] = " O ";
        }
    }else{
        for(int i = y; i < y+barco; i++){
            matriz[i][x] = " O ";
        }
    }
}

//Verifica que se pueda colocar el barco de manera exitosa con los datos recibidos
bool verificarBarcos(const vector<vector<string>> &matriz, int x,int y, int barco,int orientacion){
    if(orientacion == 1){
        if(barco + x > 10){
            cout << "Ubicacion fuera del mapa.\nIngrese de nuevo\n";
            return true;
        }else{
            for(int i = x; i < x+barco; i++){
                if(matriz[y][i] != "   "){
                    cout << "Ubicacion con colision de barcos.\nIngrese de nuevo\n";
                    return true;
                }
            }
            return false;
        }
    }else{
        if(barco + y > 10){
            cout << "Ubicacion fuera del mapa.\nIngrese de nuevo\n";
            return true;
        }else{
            for(int i = y; i < y+barco; i++){
                if(matriz[i][x] != "   "){
                    cout << "Ubicacion con colision de barcos.\nIngrese de nuevo\n";
                    return true;
                }
            }
            return false;
        }
    }
}

//Recolecta los datos necesarios para poner los barcos, y manda la informacion recolectada a verificarBarcos()
//para despues de su verificacion mandar a modificarTablero() y por ultimo mostrarTablero()
void colocarBarcos(vector<vector<string>> &matriz, int barco){
    string coordenada;
    int x=0,y=0,orientacion = 0;
    bool valido, loop;
    do{
        do{
        valido = true;
        cout << "Donde desea colocar el barco? Ejemplo:(a1)" << endl;
        cin >> coordenada;

        switch (coordenada[0])
    {
    case 'a':
        y=0;
        break;
    case 'b':
        y=1;
        break;
    case 'c':
        y=2;
        break;
    case 'd':
        y=3;
        break;
    case 'e':
        y=4;
        break;
    case 'f':
        y=5;
        break;
    case 'g':
        y=6;
        break;
    case 'h':
        y=7;
        break;
    case 'i':
        y=8;
        break;
    case 'j':
        y=9;
        break;
    default:
        cout << "Opcion invalida.\nIngrese de nuevo"<< endl;
        valido = false;
        break;
    }
        
        coordenada[0]=' ';

        try {
        x = stoi(coordenada)-1;
        } catch (const invalid_argument& e) {
        cout << "Opcion invalida.\nIngrese de nuevo"<< endl;
        valido = false;
        } catch (const out_of_range& e) {
        cout << "Opcion invalida.\nIngrese de nuevo"<< endl;
        valido = false;
        }

        if(x>9 || x<0){
            cout << "Opcion invalida.\nIngrese de nuevo"<< endl;
            valido = false;
        }
        }while(!valido);

        orientacion = 0;
        do{
        cout << "Como desea acomodarlo?" << endl;
        cout << "| 1)Horizontal | 2)Vertical |" << endl;
        cin >> orientacion;
        if(orientacion != 1 && orientacion != 2){
            cout << "Opcion invalida.\nIngrese de nuevo"<< endl;
        }
        }while(orientacion != 1 && orientacion != 2);

        loop = false;

        loop = verificarBarcos(matriz,x,y,barco,orientacion);
    }while(loop);

    modificarTablero(matriz,x,y,barco,orientacion);
    mostrarTablero(matriz);
}

//Elige el barco sin repetirlo
void elegirBarcos(vector<vector<string>> &matriz){
    int barco = 0;
    int armada[] = {0,0,0,0,0,0};
    bool bandera = true;;
    for(int i=0;i<5;i++){
        bandera = true;
        cout << "Que barco desea colocar?" << endl;
        do{
            barco = 0;
            bandera = true;
            cout << "| 1)Destructor(2 size) | 2)Submarino(3 size) | 3)Crucero(3 size) | 4)Acorazado(4 size) | 5)Portaviones(5 size) |" << endl;
            cin >> barco;
            switch (barco)
            {
            case 1:
                armada[barco] ++;
                if(armada[barco] > 1){
                    cout << "Opcion ya elegida.\nIngrese de nuevo: " << endl;
                    bandera = false;
                }
                barco = 2;
                break;
            case 2:
                armada[barco] ++;
                if(armada[barco] > 1){
                    cout << "Opcion ya elegida.\nIngrese de nuevo: " << endl;
                    bandera = false;
                }
                barco = 3;
                break;
            case 3:
                armada[barco] ++;
                if(armada[barco] > 1){
                    cout << "Opcion ya elegida.\nIngrese de nuevo: " << endl;
                    bandera = false;
                }
                barco = 3;
                break;
            case 4:
                armada[barco] ++;
                if(armada[barco] > 1){
                    cout << "Opcion ya elegida.\nIngrese de nuevo: " << endl;
                    bandera = false;
                }
                barco = 4;
                break;
            case 5:
                armada[barco] ++;
                if(armada[barco] > 1){
                    cout << "Opcion ya elegida.\nIngrese de nuevo: " << endl;
                    bandera = false;
                }
                barco = 5;
                break;
            default:
                break;
            }
            if (barco > 5 || barco < 2){
                cout << "Opcion invalida.\nIngrese de nuevo: " << endl;
                bandera = false;
            }
        }while(!bandera);

        colocarBarcos(matriz,barco);
    }
    
}

//Arranca el programa
int main(){
    vector<vector<string>> matriz(10, vector<string>(10, "   "));
    mostrarTablero(matriz);
    elegirBarcos(matriz);

    return 0;
}
