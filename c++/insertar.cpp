#include <iostream>
#include <cstdlib>
using namespace std;

int main(){

    int numeros[10] = {1,2,3,4,5,6,7,8,9,10}, newNumeros[10], numeroInsertado, posic, j=0;
    posic= 5;
    numeroInsertado = (rand() % 100) + 1;

    for(int i=0;i<10;i++){
        if(i==posic){
            newNumeros[i]=numeroInsertado;
            j++;
        }
        else{
            newNumeros[i]=numeros[i-j];
        }
    }

    for(int i=0;i<10;i++){
        cout<<newNumeros[i]<<endl;
    }

    return 0;
}