#ifndef BST_H
#define BST_H

#include "nodo.h"
#include <string>
#include <fstream>

class BST {
private:
    Nodo* raiz;
    
    Nodo* insertarRecursivo(Nodo* nodo, int key);
    bool buscarRecursivo(Nodo* nodo, int key);
    Nodo* eliminarRecursivo(Nodo* nodo, int key);
    Nodo* encontrarMinimo(Nodo* nodo);
    
    void inorderRecursivo(Nodo* nodo);
    void preorderRecursivo(Nodo* nodo);
    void postorderRecursivo(Nodo* nodo);
    
    int alturaRecursiva(Nodo* nodo);
    int contarNodos(Nodo* nodo);
    void exportInorderRecursivo(Nodo* nodo, std::ofstream& archivo);
    void destruirRecursivo(Nodo* nodo);
    
public:
    BST();
    ~BST();
    
    void insert(int key);
    bool search(int key);
    void remove(int key);
    
    void inorder();
    void preorder();
    void postorder();
    
    int height();
    int size();
    
    void exportInorder(const std::string& filename);
    void importFromFile(const std::string& filename);
};

#endif