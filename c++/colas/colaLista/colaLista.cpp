#include <iostream>
using namespace std;

struct node
{
    int data;
    struct node *next = NULL;
};

struct node *head, *tail;

void insertar()
{
    struct node *ptr;
    int elemento;
    
    cout << "\nIngrese el elemento: ";
    cin >> elemento;

    ptr = new (nothrow) node;

    if(ptr == NULL){
        cout << "\nDESBORDAMIENTO  (OVERFLOW)\n";
        return;
    }
    if(head == NULL && tail == NULL){
        head = tail = ptr;
    } else {
        tail->next = ptr;
        tail = ptr;
    }
    ptr->data = elemento;
    cout << "\nElemento insertado correctamente.\n";
}
void eliminar(){
    if(head == NULL){
        cout << "\nSUBDESBORDAMIENTO (UNDERFLOW)\n";
        return;
    }
    int elemento = head->data;
    if(head == tail){
        head = tail = NULL;
    }else {
        head = head->next;
    }
    cout << "\nElemento eliminado: " << elemento << "\n";
}
void mostrar(){
    struct node *ptr;
    ptr = head;

    if (ptr == NULL)
    {
        cout << "\nNada que imptrimir";
    }
    else
    {
        cout << "\nImprimiendo valores . . . . . . \n";
        while (ptr != NULL)
        {
            cout << ptr->data;
            if(ptr != tail){
                cout << " | ";
            }
            ptr = ptr->next;
        }
    }
}

int main() {
    int opcion = 0;
    
    while (opcion != 4) {
        cout << "\n****************** MENÚ PRINCIPAL ******************\n";
        cout << "====================================================\n";
        cout << "1. Insertar un elemento\n";
        cout << "2. Eliminar un elemento\n";
        cout << "3. Mostrar la cola\n";
        cout << "4. Salir\n";
        cout << "Ingrese su opción: ";
        cin >> opcion;
        
        switch (opcion) {
            case 1:
                insertar();
                break;
            case 2:
                eliminar();
                break;
            case 3:
                mostrar();
                break;
            case 4:
                cout << "\nSaliendo del programa...\n";
                break;
            default:
                cout << "\nOpción inválida. Intente nuevamente.\n";
        }
    }
    
    return 0;
}