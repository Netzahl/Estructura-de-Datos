#include <iostream>
#include <random>
using namespace std;

int main(){

    random_device rd;
    default_random_engine gen(rd());
    uniform_int_distribution<int> dist(1,100);

    

    return 0;
}

