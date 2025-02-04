# palindromy.py
wyraz = "bryoyrb"

dl_wyrazu = 0
for znak in wyraz:
    dl_wyrazu += 1
# dl_wyrazu = len(wyraz)

ile_porownan = dl_wyrazu // 2

for i in range(ile_porownan):
    if wyraz[i] != wyraz[-i-1]:
        print("nie plaindrom")
        exit()

print("Palindrom")
