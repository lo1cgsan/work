let SZER = 50;
let POLEGRY = [0, 0, 0,
               0, 0, 0,
               0, 0, 0]

let RUCH = 1; // 0 - pole puste, 1 - gracz, 2 - komputer

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

function postaw_znak(pole, RUCH) {
    if (POLEGRY[pole] == 0) {
        if (RUCH == 1) {
            POLEGRY[pole] = 1;
            return 2;
        } else if (RUCHH == 2) {
            POLEGRY[pole] = 2;
            return 1;
        }
    }
    return RUCH;
}

function rysuj_polegry() {
    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            pole = i * 3 + j;
            x = j * SZER + SZER / 2;
            y = i * SZER + SZER / 2;
            // TODO
        }
    }
}

function draw() {
    background(220);
    strokeWeight(1);
    rysuj_plansze();
}
