# palindromy.py
def czy_palindrom(wyraz):
    for i in range(len(wyraz) // 2):
        if wyraz[i] != wyraz[-1-i]:
            return False
    return True

wyraz = input('Podaj wyraz: ')

if czy_palindrom(wyraz):
    print('palindrom')
else:
    print('nie plaindrom')



# dl_wyrazu = 0
# for znak in wyraz:
#    dl_wyrazu += 1
