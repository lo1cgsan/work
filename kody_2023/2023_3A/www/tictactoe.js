let SZER = 50;
let POLEGRY = [0, 0, 0,
               0, 0, 0,
               0, 0, 0];
let RUCH = 1; // 1 - gracz, 2 - AI
let WYGRANY = 0;

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

function rysuj_polegry() {
    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            pole = i * 3 + j;

            x = j * SZER + SZER/2;
            y = i * SZER + SZER/2;

            if (POLEGRY[pole] == 1) {
                fill(255, 0, 0);
                circle(x, y, 25);
            } else if (POLEGRY[pole] == 2) {
                fill(0, 0, 255);
                circle(x, y, 25);
            }
        }
    }
}

function postaw_znak(pole) {
    if (POLEGRY[pole] == 0) {
        POLEGRY[pole] = RUCH;
    }
}

function mouseClicked() {
    if (WYGRANY == 0) {
        if (RUCH == 1) {
            // ruch gracza
            let pole = Math.floor(mouseY/SZER) * 3 + Math.floor(mouseX/50);
            postaw_znak(pole);
            console.log(POLEGRY);
            kto_wygral();
            RUCH = 2;
        }
        if (WYGRANY == 0 && RUCH == 2) {
            ai_ruch();
            RUCH = 1;
        }
    }
}

function sprawdz_pola(uklady, wygrany = 0) {
    let indeks = null;
    POLA_INDEKSY = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], // wiersze
        [0, 3, 6], [1, 4, 7], [2, 5, 8], // kolumny
        [0, 4, 8], [2, 4, 6]
    ];

    for (const indeksy of POLA_INDEKSY) {
        kol = []; // tablica pomocnicza
        for (const ind of indeksy) {
            kol.push(POLEGRY[ind]);
        }

        for (const uklad of uklady) {
            if (kol.toString() == uklad.toString()) {
                if (wygrany > 0) {
                    return wygrany;
                } else {
                    return indeksy[kol.indexOf(0)];
                }
            }
        }
    }
}

function kto_wygral() {;}

function ai_ruch() {
    uklady_wygrywam = [[2, 2, 0], [2, 0, 2], [0, 2, 2]];
    uklady_blokuje = [[1, 1, 0], [1, 0, 1], [0, 1, 1]];

    pole = sprawdz_pola(uklady_wygrywam);
    if (pole !== null) {
        postaw_znak(pole);
        return;
    }

    pole = sprawdz_pola(uklady_blokuje);
    if (pole !== null) {
        postaw_znak(pole);
        return;
    }

    while (pole == null) {
        let poz = Math.floor(Math.random() * 9);
        if (POLEGRY[poz] == 0) {
            postaw_znak(poz);
        }
    }

}

function draw() {
    background(220);
    strokeWeight(1);
    rysuj_plansze();
    rysuj_polegry();
}
