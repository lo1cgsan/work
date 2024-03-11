liczby = [6, 5, 3, 1, 8, 7, 2, 4, 6, 5, 3, 1, 8, 7, 2, 4]
n = len(liczby)

licznik = 0
for i in range(n-1, 0, -1):
    for j in range(i):
        licznik += 1
        if liczby[j] > liczby[j+1]:
            tmp = liczby[j]
            liczby[j] = liczby[j+1]
            liczby[j+1] = tmp
        
print(liczby)
print("Licznik:", licznik, "n:", n)

8 => 28
16 => 120

"""
0: [6, 5, 3, 1, 8, 7, 2, 4]
    
    0  1  2  3  4  5  6     7
1: [5, 3, 1, 6, 7, 2, 4,    8]
2: [3, 1, 5, 6, 2, 4,    7, 8]
3: [1, 3, 5, 2, 4,    6, 7, 8]
4: [1, 3, 2, 4,    5, 6, 7, 8]
5: [1, 2, 3,    4, 5, 6, 7, 8]
6: [1, 2,    3, 4, 5, 6, 7, 8]
7: [1,    2, 3, 4, 5, 6, 7, 8]
"""
