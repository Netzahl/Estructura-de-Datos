def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    # Contar ocurrencias
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
    
    # Posiciones acumulativas
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Construir array de salida
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    
    # Copiar a array original
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    # Encontrar el máximo para saber el número de dígitos
    max_val = max(arr)
    
    # Aplicar counting sort para cada dígito
    exp = 1
    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    
    return arr

# Ejemplo de uso
if __name__ == "__main__":
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Array original:", arr)
    radix_sort(arr)
    print("Array ordenado:", arr)