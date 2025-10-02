#include <iostream>
#include <vector>

using namespace std;

void heapSort(vector<int>& a, int h){
    int adicional = 0, j =0;
    while (h >= 0)
    {
        for(int i = h; i >= 0; i--)
        {
            j = i / 2;
            if(a[i] > a[j]){
                adicional = a[i];
                a[i] = a[j];
                a[j] = adicional;
            }
        }
        adicional = a[0];
        a[0] = a[h];
        a[h] = adicional;
        h--;
    }
}

void show(vector<int> a){
    for (auto &&i : a)
    {
        cout << i << " ";
    }
    cout << endl;
}

int main(){
    vector<int> a = {12,94,32,5,48,64,26,57};
    size_t size = a.size();

    cout << "Antes de ordenar: \n";
    show(a);
    heapSort(a,size-1);
    cout << "Despues de ordenar: \n";
    show(a);

    return 0;
}