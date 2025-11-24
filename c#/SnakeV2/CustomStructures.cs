using System;
using System.Collections;
using System.Collections.Generic;
using System.Numerics; // Necesario para comparar Vector2

namespace SnakeGame
{
    // Requisito 3 y 4: Estructuras de datos personalizadas basadas en Nodos

    public class Node<T>
    {
        public T Data { get; set; }
        public Node<T>? Next { get; set; }

        public Node(T data)
        {
            Data = data;
            Next = null;
        }
    }

    public class CustomLinkedList<T> : IEnumerable<T>
    {
        public Node<T>? Head { get; private set; }
        public Node<T>? Tail { get; private set; }
        public int Count { get; private set; }

        public void Add(T data)
        {
            Node<T> newNode = new Node<T>(data);
            if (Head == null)
            {
                Head = newNode;
                Tail = newNode;
            }
            else
            {
                Tail!.Next = newNode;
                Tail = newNode;
            }
            Count++;
        }

        public void AddFirst(T data)
        {
            Node<T> newNode = new Node<T>(data);
            newNode.Next = Head;
            Head = newNode;
            if (Tail == null) Tail = Head;
            Count++;
        }

        public void RemoveLast()
        {
            if (Head == null) return;

            if (Head == Tail)
            {
                Head = null;
                Tail = null;
            }
            else
            {
                Node<T> current = Head;
                while (current.Next != Tail)
                {
                    current = current.Next!;
                }
                current.Next = null;
                Tail = current;
            }
            Count--;
        }
        
        /// <summary>
        /// Busca y elimina el nodo que contiene el elemento dataToRemove de la lista.
        /// Utiliza la igualdad de valor (structs) o la igualdad de referencia (clases como GameElement).
        /// </summary>
        public bool Remove(T dataToRemove)
        {
            if (Head == null) return false;
            
            // Si dataToRemove es null (aunque T sea nullable) se lanza una excepción.
            // Usamos ! para indicar al compilador que dataToRemove no es null en este punto.
            
            // 1. Manejar la cabeza
            if (dataToRemove!.Equals(Head.Data))
            {
                Head = Head.Next;
                if (Head == null) Tail = null;
                Count--;
                return true;
            }

            // 2. Manejar el cuerpo
            Node<T>? current = Head.Next;
            Node<T>? previous = Head;
            while (current != null)
            {
                if (dataToRemove!.Equals(current.Data))
                {
                    previous!.Next = current.Next;
                    if (current == Tail) Tail = previous;
                    Count--;
                    return true;
                }
                previous = current;
                current = current.Next;
            }

            return false; 
        }

        public void Clear()
        {
            Head = null;
            Tail = null;
            Count = 0;
        }

        // Iterador para poder usar foreach
        public IEnumerator<T> GetEnumerator()
        {
            Node<T>? current = Head;
            while (current != null)
            {
                yield return current.Data;
                current = current.Next;
            }
        }

        IEnumerator IEnumerable.GetEnumerator()
        {
            return GetEnumerator();
        }

        // Indexador para acceso fácil (O(n) - ineficiente pero necesario para listas enlazadas simples)
        public T this[int index]
        {
            get
            {
                if (index < 0 || index >= Count) throw new IndexOutOfRangeException();
                Node<T> current = Head!;
                for (int i = 0; i < index; i++)
                {
                    current = current.Next!;
                }
                return current.Data;
            }
        }
    }
}