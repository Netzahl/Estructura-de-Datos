class Hashell
{
    static DisplayArr(arr)
    {
        let resultado = "";
        for(let x of arr){
            resultado += x + " ";
        }
        console.log(resultado);
    }
    
    Sort(arr)
    {
        const size = arr.length;    
        let gapsize = Math.floor(size/2)
        while(gapsize > 0)
        {
            for(let j = gapsize; j < size; j++)
            {
                let val = arr[j];
                let k = j;
                while(k >= gapsize && arr[k - gapsize] > val)
                {
                    arr[k] = arr[k - gapsize];
                    k -= gapsize;
                }
                arr[k] = val;
            }
            gapsize = Math.floor(gapsize / 2);
        }
        return 0;
    }
}

let arr = [36, 34, 43, 11, 15, 20, 28, 45];

console.log("Arreglo desordenado: ");
Hashell.DisplayArr(arr);
const obj = new Hashell();
obj.Sort(arr);
console.log("Arreglo ordenado: ");
Hashell.DisplayArr(arr);