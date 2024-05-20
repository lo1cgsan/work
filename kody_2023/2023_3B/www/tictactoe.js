function setup() {
    createCanvas(720, 400);
    background(234, 148, 148);

    // ustawienie koloru
    fill(204, 101, 192, 127);
    stroke(127, 63, 120);

    // prostokąt
    rect(40, 120, 120, 40);
    // elipsa
    ellipse(240, 240, 80, 80);
    // trójkąt
    triangle(300, 100, 320, 100, 310, 80);

    // zmiana początku układu współrzędnych
    translate(580, 200);
    noStroke();
    for (let i = 0; i < 10; i++) {
        ellipse(0, 30, 20, 80);
        rotate(PI/5);
    }
}
