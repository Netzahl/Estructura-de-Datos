#include <iostream>
#include <random>
using namespace std;

int main(){

    random_device rd;
    default_random_engine gen(rd());
    uniform_int_distribution<int> dist(1,20);

    int numeros[10];

    for(int i=0;i<10;i++){
        numeros[i] = dist(gen);
    }   

    int numeroBuscado = dist(gen), posic=0;
    bool bandera = false;

    for(int i=0;i<10;i++){
        if (numeros[i] == numeroBuscado){
            posic = i;
            bandera =true;
        }
    }
    
    if (bandera == true){
        cout<<"El numero "<<numeroBuscado<<", fue encontrado en la posicion "<<posic<<" del array"<<endl;
    }
    else{
        cout<<"El numero "<<numeroBuscado<<", no fue encontrado dentro del array"<<endl;
    }

    return 0;
}

