#include <iostream>
using namespace std;

int main() {

    int matriz[3][3] = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };
    
    cout << "Recorrido por filas:" << endl;

    for(int i = 0; i < 3; i++) {       
        for(int j = 0; j < 3; j++) {     
            cout << matriz[i][j] << " ";
        }
    }

    cout <<endl << "Recorrido por columnas:" << endl;

    for(int i = 0; i < 3; i++) {       
        for(int j = 0; j < 3; j++) {     
            cout << matriz[j][i] << " ";
        }
    }

    return 0;
}