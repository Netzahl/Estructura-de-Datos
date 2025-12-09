#ifndef NODO_H
#define NODO_H

struct Nodo {
    int key;
    Nodo* left;
    Nodo* right;
    
    Nodo(int k) : key(k), left(nullptr), right(nullptr) {}
};

#endif