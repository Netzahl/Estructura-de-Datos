#include <iostream>
#include <random>
using namespace std;

int main(){
    random_device rd;
    default_random_engine gen(rd());
    uniform_int_distribution<int> dist(1,20);

    int numeros[10];
    int adicional = 0;

    for(int i=0;i<10;i++){
        numeros[i] = dist(gen);
    }   

    cout << " | ";
    for(int i=0;i<10;i++){
        cout << numeros[i] << " | ";
    }   
    cout << endl;
    
    
    bool cambio = true;
    int j = sizeof(numeros)/sizeof(numeros[0]);
    do{
        cambio = false;
        for(int i=1;i<j;i++){
            if (numeros[i-1] > numeros[i]){
                adicional = numeros[i-1];
                numeros[i-1] = numeros[i];
                numeros[i] = adicional;
                cambio = true;
            }
        }
        j--;
    }while(cambio == true);

    cout << " | ";
    for(int i=0;i<10;i++){
        cout << numeros[i] << " | ";
    }   


}