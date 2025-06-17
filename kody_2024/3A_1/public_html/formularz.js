function sprawdz() {
    var imie = document.getElementById('imie').value;
    if (imie.length > 1) {
        console.log('Imię: ' + imie);
    } else {
        alert('Nie podałeś imienia!');
    }

    var nazwisko = document.getElementById('nazwisko').value;
    if (nazwisko.length > 1) {
        console.log('Nazwisko: ' + nazwisko);
    } else {
        alert('Nie podałeś nazwisko!');
    }

    var email = document.getElementById('email').value;
    if (email.length > 5 && email.indexOf('@')) {
        console.log('Nazwisko: ' + nazwisko);
    } else {
        alert('Nie podałeś nazwisko!');
    }

    return false;
}