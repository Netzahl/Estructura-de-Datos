#include "bst.h"
#include <iostream>
#include <fstream>
#include <sstream>

BST::BST() : raiz(nullptr) {}

BST::~BST() {
    destruirRecursivo(raiz);
}

void BST::destruirRecursivo(Nodo* nodo) {
    if (nodo == nullptr) return;
    
    destruirRecursivo(nodo->left);
    destruirRecursivo(nodo->right);
    delete nodo;
}

void BST::insert(int key) {
    raiz = insertarRecursivo(raiz, key);
}

Nodo* BST::insertarRecursivo(Nodo* nodo, int key) {
    if (nodo == nullptr) return new Nodo(key);
    
    if (key < nodo->key)
        nodo->left = insertarRecursivo(nodo->left, key);
    else if (key > nodo->key)
        nodo->right = insertarRecursivo(nodo->right, key);
    
    return nodo;
}

void BST::inorder() {
    inorderRecursivo(raiz);
    std::cout << std::endl;
}

void BST::inorderRecursivo(Nodo* nodo) {
    if (nodo == nullptr) return;
    
    inorderRecursivo(nodo->left);
    std::cout << nodo->key << " ";
    inorderRecursivo(nodo->right);
}

bool BST::search(int key) {
    return buscarRecursivo(raiz, key);
}

bool BST::buscarRecursivo(Nodo* nodo, int key) {
    if (nodo == nullptr) return false;
    if (nodo->key == key) return true;
    if (key < nodo->key){
        return buscarRecursivo(nodo->left, key);  
    }
    else{
        return buscarRecursivo(nodo->right, key);  
    }
}

void BST::preorder() {
    preorderRecursivo(raiz);
    std::cout << std::endl;
}

void BST::preorderRecursivo(Nodo* nodo) {
    if (nodo == nullptr) return;
    
    std::cout << nodo->key << " ";
    preorderRecursivo(nodo->left);
    preorderRecursivo(nodo->right);
}

void BST::postorder() {
    postorderRecursivo(raiz);
    std::cout << std::endl;
}

void BST::postorderRecursivo(Nodo* nodo) {
    if (nodo == nullptr) return;
    
    postorderRecursivo(nodo->left);
    postorderRecursivo(nodo->right);
    std::cout << nodo->key << " ";
}

int BST::height() {
    return alturaRecursiva(raiz);
}

int BST::alturaRecursiva(Nodo* nodo) {
    if (nodo == nullptr) return -1;
    int alturaIzq = alturaRecursiva(nodo->left);
    int alturaDer = alturaRecursiva(nodo->right);
    return 1 + (alturaIzq > alturaDer ? alturaIzq : alturaDer);
    
}

int BST::size() {
    return contarNodos(raiz);
}

int BST::contarNodos(Nodo* nodo) {
    if (nodo == nullptr) return 0;
    return 1 + contarNodos(nodo->left) + contarNodos(nodo->right);
}

void BST::exportInorder(const std::string& filename) {
    std::ofstream archivo(filename);
    
    if (!archivo.is_open()) {
        std::cerr << "Error: No se pudo abrir el archivo " << filename << std::endl;
        return;
    }
    
    exportInorderRecursivo(raiz, archivo);
    archivo.close();
    
    std::cout << "Arbol exportado a " << filename << std::endl;
}

void BST::exportInorderRecursivo(Nodo* nodo, std::ofstream& archivo) {
    if (nodo == nullptr) return;
    
    exportInorderRecursivo(nodo->left,archivo);
    archivo << nodo->key << " ";
    exportInorderRecursivo(nodo->right,archivo);
}

void BST::remove(int key){
    raiz = eliminarRecursivo(raiz,key);
}

Nodo* BST::eliminarRecursivo(Nodo* nodo, int key) {
    if (nodo == nullptr) return nullptr;
    
    if (key < nodo->key) {
        nodo->left = eliminarRecursivo(nodo->left, key);
    }
    else if (key > nodo->key) {
        nodo->right = eliminarRecursivo(nodo->right, key);
    }
    else {

        if (nodo->left == nullptr && nodo->right == nullptr) {
            delete nodo;
            return nullptr;
        }
        
        else if (nodo->left == nullptr) {
            Nodo* temp = nodo->right;
            delete nodo;
            return temp;
        }
        
        else if (nodo->right == nullptr) {
            Nodo* temp = nodo->left;
            delete nodo;
            return temp;
        }
        
        else {
            Nodo* sucesor = encontrarMinimo(nodo->right);
            nodo->key = sucesor->key;
            nodo->right = eliminarRecursivo(nodo->right, sucesor->key);
        }
    }
    
    return nodo;
}

Nodo* BST::encontrarMinimo(Nodo* nodo) {
    while (nodo->left != nullptr) {
        nodo = nodo->left;
    }
    return nodo;
}

void BST::importFromFile(const std::string& filename) {
    std::ifstream archivo(filename);
    
    if (!archivo.is_open()) {
        std::cerr << "Error: No se pudo abrir el archivo " << filename << std::endl;
        return;
    }
    
    std::string linea;
    int contador = 0;
    
    while (std::getline(archivo, linea)) {
        std::istringstream iss(linea);
        int num;
        
        while (iss >> num) {
            insert(num);
            contador++;
        }
    }
    
    archivo.close();
    std::cout << "Se importaron " << contador << " numeros desde " << filename << std::endl;
}