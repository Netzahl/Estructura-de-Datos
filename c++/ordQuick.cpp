#include <iostream>
#include <vector>

using namespace std;

void cambio(vector<int>& a,int j,int k){
    int adicional = a[j];
    a[j] = a[k];
    a[k] = adicional;
}

int partition(vector<int>& a,int l,int h){

    int pvt = a[h];
    int j = l-1;

    for(int k=l;k<h;k++){
        if(a[k] < pvt){
            j++;
            cambio(a,j,k);
        }
    }
    cambio(a,(j+1),h);

    return j+1;
}

void qckSort(vector<int>& a,int l,int h){
    if(l<h){
        int piv = partition(a,l,h);

        qckSort(a,l,piv-1);
        qckSort(a,piv+1,h);
    }
}

void mostrar(vector<int> a){
    size_t size = a.size();
    for (int i=0; i<size; i++){
        cout << a[i] << " ";
    }
    cout << endl;
}

int main(){
    vector<int> a = {10, 7, 8, 9, 1, 5};
    size_t size = a.size();
    mostrar(a);
    qckSort(a,0,size-1);
    mostrar(a);


    return 0;
}