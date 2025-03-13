## Informacje ogólne

Python to język interpretowany, wysokiego poziomu, obiektowy, umożliwia również programowanie strukturalne i funkcyjne.
Interpreter Pythona to program, który wykonuje skrypty zapisane w plikach z rozszerzeniem ".py" i polecenia wprowadzane w trybie interaktywnym. W systemach Linux Python jest zainstalowany. W systemach macOS oraz MS-Windows należy go zainstalować. Więcej informacji i kody źródłowe używane w tych lekcjach znajdziesz w serwisie GitHub pod adresem: https://github.com/ZPE-Epodreczniki/

## Konwencja formatowania kodu (ang. **code**)

- ciągi znaków otaczamy cudzysłowami albo pojedynczymi, albo podwójnymi
- nawiasy, o ile nie są częścią ciągu znaków, występują zawsze parami
- operatory otacza się spacjami
- dwukropek (`:`) zapowiada blok kodu, czyli wcięcia
- bloki kodu wcina się **4 spacjami** i ich wielokrotnościami
- w wierszu powinny występować maksymalnie 72 znaki
- znak `#` oznacza komentarz

## Co zawiera kod źródłowy (ang. **source code**)

* **`identyfikatory zmiennych`** - nazwy, które wskazują na wartość określonego typu
* **`identyfikatory słów kluczowych`** - nazwy zarezerwowane przez język, np.: `**if, elif, else, for, while**`
* **`literały`** - wartości np. znakowe `"Adam"` lub liczbowe `10`, `2.345` – które mogą być przypisywane zmiennym
* **`operatory`** arytmetyczne (`+, -, /, *`) lub logiczne (`<, >, ==, !=`)
* **`ograniczniki`**, np. przecinek, dwukropek, nawiasy okrągłe, kwadratowe, klamrowe
* **`wyrażenia`**, tj. kombinacje zmiennych, wartości, operatorów i/lub wywołań funkcji, które zwracają wartości, np.: `int((a + b) / 2)`

## Jak nazywamy zmienne (ang. `**variables**`)

- nazwa zaczyna się od litery lub znaku podkreślenia
- nazwa zawiera tylko znaki, cyfry i/lub podkreślenia, nie zawiera spacji i nie powinna zawierać znaków diakrytycznych (jak "ąę")
- małe i wielkie litery są różnymi znakami, np. `x` to coś innego niż `X`
- używamy konwencji `**snake_case**` do nazywania zmiennych (także funkcji, metod, modułów i pakietów), czyli małych liter i wyrazów oddzielanych podkreśleniem, np. `moja_zmienna`

## Typ danych (ang. `**data type**`)

Python wykorzystuje `**typowanie dynamiczne**` (ang. `**duck typing**`). Zmienne inicjuje się przez przypisanie im jakiejś wartości. Zmienne "przechowują" lub inaczej "wskazują na" wartości określonego typu.

- **`ciąg znaków`**  (<class 'str'>, ang. `**string**`) – np. `"", '', " ", '12345'`
- **`liczba całkowita`** (<class 'int'>, ang. `**integer**`) – np. `10`,
- **`liczba zmiennoprzecinkowa`** (<class 'float'>, ang. `**floating point**`) – np. `1.2345`,
- **`typ logiczny`** (<class 'bool'>, ang. `**boolean type**`) – podtyp liczb całkowitych, zawiera dwie wartości: `**True**` (1, prawda) lub `**False**` (0, fałsz)

## Inicjacja zmiennych

Inicjacja zmiennej wymaga operacji przypisania, tj. podania nazwy, operatora przypisania (`=`) oraz wartości określonego typu, np. ciągu znaków, liczby całkowitej itd. Wartość może być wynikiem wyrażenia lub funkcji.

* `imie = "Adam"` – zmienna znakowa
* `liczba = input("Podaj liczbę: ")` – zmienna z wartością zwróconą przez funkcję
* `a = 5`, `pi = 3.14` – zmienna zawierającej liczby
* `parzysta = False` – zmienna zawierająca wartość logiczną
* `iloczyn = (2 * a) + 1` – zmienna  z wartością zwróconą za pomocą wyrażenia

## Przykłady złożonych struktur danych

* lista – `[element1, element2, element3, ...]`
* słownik – `{ klucz1: wartość1, klucz2: wartość2, ... }`


## Typowe operacje

- **`łączenie ciągów znakowych`** (tzw. konkatenacja) za pomocą operatora `+`, np. `"10" + "1"`
- **`pobieranie danych z klawiatury`** – instrukcja wejścia `input("komunikat dla użytkownika")` zwraca dane jako tekst (typ `str`!)
- **`wypisywanie komunikatów`** – instrukcja `print()` wypisuje znaki lub zmienne w terminalu

  - `print("komunikat", a)` – wypisanie ciągu znaków i wartości zmiennej `a`
  - `print(f"{a} jest większe od {b}")` – wypisanie ciągu formatowanego (tzw. *`**f-string**`*), w miejsce nawiasów klamrowych wstawiane są wartości zmiennych lub wyrażeń

- **rzutowanie typów danych**:

  - `int("123")` – zamiana tekstu na liczbę całkowitą
  - `float("2.5")` – zamiana na liczbę zmiennoprzecinkową
  - `str(10)` – zamiana np. liczby na tekst

## Instrukcje warunkowe

Ogólna forma:

```python
if warunek1:
    # instrukcja lub blok instrukcji wykonywanych gdy warunek1 jest prawdą
elif warunek2:
    # instrukcja lub blok instrukcji wykonywanych gdy warunek2 jest prawdą
else:
    # instrukcja lub blok instrukcji wykonywanych gdy warunki nie są prawdziwe
```

Przykłady:

```python
# sprawdzamy, czy a jest parzyste
if a % 2 == 0:
    print("Liczba", a, "jest parzysta!")
else:
    print("Liczba", a, "nie jest parzysta!")
```

Forma z dodatkowym testem:

```python
# sprawdzamy, czy a jest większe, czy równe b
if a > b:
    print("Liczba", a,"jest większa od", b, "!")
elif a == b:
    print("Liczby", a, "i", b, "są równe!")
else:
    print("Liczba", a,"jest mniejsza od", b, "!")
```

Zagnieżdżanie instrukcji warunkowych:

```Python
# sprawdzamy, czy a jest większe od b i c
if a > b:
    # ewentualna instrukcja lub instrukcje
    if a > c:
        print("Liczba", a, "jest największa.")
else:
    # blok kodu
```

## Instrukcje iteracji (pętle)

Przykłady pętli `for` (wykonuje się określoną liczbę razy):

```Python
# pętla, która wykona się 10 razy
for i in range(10):
    print(i)  # powtarzana instrukcja wypisująca wartość i
```

Przykłady pętli `while` (wykonuje się, dopóki warunek jest prawdziwy):

```Python
# pętla, która wykonuje się dopóki warunek a > 0 jest prawdziwy
a = 10
while a > 0:
    a = a - 1

# pętla, która pobiera liczbę z klawiatury, dopóki liczba jest ujemna lub równa 0
liczba = int(input("Podaj liczbę: "))
while liczba <= 0:
    liczba = int(input("Podaj liczbę: "))
```
