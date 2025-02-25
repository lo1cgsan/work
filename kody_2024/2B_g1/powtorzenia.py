liczba_spotkan = 5

for nr in range(liczba_spotkan):
    print(f'Spotkanie {nr+1}')

love = 'tak'

while love == 'tak':
    print(f'Spotkanie {nr+1+1}')
    nr += 1
    love = input('Czy dalej (tak/nie)? ')


