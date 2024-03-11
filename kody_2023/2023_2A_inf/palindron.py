tekst = input("Podaj tekst: ")
d = len(tekst)
for i in range(d // 2):
    if tekst[i] != tekst[d - 1 - i]:
        print("To nie palindron!")
        exit()
print("To paindron!")
