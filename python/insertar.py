import random

array1 = [1,2,3,4,5,6,7,8,9,10]
newArray = []
numeroAdd = random.randint(1,30)
posicion = 5
j = 0

for i in range(len(array1)):
    if i == posicion: 
        newArray.insert(i,numeroAdd)
        j += 1
    else:
        newArray.insert(i,array1[i-j])

for num in newArray:
    print(num)