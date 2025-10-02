function heapSort(a, h){
    let adicional=0;
    let j = 0;
    while(h>=0){
        for(let i = h; i >=0; i--){
            j = Math.trunc(i/2);
            if(a[i] > a[j]){
                adicional = a[i];
                a[i] = a[j];
                a[j] = adicional;
            }
        }
        adicional = a[0];
        a[0] = a[h];
        a[h] = adicional;
        h--;
    }
}

function show(a){
    a.forEach(x => {
        process.stdout.write(x.toString() + " ");
    });
    console.log();
}

let a = [12, 94, 32, 5, 48, 64, 26, 57];
let tamaño = a.length;

console.log("Antes de ordenar: ");
show(a);
heapSort(a, tamaño-1);
console.log("Despues de ordenar: ");
show(a);
