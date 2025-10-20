#include <iostream>
#include <vector>

using namespace std;

void Insort(vector<double>& buckt)
{
    for(int i = 0; i < buckt.size(); i++)
    {
        double val = buckt[i];
        int k = i - 1;
        while(k  >= 0 && buckt[k] > val)
        {
            buckt[k + 1] = buckt[k];
            k--;
        }
        buckt[k + 1] = val;
    }
}

void Bucket(vector<double>& arr)
{
    int s = arr.size();
    vector<vector<double>> bucketArr(s);

    for(int i = 0; i < s; i++)
    {
        int bi = (int)(s * arr[i]);
        bucketArr[bi].push_back(arr[i]);
    }

    for(int i = 0; i < s; i++)
    {
        Insort(bucketArr[i]);
    }

    int idx = 0;
    for(int i = 0; i < s; i++)
    {
        for(int j = 0; j < bucketArr[i].size(); j++)
        {
            arr[idx] = bucketArr[i][j];
            idx++;
        }
    }

}

int main(){

    vector<double> arr = {.77, .16, .38, .25, .71, .93, .22, .11, .24, .67};
    cout << "Arreglo desordenado: " << endl;
    for(int i = 0; i < arr.size(); i++)
    {
        cout << arr[i];
        if(i < arr.size()-1) cout << " ";
    }
    cout << endl;
    Bucket(arr);
    cout << "Arreglo ordenado: " << endl;
    for(int i = 0; i < arr.size(); i++)
    {
        cout << arr[i];
        if(i < arr.size()-1) cout << " ";
    }
    cout << endl;

    return 0;
}