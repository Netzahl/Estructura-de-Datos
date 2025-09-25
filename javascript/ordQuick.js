function swap(a,k,j){
    let adicional = a[k];
    a[k] = a[j];
    a[j] = adicional;
    return a;
}

function partition(a,l,h){
    let pvt = a[h];
    let j = l-1;

    for(let k=l;k<h;k++){
        if(a[k] < pvt){
            j++;
            a = swap(a,k,j);
        }
    }
    a = swap(a,h,j+1)
    j++
    return {a, j};
}

function qckSort(a,l,h){
    if(l<h){
        let {a : arr, j : piv} = partition(a,l,h);
        
        a = qckSort(arr,l,piv-1);
        a = qckSort(arr,piv+1,h);
    }
    return a;
}

function show(a){
    a.forEach(x => {
        process.stdout.write(x.toString() + " ");
    });
    console.log();
}

let a = [10, 7, 8, 9, 1, 5];
let l = 0;
let h = a.length-1;
show(a);
a = qckSort(a,l,h)
show(a);

