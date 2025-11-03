#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void countingSort(vector<int>& arr, int exp) {
    int n = arr.size();
    vector<int> output(n);
    vector<int> count(10, 0);
    
    // Contar ocurrencias
    for (int i = 0; i < n; i++) {
        count[(arr[i] / exp) % 10]++;
    }
    
    // Posiciones acumulativas
    for (int i = 1; i < 10; i++) {
        count[i] += count[i - 1];
    }
    
    // Construir array de salida
    for (int i = n - 1; i >= 0; i--) {
        output[count[(arr[i] / exp) % 10] - 1] = arr[i];
        count[(arr[i] / exp) % 10]--;
    }
    
    // Copiar a array original
    for (int i = 0; i < n; i++) {
        arr[i] = output[i];
    }
}

void radixSort(vector<int>& arr) {
    // Encontrar el máximo
    int max = *max_element(arr.begin(), arr.end());
    
    // Aplicar counting sort para cada dígito
    for (int exp = 1; max / exp > 0; exp *= 10) {
        countingSort(arr, exp);
    }
}

int main() {
    vector<int> arr = {170, 45, 75, 90, 802, 24, 2, 66};
    
    cout << "Array original: ";
    for (int num : arr) cout << num << " ";
    cout << endl;
    
    radixSort(arr);
    
    cout << "Array ordenado: ";
    for (int num : arr) cout << num << " ";
    cout << endl;
    
    return 0;
}