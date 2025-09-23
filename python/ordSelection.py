def selection(a):
    for i in range(len(a)): #Recorre el array n()
        small = i 
        for j in range(i+1, len(a)): #Recorre en busca del numero mas pequeño
            if a[small] > a[j]: #Selecciona el numero mas pequeño
                small = j
        a[i],a[small] = a[small], a[i] #Intercambia posiciones.

def printArr(a):
    print (*a)

a = [65,26,13,23,12]

printArr(a)
selection(a)
printArr(a)

