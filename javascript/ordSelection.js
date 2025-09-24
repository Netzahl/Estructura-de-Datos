function selectionSort(a){
    let small = 0, adicional=0;
    for(let i = 0; i < a.length; i++){
        small = i;
        for(let j=i+1;j<a.length;j++){
            if(a[small]>a[j]){
                small = j;
            }
        }
        adicional = a[small];
        a[small] = a[i];
        a[i] = adicional;
    }
    return a;
}

function printArr(a){
    for(let i=0;i<a.length; i++){
        process.stdout.write(a[i].toString() + " ");
    }
    console.log("");
}

let a = [65,26,13,23,12];

printArr(a);
a = selectionSort(a);
printArr(a);