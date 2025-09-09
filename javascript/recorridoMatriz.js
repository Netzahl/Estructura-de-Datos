let matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

console.log("Recorrido por fila")

for(let i = 0; i < 3; i++){
    for(let j = 0; j < 3; j++){
    
        console.log(matriz[i][j])

    }
}

console.log("\n")
console.log("Recorrido por columna")

for(let i = 0; i < 3; i++){
    for(let j = 0; j < 3; j++){
    
        console.log(matriz[j][i])

    }
}
