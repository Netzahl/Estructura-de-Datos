#include <iostream>
#include <vector>

using namespace std;

void merge(vector<int>& a, int l,int m, int r){
    int a1 = m - l +1;
    int a2 = r - m;
    vector<int> L(a1,0);
    vector<int> R(a2,0);

    int i = l;
    int j = m+1;

    for(int h = 0; h < a1; h++){
        L[h] = a[i];
        i++;
    }

    for(int h = 0; h < a2; h++){
        R[h] = a[j];
        j++;
    }
    
    i=0;
    j=0;
    int k = l;

    while(i<a1 && j<a2){
        if(L[i] <= R[j]){
            a[k] = L[i];
            i++;
        }
        else
        {
            a[k] = R[j];
            j++;
        }
        k++;
    }

    while(i<a1){
        a[k] = L[i];
        i++;
        k++;
    }

    while(j<a2){
        a[k] = R[j];
        j++;
        k++;
    }

}

void mergeSort(vector<int>& a, int l, int r){
    if(l< r){
        int m = l + (r - l) / 2;
        mergeSort(a, l, m);
        mergeSort(a, m+1,r);
        merge(a,l,m,r);
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
    vector<int> a = {45, 67, 12, 5, 89, 4, 27, 48, 65, 19, 75};
    size_t size = a.size();

    cout << "Antes de ordenar\n";
    show(a);
    mergeSort(a, 0, size -1);
    cout << "Despues de ordenar\n";
    show(a);

    return 0;
}