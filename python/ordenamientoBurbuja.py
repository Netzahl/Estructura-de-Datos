array = [56,45,25,86,5,54,12,79,32]

print(array)
adicional = 0
j=len(array)
cambio = True
while True:
    cambio = False
    for i in range(1,j):
        if array[i-1] > array[i]:
            adicional = array[i-1]
            array[i-1] = array[i]
            array[i] = adicional
            cambio = True
    j-=1
    if cambio == False:
        break
print(array)