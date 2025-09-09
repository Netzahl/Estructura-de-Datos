import random

array = [1,2,3,4,5,6,7,8,9,10]
numeroBus = random.randint(1,20)
bandera = False
posic = 0

for i in range(len(array)):
    if array[i] == numeroBus:
        bandera = True
        posic = i+1

if bandera == True:
    print(f"El numero {numeroBus}, fue encontrado en la posicion {posic} del array")
else:
    print(f"El numero {numeroBus}, no fue encontrado dentro del array")
