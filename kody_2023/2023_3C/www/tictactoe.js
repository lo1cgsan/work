let SZER = 50;
let POLEGRY = [0, 0, 0,
               0, 0, 0,
               0, 0, 0]

let RUCH = 1; // 0 - pole puste, 1 - gracz, 2 - komputer
let WYGRANY = 0; // 0 - nikt, 1 - gracz, 2 - komputer



function setup() {
    createCanvas(3 * SZER, 3 * SZER);
}

function rysuj_plansze() {
    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            fill(255);
            rect((j * SZER), (i * SZER), SZER, SZER);
        }
    }
}

function postaw_znak(pole) {
    if (POLEGRY[pole] == 0) {
        POLEGRY[pole] = RUCH;
    }
}

function rysuj_polegry() {
    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            pole = i * 3 + j;
            x = j * SZER + SZER / 2;
            y = i * SZER + SZER / 2;

            if (POLEGRY[pole] == 1) {
                fill(0, 0, 255);
                circle(x, y, SZER / 3);
            } else if (POLEGRY[pole] == 2) {
                fill(255, 0, 0);
                circle(x, y, SZER / 3);
            }
        }
    }
}

function mouseClicked() {
    if (WYGRANY == 0) {
        if (RUCH == 1) {
            let pole = (Math.floor(mouseY / SZER) * 3) + Math.floor(mouseX / SZER);
            console.log("Pole: ", pole);
            postaw_znak(pole);
        }
    }
}

function draw() {
    background(220);
    strokeWeight(1);
    rysuj_plansze();
    rysuj_polegry();
}
