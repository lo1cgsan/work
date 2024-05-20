function setup() {
    createCanvas(720, 400);
    background(200, 200, 200);

    fill(239, 34, 34);
    stroke(0);
}

function draw() {
    // prostokąt
    rect(40, 120, 120, 40);
    ellipse(240, 240, 80, 80);
    triangle(50, 10, 300, 10, 125, 100);

    // transformacja
    translate(580, 200);
    noStroke();
    for (let i = 0; i < 10; i++) {
        ellipse(0, 30, 20, 80);
        rotate(PI/5);
    }
}
