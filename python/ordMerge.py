def merge(a,l,m, r):
    a1 = m - l + 1
    a2 = r - m

    L = [0] * (a1)
    R = [0] * (a2)

    for j in range(0,a1):
        L[j] = a[l + j]
    for k in range(0,a2):
        R[k] = a[m + 1 + k]
    i = 0
    j = 0
    k = l

    while i < a1 and j < a2:
        if L[i] <= R[j]:
            a[k] = L[i]
            i = i + 1
        else:
            a[k] = R[j]
            j = j + 1
        k = k + 1

    while i < a1:
        a[k] = L[i]
        i = i + 1
        k = k + 1

    while j < a2:
        a[k] = R[j]
        j = j + 1
        k = k + 1

def mergeSort(a, l, r):
    if l  <  r:
        m = l + (r - l)//2
        mergeSort(a, l, m)
        mergeSort(a,m+1,r)
        merge(a,l,m,r)

a = [39, 28, 44, 11]
s = len(a)
print("Antes de ordenar: ")
for j in range(s):
    print("%d" % a[j], end=" ")
mergeSort(a,0,s-1)
print("\nDespues de ordenar: ")
for j in range(s):
    print("%d" % a[j], end=" ")

