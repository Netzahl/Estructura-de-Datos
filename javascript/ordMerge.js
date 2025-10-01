function merge(a,l,m,r){
    let a1 = m - l + 1;
    let a2 = r - m;
    let L = [];
    let R = [];

    let i = l;
    let j = m+1;

    for(let h = 0; h < a1; h++){
        L[h] = a[i];
        i++;
    }

    for(let h = 0; h < a2; h++){
        R[h] = a[j];
        j++;
    }

    i = 0;
    j = 0;
    let k = l;

    while(i < a1 && j < a2){
        if(L[i] <= R[j]){
            a[k] = L[i];
            i++;
        }
        else
        {
            a[k] = R[j];
            j++;
        }
        k++;
    }

    while(i<a1){
        a[k] = L[i];
        i++;
        k++;
    }

    while(j<a2){
        a[k] = R[j];
        j++;
        k++;
    }
}

function mergeSort(a,l,r){
    if(l < r){
        let m = l + Math.trunc((r-l)/2);
        mergeSort(a,l,m);
        mergeSort(a,m+1,r);
        merge(a,l,m,r);
    }
}

function show(a){
    a.forEach(x => {
        process.stdout.write(x.toString() + " ");
    });
    console.log();
}

let a = [45, 67, 12, 5, 89, 4, 27, 48, 65, 19, 75];
let tamaño = a.length;
console.log("Antes de ordenar: ");
show(a);
mergeSort(a, 0, tamaño-1);
console.log("Despues de ordenar: ");
show(a);