let array = [10];
let numBuscado = Math.floor(Math.random()*30 + 1)
let posicion = 0;
let bandera = false;

for (let i= 0;i<10;i++){
    array[i]= Math.floor(Math.random()*30 + 1)
}

for (let i= 0; i<10;i++){
    if(array[i]==numBuscado){
        bandera = true;
        posicion = i+1;
    }
}

if(bandera==true){
    console.log("El numero "+numBuscado+", fue encontrado en la posicion "+posicion+" del array");
}
else{
    console.log("El numero "+numBuscado+", no fue encontrado en el array");
}