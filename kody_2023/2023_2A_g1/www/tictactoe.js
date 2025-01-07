let SZER = 60;

let POLE_GRY = [0, 0, 0,
                0, 0, 0,
                0, 0, 0];

function setup() {
    createCanvas(3 * SZER, 3 * SZER);
    background(220);
    strokeWeight(1);
}


function rysuj_plansze() {
    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            fill(255);
            rect((j * SZER), (i * SZER), SZER, SZER);
        }
    }
}


function draw() {
    rysuj_plansze();
}
