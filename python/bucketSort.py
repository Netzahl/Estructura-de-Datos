def inSort(bukt):
    for j in range(1, len(bukt)):
        val = bukt[j]
        k = j - 1
        while k >= 0 and bukt[k] > val:
            bukt[k + 1] = bukt[k]
            k -= 1
        bukt[k + 1] = val

def bucketSort(arr):
    s = len(arr)
    bucketArr = [[] for _ in range(s)]

    for j in arr:
        bi = int(s * j)
        bucketArr[bi].append(j)

    for bukt in bucketArr:
        inSort(bukt)

    idx = 0
    for bukt in bucketArr:
        for j in bukt:
            arr[idx] = j
            idx += 1

arr = [.77, .16, .38, .25, .71, .93, .22, .11, .24, .67]
print("Arreglo desordenado: ")
print(" ".join(map(str, arr)))
bucketSort(arr)
print("Arreglo ordenado: ") 
print(" ".join(map(str, arr)))