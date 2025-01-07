def sumuj_kody_ascii(tekst):
    suma = 0
    for znak in tekst:
        kod = ord(znak)
        suma = suma + kod
    return suma

# program sprawdza, czy podane wyrazy są anagramami
w1 = input('Podaj wyraz: ')
w2 = input('Podaj wyraz: ')

w1 = w1.strip().lower()  # usuń zbędne spacje i zamień na małe litery
w2 = w2.strip().lower()

w1 = w1.replace(' ', '')  # usuń spację wewnątrz wyrazu
w2 = w2.replace(' ', '')

if sumuj_kody_ascii(w1) == sumuj_kody_ascii(w2):
    print(w1, w2, "to anagramy!")
else:
    print('To nie anagramy!')
