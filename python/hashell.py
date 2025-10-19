class ShellSort:
    
    @staticmethod
    def DisplayArr(arr):
        for k in arr:
            print(k,end=" ")
        print()

    def sort(self, arr):
        size = len(arr)
        gapsize = size // 2

        while gapsize > 0:

            for j in range(gapsize, size):
                val = arr[j]
                k = j

                while k >= gapsize and arr[k - gapsize] > val:
                    arr[k] = arr[k - gapsize]
                    k = k - gapsize
                
                arr[k] = val

            gapsize = gapsize // 2

        return 0
    
if __name__ == "__main__":
    arr = [36,34,43,11,15,20,28,45]
    print("Arreglo desordenado: ")
    ShellSort.DisplayArr(arr)
    obj = ShellSort()
    obj.sort(arr)
    print("Arreglo ordenado: ")
    ShellSort.DisplayArr(arr)



