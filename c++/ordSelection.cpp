#include <iostream>
#include <vector>

using namespace std;

void selectionSort(vector<int>& a){
    size_t h = a.size();
    int small = 0, adicional = 0;
    for(int i=0;i<h;i++){
        small = i;
        for(int j=i+1; j<h;j++){
            if(a[small] > a[j]){
                small = j;
            }
        }
        adicional = a[small];
        a[small]=a[i];
        a[i] = adicional;
    }
}

int printArr(vector<int> a){
    size_t h = a.size();
    for(int i=0;i<h;i++){
        cout << a[i] << " ";
    }
    cout << endl;
    return 0;
}

int main(){
    vector<int> a = {65,26,13,23,12};
    printArr(a);
    selectionSort(a);
    printArr(a);
    return 0;
}