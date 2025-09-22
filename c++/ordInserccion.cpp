#include <iostream>
#include <vector>

using namespace std;

void insertionSort(vector<int>& a){
    size_t h = a.size();
    int temp = 0, j = 0;
    for(int i=1;i<h;i++){
        temp = a[i];
        j = i-1;
        while(j>=0 && temp < a[j]){
            a[j+1] = a[j];
            j--;
        }
        a[j+1] = temp;
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
    vector<int> a = {70, 15, 2, 51, 60};
    printArr(a);
    insertionSort(a);
    printArr(a);
    return 0;
}