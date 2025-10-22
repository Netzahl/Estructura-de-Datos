//Inicializamos kaboom
const k = kaboom({
    width: 800,
    height: 640,
    scale: 1,
    clearColor: [0.1, 0.1, 0.2, 1]
});

let nivelActual = 1;
let puntuacion = 0;
const MAX_NIVELES = 5;

function crearLaberinto(nivel) {
    const FILAS = 25;
    const COLUMNAS = 25;
    const PARED = 1;
    const CAMINO = 0;  

    let lab = Array.from({ length: FILAS }, () => Array(COLUMNAS).fill(PARED));

    const esValida = (r, c) => r >= 0 && r < FILAS && c >= 0 && c < COLUMNAS;

    let paredes = [];

    let inicioR = 1 + 2 * Math.floor(Math.random() * ((FILAS - 2) / 2));
    let inicioC = 1 + 2 * Math.floor(Math.random() * ((COLUMNAS - 2) / 2));

    lab[inicioR][inicioC] = CAMINO;

    const vecinos = [[0, 1], [0, -1], [1, 0], [-1, 0]];
    for (const [dr, dc] of vecinos) {
        const nr = inicioR + dr;
        const nc = inicioC + dc;
        if (esValida(nr, nc)) {
            paredes.push({ r: nr, c: nc, de: { r: inicioR, c: inicioC } }); 
        }
    }

    while (paredes.length > 0) {
        
        const index = Math.floor(Math.random() * paredes.length);
        const pared = paredes[index];
        paredes.splice(index, 1); 

        const r = pared.r;
        const c = pared.c;
        const deR = pared.de.r;
        const deC = pared.de.c;

        
        const dr = r - deR;
        const dc = c - deC;
        const opuestaR = r + dr;
        const opuestaC = c + dc;

        
        if (esValida(opuestaR, opuestaC) && lab[opuestaR][opuestaC] === PARED) {
            
            lab[r][c] = CAMINO;
            lab[opuestaR][opuestaC] = CAMINO;

            for (const [vDr, vDc] of vecinos) {
                const nr = opuestaR + vDr;
                const nc = opuestaC + vDc;
                
                if (esValida(nr, nc) && lab[nr][nc] === PARED) {
                    if (nr !== r || nc !== c) {
                        paredes.push({ r: nr, c: nc, de: { r: opuestaR, c: opuestaC } });
                    }
                }
            }
        }
    }

    for (let i = 0; i < FILAS; i++) {
        lab[i][0] = PARED;
        lab[i][COLUMNAS - 1] = PARED;
    }
    for (let j = 1; j < COLUMNAS - 1; j++) { 
        lab[0][j] = PARED;
        lab[FILAS - 1][j] = PARED;
    }

    let caminosDisponibles = [];
    for (let r = 1; r < FILAS - 1; r++) {
        for (let c = 1; c < COLUMNAS - 1; c++) {
            if (lab[r][c] === CAMINO) {
                caminosDisponibles.push({ r, c });
            }
        }
    }

    const sacarPosicionAleatoria = () => {
        if (caminosDisponibles.length === 0) return null;
        const index = Math.floor(Math.random() * caminosDisponibles.length);
        return caminosDisponibles.splice(index, 1)[0];
    };

    let posLlaveTP = sacarPosicionAleatoria();
    if (posLlaveTP) {
        lab[posLlaveTP.r][posLlaveTP.c] = 6;
    }

    let posPortal = sacarPosicionAleatoria();
    if (posPortal) {
        lab[posPortal.r][posPortal.c] = 5;
    }

    const numLlavePuerta = 6;
    for (let i = 0; i < numLlavePuerta; i++) {
        let posLlave = sacarPosicionAleatoria();
        if (posLlave) {
            lab[posLlave.r][posLlave.c] = 3;
        }

        let paredPuerta = null;
        const paredesDisponibles = [];

        for (let r = 1; r < FILAS - 1; r++) {
            for (let c = 1; c < COLUMNAS - 1; c++) {
                if (lab[r][c] === PARED) {
                    let caminosAdyacentes = 0;
                    for (const [dr, dc] of vecinos) {
                        const nr = r + dr;
                        const nc = c + dc;
                        
                        if (esValida(nr, nc) && lab[nr][nc] === CAMINO) {
                            caminosAdyacentes++;
                        }
                    }
                    
                    if (caminosAdyacentes >= 2) {
                        paredesDisponibles.push({ r, c });
                    }
                }
            }
        }

        if (paredesDisponibles.length > 0) {
            const index = Math.floor(Math.random() * paredesDisponibles.length);
            paredPuerta = paredesDisponibles.splice(index, 1)[0];
            lab[paredPuerta.r][paredPuerta.c] = 4;
        }
    }

    const numTrampas = 4 + (nivel - 1);
    for (let i = 0; i < numTrampas; i++) {
        let posTrampa = sacarPosicionAleatoria();
        if (posTrampa) {
            lab[posTrampa.r][posTrampa.c] = 2;
        }
    }

    lab[1][1] = CAMINO;

    return lab;

}

//Declaramos el laberinto y lo construimos
//  0 = camino, 1 = pared, 2 = trampa, 3 = llave, 4 = puerta, 5 = tp, 6 = llave para tp

let laberinto = [];


const tamCelda = 640 / 25;

k.loadSprite("puerta", "images/puerta.png");
k.loadSprite("puertaAbierta", "images/puertaAbierta.png");
k.loadSprite("llave", "images/llave.png");
k.loadSprite("pared", "images/pared.png");
k.loadSprite("trampa", "images/trampa.png");
k.loadSprite("portal", "images/portal.png");
k.loadSprite("llavetp", "images/llavetp.png");

let llavtp = false;
let llaves = 0;

let celdasVisibles = new Set();
let celdasExploradas = new Set();

let mensajeActual = null;
let listenerActual = null;
let puertaActual = null;
let timerMensaje = null;

//Funcion para el HUD
function actualizarHUD(jugador) {
    const hudVidas = k.get("hudVidas")[0];
    if (hudVidas) {
        hudVidas.text = `Vidas: ${jugador.hp()}`;
    }

    const hudLlaves = k.get("hudLlaves")[0];
    if (hudLlaves) {
        hudLlaves.text = `Llaves: ${llaves}`;
    }

    const hudLlaveTP = k.get("hudLlaveTP")[0];
    if (hudLlaveTP) {
        hudLlaveTP.text = `Llave TP:\n${llavtp ? 'Sí' : 'No'}`;
    }

    const hudNivel = k.get("hudNivel")[0];
    if (hudNivel) {
        hudNivel.text = `Nivel: ${nivelActual}`;
    }

    const hudPuntaje = k.get("hudPuntaje")[0];
    if (hudPuntaje) {
        hudPuntaje.text = `Puntaje: \n${puntuacion}`;
    }
}

//Funcion para dibujar el laberinto
function dibujarLaberinto(){
    const filas = laberinto.length
    const columnas = laberinto[0].length

    const tamLlave = tamCelda * 0.94;
    const escalaAreaLlave = 0.4;

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
                        k.sprite("pared",{width: tamCelda, height: tamCelda}),
                        k.pos(x,y),
                        k.area(),
                        k.body({isStatic: true}),
                        "pared"
                    ]);
                break;

                //Dibujamos trampas
                case 2:
                    k.add([
                        k.rect(tamCelda,tamCelda),
                        k.pos(x,y),
                        k.color(200, 200, 200),
                        "camino"
                    ]);

                    k.add([
                        k.sprite("trampa", { width: tamCelda, height: tamCelda }),
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
                        k.sprite("llave", {width: tamLlave, height: tamLlave}),
                        k.pos(x + tamCelda/2, y + tamCelda/2),
                        k.anchor("center"),
                        k.area({scale: escalaAreaLlave}),
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
                        k.sprite("puerta", { width: tamCelda, height: tamCelda }),
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
                        k.sprite("portal", { width: tamCelda, height: tamCelda }),
                        k.pos(x, y),
                        k.area(),
                        "portal"
                    ]);

                break;

                //Dibujamos la llave del portal
                case 6:
                    k.add([
                        k.rect(tamCelda,tamCelda),
                        k.pos(x,y),
                        k.color(200, 200, 200),
                        "camino"
                    ]);

                    k.add([
                        k.sprite("llavetp", {width: tamLlave, height: tamLlave}),
                        k.pos(x + tamCelda/2, y + tamCelda/2),
                        k.anchor("center"),
                        k.area({scale: escalaAreaLlave}),
                        "llavetp"
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

//Definimos la funcion par dibujar el campo de vision
function dibujarCampoVision(posicion){
    const radioVision = tamCelda * 0.89;
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

const tamJugador = tamCelda * 0.78; 
const areaJugador = tamJugador * 0.84;

//Cargamos al jugador
function agregarJugador(){
    const jugador = k.add([
        k.sprite("magordito",{ width: tamJugador, height: tamJugador }),
        k.pos(tamCelda + tamCelda/2, tamCelda + tamCelda/2),
        k.anchor("center"),
        k.area({
            shape: new k.Rect(k.vec2(0, 0), areaJugador, areaJugador)  
        }),
        k.body({gravityScale: 0}),
        k.scale(1),
        k.z(5),
        k.health(4),
        k.color(),
        "jugador",
        {
            isInvulnerable: false, 
            originalColor: k.rgb(255, 255, 255) 
        }
    ]);
        
    //Definimos los controles del jugador
    const velocidad = tamCelda * 4.7;

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
        puntuacion += 10;
        actualizarHUD(jugador);
    });

    //Colision con la llave del portal
    jugador.onCollide("llavetp", (llavetp) => {
        k.destroy(llavetp);
        llavtp = true;
        puntuacion += 50;
        actualizarHUD(jugador);
    });

    //Colision con puertas
    jugador.onCollide("puerta", (puerta) => {

        //Checamos que no sea la misma puerta con la que ya chocamos
        if (puertaActual === puerta) return;
        //Borramos mensajes si hay
        if (mensajeActual) k.destroy(mensajeActual);
        //Cancelamos el evento listenerActual si esta en ejecucion
        if (listenerActual) listenerActual.cancel();
        //Cancelamos el timer de destruccion de mensaje anterior
        if (timerMensaje) timerMensaje.cancel();

        puertaActual = puerta;

        //Mostramos el mensaje
        mensajeActual = k.add([
            k.text("¿Abrir puerta? (E = Si)", {size : 20}),
            k.pos(k.width()/2, k.height() - 100),
            k.anchor("center"),
            k.color(20, 20, 255), 
            k.z(100),
            "mensajePuerta"
        ]);

        //Creamos el listenerActual para leer la respuesta "E"
        listenerActual = k.onKeyPress("e", () => {
            if(llaves > 0){
                const x = puerta.pos.x - puerta.width / 2;
                const y = puerta.pos.y - puerta.height / 2;

                k.destroy(puerta);

                k.add([
                    k.sprite("puertaAbierta", { width: tamCelda, height: tamCelda }),
                    k.pos(x + tamCelda/2, y + tamCelda/2),
                    k.anchor("center"),
                    "puertaAbierta"
                ]);

                llaves--;
                actualizarHUD(jugador);

                if(mensajeActual){
                    k.destroy(mensajeActual);
                    mensajeActual = null;
                }
                if(listenerActual){
                    listenerActual.cancel();
                    listenerActual = null;
                }
                if(timerMensaje){ 
                    timerMensaje.cancel();
                    timerMensaje = null;
                }
                puertaActual = null;
            }
            else{
                k.destroy(mensajeActual);
            
                mensajeActual = k.add([
                    k.text("No tienes llaves", { size: 20 }),
                    k.pos(k.width()/2, k.height() - 100),
                    k.anchor("center"),
                    k.color(255, 0, 0),
                    k.z(100)
                ]);

                if(listenerActual){
                    listenerActual.cancel();
                    listenerActual = null;
                }

                timerMensaje = k.wait(1, () => {
                    if(mensajeActual){
                        k.destroy(mensajeActual);
                        mensajeActual = null;
                    }
                    timerMensaje = null;
                });
            }
        });
    });

    //Cuando se acabe la colision con la puerta
    jugador.onCollideEnd("puerta", (puerta) => {
        if(puertaActual === puerta){
            if(mensajeActual){
                k.destroy(mensajeActual);
                mensajeActual = null;
            }
            if(listenerActual){
                listenerActual.cancel();
                listenerActual = null;
            }
            if(timerMensaje){ 
                timerMensaje.cancel();
                timerMensaje = null;
            }
            puertaActual = null;
        }
    });

    //Colision con trampas
    jugador.onCollide("trampa", (trampa) => {

        if (jugador.isInvulnerable) {
            return; 
        }

        jugador.hurt(1);
        puntuacion -= 25; 
        if (puntuacion < 0) puntuacion = 0;
        actualizarHUD(jugador);
        k.destroy(trampa);

        if (jugador.hp() > 0) {
            jugador.isInvulnerable = true;
            const BLINKS = 4; 
            const DURATION = 1.0;

            const originalColor = jugador.originalColor; 
            const dañoColor = k.rgb(255, 0, 0);

            const parpadeo = k.loop(DURATION / (BLINKS * 2), () => {
                if (jugador.color.eq(dañoColor)) {
                    jugador.color = originalColor;
                } else {
                    jugador.color = dañoColor;
                }
            });

            k.wait(DURATION, () => {
                parpadeo.cancel(); 
                jugador.color = originalColor; 
                jugador.isInvulnerable = false;
            });
        }
    });

    //Colision con portal
    jugador.onCollide("portal", () => {
        if(llavtp == true){
            puntuacion += 100 * nivelActual;
            
            nivelActual++; 

            if (nivelActual > MAX_NIVELES) {
                go("ganar");
            } else {
                go("juego");
            }
        }
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
        actualizarHUD(jugador);
    });

    actualizarHUD(jugador);
    return jugador;
}

//Definimos el escenario de juego
k.scene("juego", () => {
    laberinto = [];
    llavtp = false;
    llaves = 0;
    celdasExploradas = new Set();
    mensajeActual = null;
    listenerActual = null;
    puertaActual = null;
    timerMensaje = null;
    laberinto = crearLaberinto(nivelActual);
    dibujarLaberinto();
    dibujarOscuridad();
    const jugador = agregarJugador();

    const anchoMapa = 640;
    const anchoHUD = 160;
    const margenX = anchoMapa;

    k.add([
        k.rect(anchoHUD, k.height()),
        k.pos(margenX, 0),
        k.color(10, 10, 10), 
        k.z(90),
        k.fixed(),
    ]);

    const textoX = margenX + 10; 
    let textoY = 40;

    k.add([
        k.text("ESTADO DEL JUEGO", { size: 18, width: 140, align: "center" }),
        k.pos(margenX + anchoHUD / 2, textoY), 
        k.anchor("center"),
        k.color(255, 255, 255),
        k.z(100),
        k.fixed(),
    ]);

    textoY += 50;

    k.add([
        k.rect(anchoHUD - 20, 2),
        k.pos(margenX + 10, textoY),
        k.color(50, 50, 50),
        k.z(100),
        k.fixed(),
    ]);

    textoY += 20;

    const hudVidas = k.add([
        k.text(`Vidas: ${jugador.hp()}`, { size: 24 }),
        k.pos(textoX, textoY), 
        k.color(255, 0, 0), 
        k.z(100),
        k.fixed(),
        "hudVidas" 
    ]);

    textoY += 40;

    const hudLlaves = k.add([
        k.text(`Llaves: ${llaves}`, { size: 24 }),
        k.pos(textoX, textoY), 
        k.color(255, 255, 0), 
        k.z(100),
        k.fixed(),
        "hudLlaves" 
    ]);

    textoY += 40; 

    
    const hudLlaveTP = k.add([
        k.text(
        `Llave TP:\n${llavtp ? 'Sí' : 'No'}`,
        {
            size: 24,
            align: "left"
        }
    ),
        k.pos(textoX, textoY), 
        k.color(0, 255, 255), 
        k.z(100),
        k.fixed(),
        "hudLlaveTP"
    ]);

    textoY += 60; 


    const hudNivel = k.add([
        k.text(`Nivel: ${nivelActual}`, { size: 24 }),
        k.pos(textoX, textoY), 
        k.color(255, 165, 0), 
        k.z(100),
        k.fixed(),
        "hudNivel" 
    ]);

    textoY += 40; 

    const hudPuntaje = k.add([
        k.text(`Puntaje: \n${puntuacion}`, { size: 24 }),
        k.pos(textoX, textoY), 
        k.color(0, 255, 0), 
        k.z(100),
        k.fixed(),
        "hudPuntaje"
    ]);

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
        k.pos(k.width()/2, k.height()/2 - 100),
        k.anchor("center"),
        k.color(255, 0, 0)
    ]);

    k.add([
        k.text(`Puntaje final: ${puntuacion}`, { size: 30 }),
        k.pos(k.width()/2, k.height()/2 - 20),
        k.anchor("center"),
        k.color(0, 255, 0)
    ]);
    
    k.add([
        k.text("Presiona ESPACIO para reintentar", { size: 24 }),
        k.pos(k.width()/2, k.height()/2 + 50),
        k.anchor("center"),
        k.color(255, 255, 255)
    ]);

    k.onKeyPress("space", () => {
        nivelActual = 1;
        puntuacion = 0;
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
        k.pos(k.width()/2, k.height()/2 - 100),
        k.anchor("center"),
        k.color(255, 0, 0)
    ]);
    
    k.add([
        k.text(`Puntaje final: ${puntuacion}`, { size: 30 }),
        k.pos(k.width()/2, k.height()/2 - 20),
        k.anchor("center"),
        k.color(0, 255, 0)
    ]);

    k.add([
        k.text("Presiona ESPACIO volver a jugar", { size: 24 }),
        k.pos(k.width()/2, k.height()/2 + 50),
        k.anchor("center"),
        k.color(255, 255, 255)
    ]);
    
    k.onKeyPress("space", () => {
        nivelActual = 1;
        puntuacion = 0;
        k.go("juego");
    });
});

//Declaramos la funcion principal
function main(){
    nivelActual = 1;
    puntuacion = 0;
    go("juego");
}

main();

