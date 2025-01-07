ASCII_0 = 48
ASCII_A_10 = 55

def digit_to_int(digit):
    # zamiana cyfry na liczbę
    if '0' <= digit <= '9':
        return ord(digit) - ASCII_0
    elif 'A' <= digit.upper() <= 'Z':
        return ord(digit.upper()) - ASCII_A_10
    else:
        return 0

def int_to_digit(value):
    # zamiana liczby na znak
    if 0 <= value <= 9:
        return chr(value + ASCII_0)
    elif 10 <= value <= 15:
        return chr(value + ASCII_A_10)
    else:
        return 0

def any2dec(value, base):
    #  zamiana liczby na system dziesiętny
    wynik = 0
    for digit in value:
        wynik = wynik * base + digit_to_int(digit)
    return wynik

def dec2any(value, base):
    if value == 0:
        return '0'
    wynik = ''
    while value > 0:
        wynik = int_to_digit(value % base) + wynik
        value = value // base
    return wynik


print(digit_to_int('a'))
print(int_to_digit(10))
print(any2dec('1101', 2))
print(any2dec('FF', 16))
print(dec2any(13, 2))