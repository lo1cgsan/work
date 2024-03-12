"""
Napisz program, który wypisuje w osobnych wierszach
małe litery alfabetu łacińskiego w porządku rosnącym,
a duże litery w porządku malejącym.
"""

for i in range(97, 123):
    print(i, chr(i), end='')

for i in range(90, 64, -1):
    print(i, chr(i))

male = 'abcdefghijklmnopqrstuwvxyz'
for i in male:
    print(i)

duze = 'ABCDEFGHIJKLMNOPQRSTUWVXYZ'

for i in range(len(duze)-1, -1, -1):
    print(duze[i])
