#include <iostream>
#include <vector>

using namespace std;

class Hashell{
    public:
    static void DisplayArr(const vector<int> arr)
    {
        for (int k : arr)
        {
            cout << k << " ";
        }
        cout << endl;
    }

    int Sort(vector<int>& arr)
    {
        int size = arr.size();
        int gapsize = size / 2;
        while(gapsize > 0){
            for (int j = gapsize; j < size; j++)
            {
                int val = arr[j];
                int k = j;
                while(k >= gapsize && arr[k - gapsize] > val)
                {
                    arr[k] = arr[k - gapsize];
                    k -= gapsize;
                }
                arr[k] = val;
            }
            gapsize /= 2;
        }
        return 0;
    }
};

int main(){
    vector<int> arr = {36, 34, 43, 11, 15, 20, 28, 45};
    cout << "Arreglo desordenado: " << endl;
    Hashell :: DisplayArr(arr);
    Hashell obj;
    obj.Sort(arr);
    cout << "Arreglo ordenado: " << endl;
    Hashell :: DisplayArr(arr);
}