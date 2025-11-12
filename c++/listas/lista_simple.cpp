#include <iostream>
#include <cstdlib>
#include <new>

using namespace std;

struct node
{
    int data;
    struct node *next;
};

struct node *head;

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
        ptr->next = head;
        head = ptr;
        cout << "\nNodo insertado";
    }
}

void lastInsert()
{
    struct node *ptr, *temp;
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
        ptr->next = NULL;

        if (head == NULL)
        {
            head = ptr;
            cout << "\nNodo ingresado";
        }
        else
        {
            temp = head;
            while (temp->next != NULL)
            {
                temp = temp->next;
            }
            temp->next = ptr;
            cout << "\nNodo insertado";
        }
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

        temp = head;

        if(temp == NULL)
        {
            cout << "\nNo se puede insertar";
            return;
        }

        for (i = 1; i < loc; i++)
        {
            temp = temp->next;
            if (temp == NULL)
            {
                cout << "\nNo se puede insertar";
                return;
            }
        }
        ptr->next = temp->next;
        temp->next = ptr;
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
    else
    {
        ptr = head;
        head = ptr->next;
        delete ptr;
        cout << "\nPrimer nodo eliminado ...";
    }
}

void lastDelete()
{
    struct node *ptr, *ptr1;

    if (head == NULL)
    {
        cout << "\nLa lista esta vacia";
    }
    else if(head->next == NULL)
    {
        delete head;
        head = NULL;
        cout << "\nSolo se elimino el unico nodo de la lista ...";
    }
    else
    {
        ptr = head;
        while(ptr->next != NULL)
        {
            ptr1 = ptr;
            ptr = ptr->next;
        }
        ptr1->next = NULL;
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
    ptr = head;
    for (i = 0; i<loc; i++)
    {
        ptr1 = ptr;
        ptr = ptr->next;

        if(ptr == NULL)
        {
            cout << "\nNo se puede eliminar";
            return;
        }
    }
    ptr1->next = ptr->next;
    delete ptr;
    cout << "\nNodo eliminado " << loc + 1;
}

void search()
{
    struct node *ptr;
    int item, i=0;
    bool flag = false;
    ptr = head;

    if(ptr == NULL)
    {
        cout << "\nLista vacia";
    }
    else
    {
        cout << "\nIntroduce el elemento que deseas buscar?\n";
        cin >> item;

        while(ptr != NULL)
        {
            if(ptr->data == item)
            {
                cout << "\nElemento encontrado en la ubicacion " << i + 1;
                flag = true;
            }
            i++;
            ptr = ptr->next;
        }
        if(flag == false)
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
        cout << "\nNada que imptrimir";
    }
    else
    {
        cout << "\nImprimiendo valores . . . . . . \n";
        while (ptr != NULL)
        {
            cout << ptr->data << "\n";
            ptr = ptr->next;
        }
    }
}

