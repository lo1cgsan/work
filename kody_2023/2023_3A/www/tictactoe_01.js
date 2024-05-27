let SZER = 50;

function setup() {
    createCanvas(SZER * 3, SZER * 3);
}

function rysuj_plansze() {
    fill(255);
    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            rect((j * SZER), (i * SZER), SZER, SZER, 1);
        }
    }
}

function draw() {
    background(220);
    strokeWeight(1);
    rysuj_plansze();
}
