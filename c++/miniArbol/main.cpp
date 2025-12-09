#include <iostream>
#include "bst.h"
#include <sstream>
#include <string>

void mostrarMenu()
{
    std::cout << "\n=== GESTOR BST ===" << std::endl;
    std::cout << "insert <num>  - Insertar numero" << std::endl;
    std::cout << "search <num>  - Buscar numero" << std::endl;
    std::cout << "delete <num>  - Eliminar numero" << std::endl;
    std::cout << "inorder       - Mostrar recorrido inorden" << std::endl;
    std::cout << "preorder      - Mostrar recorrido preorden" << std::endl;
    std::cout << "postorder     - Mostrar recorrido postorden" << std::endl;
    std::cout << "height        - Mostrar altura del arbol" << std::endl;
    std::cout << "size          - Mostrar numero de nodos" << std::endl;
    std::cout << "export <file> - Exportar inorden a archivo" << std::endl;
    std::cout << "import <file> - Importar numeros desde archivo" << std::endl;
    std::cout << "help          - Mostrar este menu" << std::endl;
    std::cout << "exit          - Salir" << std::endl;
}

int main()
{
    BST arbol;
    std::string linea, comando;

    std::cout << "Gestor de Arbol Binario de Busqueda" << std::endl;
    std::cout << "Escribe 'help' para ver comandos disponibles" << std::endl;

    while (true)
    {
        std::cout << "\n> ";
        std::getline(std::cin, linea);

        if (linea.empty())
            continue;

        std::istringstream iss(linea);
        iss >> comando;

        if (comando == "exit")
        {
            std::cout << "Saliendo..." << std::endl;
            break;
        }
        else if (comando == "help")
        {
            mostrarMenu();
        }
        else if (comando == "insert")
        {
            int num;
            if (iss >> num)
            {
                arbol.insert(num);
                std::cout << "Insertado: " << num << std::endl;
            }
            else
            {
                std::cout << "Error: Debes especificar un numero" << std::endl;
            }
        }
        else if (comando == "search")
        {
            int num;
            if (iss >> num)
            {
                bool encontrado = arbol.search(num);
                std::cout << num << (encontrado ? " EXISTE" : " NO EXISTE") << std::endl;
            }
            else
            {
                std::cout << "Error: Debes especificar un numero" << std::endl;
            }
        }
        else if (comando == "inorder")
        {
            std::cout << "Inorder: ";
            arbol.inorder();
        }
        else if (comando == "preorder")
        {
            std::cout << "Preorder: ";
            arbol.preorder();
        }
        else if (comando == "postorder")
        {
            std::cout << "Postorder: ";
            arbol.postorder();
        }
        else if (comando == "height")
        {
            std::cout << "Altura: " << arbol.height() << std::endl;
        }
        else if (comando == "size")
        {
            std::cout << "Nodos: " << arbol.size() << std::endl;
        }
        else if (comando == "export")
        {
            std::string archivo;
            if (iss >> archivo)
            {
                arbol.exportInorder(archivo);
            }
            else
            {
                std::cout << "Error: Debes especificar nombre de archivo" << std::endl;
            }
        }
        else if (comando == "delete")
        {
            int num;
            if (iss >> num)
            {
                arbol.remove(num);
                std::cout << "Eliminado: " << num << std::endl;
            }
            else
            {
                std::cout << "Error: Debes especificar un numero" << std::endl;
            }
        }
        else if (comando == "import")
        {
            std::string archivo;
            if (iss >> archivo)
            {
                arbol.importFromFile(archivo);
            }
            else
            {
                std::cout << "Error: Debes especificar nombre de archivo" << std::endl;
            }
        }
        else
        {
            std::cout << "Comando desconocido. Escribe 'help' para ver comandos." << std::endl;
        }
    }

    return 0;
}