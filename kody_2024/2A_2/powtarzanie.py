# powtarzanie.py

liczba_spotkan = 3

for nr in range(liczba_spotkan):
    print(f'Spotkanie {nr+1}')

love = 'tak'

while love == 'tak':
    print(f'Spotkanie {nr+1}')
    nr += 1
    love = input('Czy chcesz jeszcze (tak/nie)?')

