# palindromy.py
wyraz = "raddr"

dlugosc_wyr = 0
for znak in wyraz:
    dlugosc_wyr += 1

print(dlugosc_wyr)

for i in range(dlugosc_wyr // 2):
    if wyraz[i] != wyraz[-i-1]:
        print("nie palindrom")
        exit()

print("Palindrom")
