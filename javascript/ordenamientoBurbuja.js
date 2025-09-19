let numeros = [12,56,48,52,78,62,23,2,95];
let adicional = 0;

for(let i = 0; i < numeros.length; i++){
    process.stdout.write(numeros[i] + " ");
}

let cambio = true;
let j = numeros.length;
do{
    cambio = false;
    for(let i=1;i<j;i++){
        if(numeros[i-1] > numeros[i]){
            adicional = numeros[i-1];
            numeros[i-1] = numeros[i];
            numeros[i] = adicional
            cambio = true;
        }
    }
    j--;
}while(cambio);

console.log("")
for(let i = 0; i < numeros.length; i++){
    process.stdout.write(numeros[i] + " ");
}