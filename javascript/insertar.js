let numeros = [1,2,3,4,5,6,7,8,9,10];
let numRandom = Math.floor(Math.random() * 100) + 1;
let posicion = 5;
let newNumeros = [10];
let j=0;

for(let i=0;i<10;i++){
    
    if(i == posicion){
        newNumeros[i] = numRandom;
        j++;
    }
    else{
        newNumeros[i] = numeros[i - j];
    }

}

newNumeros.forEach(num => {
    console.log(num)
});