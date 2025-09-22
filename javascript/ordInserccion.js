function insertionSort(a){
    let temp = 0, j=0;
    for(let i = 1; i < a.length; i++){
        temp = a[i];
        j = i-1;
        while(j>=0 && temp<a[j]){
            a[j+1] = a[j];
            j--;
        }
        a[j+1] = temp;
    }
    return a;
}

function printArr(a){
    for(let i=0;i<a.length; i++){
        process.stdout.write(a[i].toString() + " ");
    }
    console.log("");
}

let a = [70, 15, 2, 51, 60];

printArr(a);
a = insertionSort(a);
printArr(a);