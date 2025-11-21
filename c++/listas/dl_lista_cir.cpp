#include <iostream>
#include <cstdlib>
#include <new>

using namespace std;

struct node
{
    int data;
    struct node *next;
    struct node *ant;
};

struct node *head = NULL;
struct node *tail = NULL;

void begInsert();
void lastInsert();
void selectInsert();
void beginDelete();
void lastDelete();
void selectDelete();
void display();
void search();

int main()
{
    int choice = 0;
    while (choice != 9)
    {
        cout << "\n**********Menú principal**********\n";
        cout << "Elige una opción de la siguiente lista ...\n";
        cout << "=========================================\n";
        cout << "\n1. Insertar al principio\n2. Insertar al final\n3. Insertar\n4. Eliminar del principio\n"
                "5. Eliminar desde el último\n6. Eliminar nodo después de la ubicación especificada\n"
                "7. Buscar un elemento\n8. Mostrar\n9. Salir\n";
        cout << "\nIngrese su opción\n";
        cin >> choice;

        switch (choice)
        {
        case 1:
            begInsert();
            break;
        case 2:
            lastInsert();
            break;
        case 3:
            selectInsert();
            break;
        case 4:
            beginDelete();
            break;
        case 5:
            lastDelete();
            break;
        case 6:
            selectDelete();
            break;
        case 7:
            search();
            break;
        case 8:
            display();
            break;
        case 9:
            exit(0);
            break;
        default:
            cout << "\nIntroduzca una opción válida..";
        }
    }
    return 0;
}

void begInsert()
{
    struct node *ptr;
    int item;

    ptr = new (nothrow) node;

    if (ptr == NULL)
    {
        cout << "\nOVERFLOW";
    }
    else
    {
        cout << "\nIngrese valor\n";
        cin >> item;

        ptr->data = item;

        if (head == NULL) 
        {
            tail = ptr;
            ptr->next = ptr;
            ptr->ant = ptr;
        }
        else
        {
            ptr->next = head;
            ptr->ant = tail;
            head->ant = ptr;
            tail->next = ptr;
        }

        head = ptr;

        cout << "\nNodo insertado";
    }
}

void lastInsert()
{
    struct node *ptr;
    int item;

    ptr = new (nothrow) node;

    if (ptr == NULL)
    {
        cout << "\nOVERFLOW";
    }
    else
    {
        cout << "\nIngrese valor:\n";
        cin >> item;
        ptr->data = item;

        if (head == NULL)
        {
            head = ptr;
            ptr->next = ptr;
            ptr->ant = ptr;
        }
        else
        {
            tail->next = ptr;
            head->ant = ptr;
            ptr->ant = tail;
            ptr->next = head;
        }
        tail = ptr;
        cout << "\nNodo insertado";
    }
}

void selectInsert()
{
    int i, loc, item;
    struct node *ptr, *temp;
    ptr = new (nothrow) node;
    if (ptr == NULL)
    {
        cout << "\nOVERFLOW";
    }
    else
    {
        cout << "\nIntroduzca el valor del elemento\n";
        cin >> item;
        ptr->data = item;

        cout << "\nIntroduce la ubicación despues de la cual deseas ingresar\n";
        cin >> loc;

        if (loc <= 0)
        {
            cout << "\nUbicación no válida. Debe ser 1 o mayor.";
            delete ptr;
            return;
        }

        temp = head;

        if (temp == NULL)
        {
            cout << "\nNo se puede insertar";
            delete ptr;
            return;
        }

        for (i = 1; i < loc; i++)
        {
            temp = temp->next;
            if (temp == head)
            {
                cout << "\nNo se puede insertar";
                delete ptr;
                return;
            }
        }

        ptr->next = temp->next;
        temp->next = ptr;
        ptr->ant = temp;

        if(ptr->next == head){
            tail = ptr;
        }

        ptr->next->ant = ptr;

        cout << "\nNodo insertado";
    }
}

void beginDelete()
{
    struct node *ptr;

    if (head == NULL)
    {
        cout << "\nLa lista esta vacia";
    }
    else if(head->next == head){
        delete head;
        head = NULL;
        tail = NULL;
        cout << "\nUnico nodo eliminado ...";
    }
    else
    {
        ptr = head;
        head = ptr->next;
        head->ant = tail;
        tail->next = head;
        delete ptr;
        cout << "\nPrimer nodo eliminado ...";
    }
}

void lastDelete()
{
    struct node *ptr;

    if (head == NULL)
    {
        cout << "\nLa lista esta vacia";
    }
    else if (tail->ant == tail)
    {
        delete tail;
        head = NULL;
        tail = NULL;
        cout << "\nSe elimino el unico nodo de la lista ...";
    }
    else
    {
        ptr = tail;
        tail = tail->ant;
        tail -> next = head;
        delete ptr;
        cout << "\nUltimo nodo eliminado ...";
    }
}

void selectDelete()
{
    struct node *ptr, *ptr1;
    int loc, i;
    cout << "\nIntroduzca la ubicacion del nodo despues del cual desea realizar la eliminacion. \n";
    cin >> loc;

    if (head == NULL)
    {
        cout << "\nLista vacia, no se puede eliminar";
        return;
    }

    if (loc <= 0)
    {
        cout << "\nLa ubicación debe ser 1 o mayor.";
        return;
    }

    ptr = head;
    for (i = 0; i < loc; i++)
    {
        ptr1 = ptr;
        ptr = ptr->next;

        if (ptr == head)
        {
            cout << "\nNo se puede eliminar, ubicacion no encontrada";
            return;
        }
    }
    ptr1->next = ptr->next;
    ptr->next->ant = ptr1;

    if(ptr->next == head){
        tail = ptr1;
    }

    delete ptr;
    cout << "\nNodo eliminado " << loc + 1;
}

void search()
{
    struct node *ptr;
    int item, i = 0;
    bool flag = false;
    ptr = head;

    if (ptr == NULL)
    {
        cout << "\nLista vacia";
    }
    else
    {
        cout << "\nIntroduce el elemento que deseas buscar?\n";
        cin >> item;

        do
        {
            if (ptr->data == item) 
            {
                cout << "\nElemento encontrado en la ubicacion " << i + 1;
                flag = true;
            }
            i++;
            ptr = ptr->next;
        }while(ptr != head);

        if (flag == false)
        {
            cout << "\nElemento no encontrado";
        }
    }
}

void display()
{
    struct node *ptr;
    ptr = head;

    if (ptr == NULL)
    {
        cout << "\nNada que imprimir";
    }
    else
    {
        cout << "\nImprimiendo valores . . . . . . \n";
        do
        {
            cout << ptr->data << "\n";
            ptr = ptr->next;
        }while(ptr != head);
    }
}
