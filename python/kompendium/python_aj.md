## Informacje ogólne

Python to język interpretowany, wysokiego poziomu, obiektowy, umożliwia również programowanie strukturalne i funkcyjne.
Interpreter Pythona to program, który wykonuje skrypty zapisane w plikach z rozszerzeniem ".py" i polecenia wprowadzane w trybie interaktywnym. W systemach Linux Python jest zainstalowany. W systemach macOS oraz MS-Windows należy go zainstalować. Więcej informacji i kody źródłowe używane w tych lekcjach znajdziesz w serwisie GitHub pod adresem: https://github.com/ZPE-Epodreczniki/

## Konwencja formatowania kodu (ang. <code><foreign lang='en'>code</foreign></code>)

- ciągi znaków otaczamy cudzysłowami albo pojedynczymi, albo podwójnymi
- nawiasy, o ile nie są częścią ciągu znaków, występują zawsze parami
- operatory otacza się spacjami
- dwukropek (`:`) zapowiada blok kodu, czyli wcięcia
- bloki kodu wcina się **4 spacjami** i ich wielokrotnościami
- w wierszu powinny występować maksymalnie 72 znaki
- znak `#` oznacza komentarz

## Co zawiera kod źródłowy (ang. <code><foreign lang='en'>source code</foreign></code>)

* **<code>identyfikatory zmiennych</code>** - nazwy, które wskazują na wartość określonego typu
* **<code>identyfikatory słów kluczowych</code>** - nazwy zarezerwowane przez język, np.: <code><foreign lang='en'>if, elif, else, for, while</foreign></code>
* **<code>literały</code>** - wartości np. znakowe <code>"Adam"</code> lub liczbowe <code>10</code>, <code>2.345</code> – które mogą być przypisywane zmiennym
* **<code>operatory</code>** arytmetyczne (<code>+, -, /, *</code>) lub logiczne (<code><, >, ==, !=</code>)
* **<code>ograniczniki</code>**, np. przecinek, dwukropek, nawiasy okrągłe, kwadratowe, klamrowe
* **<code>wyrażenia</code>**, tj. kombinacje zmiennych, wartości, operatorów i/lub wywołań funkcji, które zwracają wartości, np.: <code>int((a + b) / 2)</code>

## Jak nazywamy zmienne (ang. <code><foreign lang='en'>variables</foreign></code>)

- nazwa zaczyna się od litery lub znaku podkreślenia
- nazwa zawiera tylko znaki, cyfry i/lub podkreślenia, nie zawiera spacji i nie powinna zawierać znaków diakrytycznych (jak "ąę")
- małe i wielkie litery są różnymi znakami, np. <code>x</code> to coś innego niż <code>X</code>
- używamy konwencji **<code><foreign lang='en'>snake_case</foreign></code>** do nazywania zmiennych (także funkcji, metod, modułów i pakietów), czyli małych liter i wyrazów oddzielanych podkreśleniem, np. <code>moja_zmienna</code>

## Typ danych (ang. <code><foreign lang='en'>data type</foreign></code>)

Python wykorzystuje **<code><foreign lang='en'>typowanie dynamiczne</foreign></code>** (ang. <code><foreign lang='en'>duck typing</foreign></code>). Zmienne inicjuje się przez przypisanie im jakiejś wartości. Zmienne "przechowują" lub inaczej "wskazują na" wartości określonego typu.

- **<code>ciąg znaków</code>**  (<class 'str'>, ang. <code><foreign lang='en'>string</foreign></code>) – np. <code>"", '', " ", '12345'</code>
- **<code>liczba całkowita</code>** (<class 'int'>, ang. <code><foreign lang='en'>integer</foreign></code>) – np. <code>10</code>,
- **<code>liczba zmiennoprzecinkowa</code>** (<class 'float'>, ang. <code>floating point</code>) – np. <code>1.2345</code>,
- **<code>typ logiczny</code>** (<class 'bool'>, ang. <code><foreign lang='en'>boolean type</foreign></code>) – podtyp liczb całkowitych, zawiera dwie wartości: <code><foreign lang='en'>True</foreign></code> (1, prawda) lub <code><foreign lang='en'>False</foreign></code> (0, fałsz)

## Inicjacja zmiennych

Inicjacja zmiennej wymaga operacji przypisania, tj. podania nazwy, operatora przypisania (<code>=</code>) oraz wartości określonego typu, np. ciągu znaków, liczby całkowitej itd. Wartość może być wynikiem wyrażenia lub funkcji.

* <code>imie = "Adam"</code> – zmienna znakowa
* <code>liczba = input("Podaj liczbę: ")</code> – zmienna z wartością zwróconą przez funkcję
* <code>a = 5</code>, <code>pi = 3.14</code> – zmienna zawierającej liczby
* <code>parzysta = False</code> – zmienna zawierająca wartość logiczną
* <code>iloczyn = (2 * a) + 1</code> – zmienna  z wartością zwróconą za pomocą wyrażenia

## Przykłady złożonych struktur danych

* lista – <code>[element1, element2, element3, ...]</code>
* słownik – <code>{ klucz1: wartość1, klucz2: wartość2, ... }</code>


## Typowe operacje

- **<code>łączenie ciągów znakowych</code>** (tzw. konkatenacja) za pomocą operatora `+`, np. <code>"10" + "1"</code>
- **<code>pobieranie danych z klawiatury</code>** – instrukcja wejścia `input("komunikat dla użytkownika")` zwraca dane jako tekst (typ <code>str</code>!)
- **<code>wypisywanie komunikatów</code>** – instrukcja `print()` wypisuje znaki lub zmienne w terminalu

  - `print("komunikat", a)` – wypisanie ciągu znaków i wartości zmiennej <code>a</code>
  - `print(f"{a} jest większe od {b}")` – wypisanie ciągu formatowanego (tzw. *<code><foreign lang='en'>f-string</foreign></code>*), w miejsce nawiasów klamrowych wstawiane są wartości zmiennych lub wyrażeń

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

Przykłady pętli <code>for</code> (wykonuje się określoną liczbę razy):

```Python
# pętla, która wykona się 10 razy
for i in range(10):
    print(i)  # powtarzana instrukcja wypisująca wartość i
```

Przykłady pętli <code>while</code> (wykonuje się, dopóki warunek jest prawdziwy):

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
