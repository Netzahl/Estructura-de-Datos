function Insort(bukt)
{
    for(let i = 0; i < bukt.length; i++)
    {
        let val = bukt[i];
        let k = i - 1;
        while(k >= 0 && bukt[k] > val)
        {
            bukt[k + 1] = bukt[k];
            k--;
        }
        bukt[k + 1] = val;
    }
}

function BucketSort(arr)
{
    let s = arr.length;
    let buckets = [];

    for (let i = 0; i < s; i++)
    {
        buckets.push([]);
    }

    for (let j of arr)
    {
        let bi = Math.floor(s * j);
        buckets[bi].push(j);
    }

    for (let i = 0; i < s; i++)
    {
        Insort(buckets[i]);
    }

    let idx = 0;
    for(let i = 0; i < s; i++)
    {
        for(let j = 0; j < buckets[i].length; j++)
        {
            arr[idx] = buckets[i][j];
            idx++;
        }
    }
}

let arr = [.77, .16, .38, .25, .71, .93, .22, .11, .24, .67];

console.log("Arreglo desordenado: ");
console.log(arr.join(" "));
BucketSort(arr);
console.log("Arreglo ordenado: ");
console.log(arr.join(" "));
