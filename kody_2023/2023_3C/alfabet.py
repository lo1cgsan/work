"""
Napisz program, który wypisuje małe litery alfabetu
łacińskiego w kolejności malejącej (z..a),
a duże w kolejności rosnącej (A..Z).
"""
print('zyxwvutsrqponmlkjihgfedcba')
print('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

male = 'zyxwvutsrqponmlkjihgfedcba'
duze = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for znak in male:
    print(znak, end='')
print()

for i in range(122, 96, -1):
    print(chr(i), end='')
print()

for i in range(65, 91):
    print(chr(i), end='')
print()
