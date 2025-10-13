//Inicializamos kaboom
const k = kaboom({
    width: 640,
    height: 640,
    scale: 1,
    clearColor: [0.1, 0.1, 0.2, 1]
});

//Declaramos el laberinto y lo construimos, 0 = camino, 1 = pared
const laberinto = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 3, 1, 0, 0, 0, 5, 1],
    [1, 0, 1, 0, 1, 4, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 3, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
];

const tamCelda = 64;

k.loadSprite("puerta", "images/puerta.png");
k.loadSprite("puertaAbierta", "images/puertaAbierta.png");
k.loadSprite("llave", "images/llave.png");
k.loadSprite("pared", "images/pared.png");
k.loadSprite("trampa", "images/trampa.png");
k.loadSprite("portal", "images/portal.png");

let llaves = 0;
let celdasVisibles = new Set();
let celdasExploradas = new Set();

//Funcion para dibujar el laberinto
function dibujarLaberinto(){
    const filas = laberinto.length
    const columnas = laberinto[0].length

    for(let i=0; i<filas; i++){
        for(let j=0; j<columnas; j++){
            const x = j * tamCelda;
            const y = i * tamCelda;

            switch(laberinto[i][j]){
                //Dibujamos caminos
                case 0:
                    k.add([
                        k.rect(tamCelda,tamCelda),
                        k.pos(x,y),
                        k.color(200, 200, 200),
                        "camino"
                    ]);
                break;
                //Dibujamos paredes
                case 1:
                    k.add([
                        k.sprite("pared",{with: 64, height: 64}),
                        k.pos(x,y),
                        k.area(),
                        k.body({isStatic: true}),
                        "pared"
                    ]);
                break;

                //Dibujamos trampas
                case 2:
                    k.add([
                        k.sprite("trampa", { width: 64, height: 64 }),
                        k.pos(x, y),
                        k.area(),
                        "trampa"
                    ]);
                break;
                
                //Dibujamos llaves
                case 3:

                    k.add([
                        k.rect(tamCelda,tamCelda),
                        k.pos(x,y),
                        k.color(200, 200, 200),
                        "camino"
                    ]);

                    k.add([
                        k.sprite("llave", {width: 60, height: 60}),
                        k.pos(x + tamCelda/2, y + tamCelda/2),
                        k.anchor("center"),
                        k.area({scale: .4}),
                        "llave"
                    ]);

                break;

                //Dibujamos puertas
                case 4:

                    k.add([
                        k.rect(tamCelda, tamCelda),
                        k.pos(x, y),
                        k.color(200, 200, 200),
                        "camino"
                    ]);
    
                    k.add([
                        k.sprite("puerta", { width: 64, height: 64 }),
                        k.pos(x + tamCelda/2, y + tamCelda/2),
                        k.anchor("center"),
                        k.area(),
                        k.body({isStatic: true}),
                        "puerta"
                    ]);

                break;

                //Dibujamos el portal de nivel
                case 5:

                    k.add([
                        k.sprite("portal", { width: 64, height: 64 }),
                        k.pos(x, y),
                        k.area(),
                        "portal"
                    ]);

                break;

                default:
                break;
            }
        }
    }
}

//Funcion para oscurecer el mapa
function dibujarOscuridad(){
    
    const columnas = laberinto.length;
    const filas = laberinto[0].length;

    for(let i = 0; i < columnas; i++){
        for(let j = 0; j < filas; j++){
            const x = j * tamCelda;
            const y = i * tamCelda;
            const id = `${i}-${j}`;

            const oscuridad = k.add([
                k.rect(tamCelda,tamCelda),
                k.pos(x,y),
                k.color(0,0,0),
                k.opacity(1),
                k.z(50),
                "oscuridad",
                {
                    celdaid: id,
                    celdaX: j,
                    celdaY: i,
                    explorada: false
                }
            ]);
        }
    }
}

function dibujarCampoVision(posicion){
    const radioVision = 57;
    celdasVisibles.clear();

    k.get("oscuridad").forEach(oscuridad => {
        
        const centroX = oscuridad.celdaX * tamCelda + tamCelda / 2;
        const centroY = oscuridad.celdaY * tamCelda + tamCelda / 2;
        const distancia = Math.sqrt(Math.pow(posicion.x - centroX, 2) + Math.pow(posicion.y - centroY, 2));
        const id = oscuridad.celdaid;

        if(distancia < radioVision){
            celdasVisibles.add(id);
            
            if(oscuridad.explorada != true){
                oscuridad.explorada = true;
                celdasExploradas.add(id);
            }
            oscuridad.opacity = 0;
        }
        else if(celdasExploradas.has(id)){
            oscuridad.opacity = 0.3;
        }
        else{
            oscuridad.opacity = 1;
        }
        
    });

}

//Cargamos imagen del jugador
k.loadSprite("magordito", "images/magordito.png");

//Cargamos al jugador
function agregarJugador(){
    const jugador = k.add([
        k.sprite("magordito",{ width: 50, height: 50 }),
        k.pos(tamCelda + tamCelda/2, tamCelda + tamCelda/2),
        k.anchor("center"),
        k.area({
            shape: new k.Rect(k.vec2(-1, 0), 42, 46) 
        }),
        k.body({gravityScale: 0}),
        k.scale(1),
        k.z(5),
        k.health(3),
        "jugador"
    ]);
        
    //Definimos los controles del jugador
    const velocidad = 300;

    k.onKeyDown("a", () => {
        jugador.move(-velocidad,0);
    });

    k.onKeyDown("d", () => {
        jugador.move(velocidad,0);
    });

    k.onKeyDown("w", () => {
        jugador.move(0,-velocidad);
    });

    k.onKeyDown("s", () => {
        jugador.move(0,velocidad);
    });

    //Definimos interacciones del jugador

    //Colision con llaves
    jugador.onCollide("llave", (llave) => {
        k.destroy(llave);
        llaves++;
    });

    //Colision con puertas
    jugador.onCollide("puerta", (puerta) => {
        if(llaves > 0){
            const x = puerta.pos.x - puerta.width / 2;
            const y = puerta.pos.y - puerta.height / 2;

            k.destroy(puerta);

            k.add([
                k.sprite("puertaAbierta", { width: 64, height: 64 }),
                k.pos(x + tamCelda/2, y + tamCelda/2),
                k.anchor("center"),
                "puertaAbierta"
            ]);

            llaves--;
        }
    });

    //Colision con trampas
    jugador.onCollide("trampa", (trampa) => {
        jugador.hurt(1);

        const color = jugador.color;
        for(let i = 0; i < 3; i++){
            k.wait(i * 0.2, () => [
                jugador.color = k.rgb(255, 0, 0)
            ]);

            k.wait(i * 0.2 + 0.1, () => {
            jugador.color = color
            });
        }
        jugador.color = color;

    });

    //Colision con portal
    jugador.onCollide("portal", () => {
        go("ganar");
    })

    //Eventos de jugador

    //Evento de muerte
    jugador.on("death", () => {
    destroy(jugador)
    go("perder")
    })

    //Definimos el campo de vision
    k.onUpdate(() => {
        dibujarCampoVision(jugador.pos);
    });

}

//Definimos el escenario de juego
k.scene("juego", () => {
    llaves = 0;
    celdasExploradas = new Set();
    dibujarLaberinto();
    dibujarOscuridad();
    agregarJugador();
});

//Definimos el escenario de perder
k.scene("perder", () => {

    k.add([
        k.rect(k.width(), k.height()),
        k.pos(0, 0),
        k.color(20, 20, 30), 
        k.z(-100) 
    ]);

    k.add([
        k.text("¡PERDISTE!", { size: 48 }),
        k.pos(k.width()/2, k.height()/2 - 50),
        k.anchor("center"),
        k.color(255, 0, 0)
    ]);
    
    k.add([
        k.text("Presiona ESPACIO para reintentar", { size: 24 }),
        k.pos(k.width()/2, k.height()/2 + 50),
        k.anchor("center"),
        k.color(255, 255, 255)
    ]);

    k.onKeyPress("space", () => {
        k.go("juego");
    });
});

//Definimos el escenario de ganar
k.scene("ganar", () => {

    k.add([
        k.rect(k.width(), k.height()),
        k.pos(0, 0),
        k.color(20, 20, 30), 
        k.z(-100) 
    ]);

    k.add([
        k.text("¡Ganaste!", { size: 48 }),
        k.pos(k.width()/2, k.height()/2 - 50),
        k.anchor("center"),
        k.color(255, 0, 0)
    ]);
    
    k.add([
        k.text("Presiona ESPACIO volver a jugar", { size: 24 }),
        k.pos(k.width()/2, k.height()/2 + 50),
        k.anchor("center"),
        k.color(255, 255, 255)
    ]);
    
    k.onKeyPress("space", () => {
        k.go("juego");
    });
});

//Declaramos la funcion principal
function main(){
    go("juego");
}

main();

