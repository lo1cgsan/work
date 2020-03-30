m = float(input('Podaj masę ciała (kg): '))
w = float(input('Podaj wzrost (m): '))

print(m, w)

bmi = m / (w**2)
print(bmi)

if bmi < 18.5:
    print('niedowaga')
elif bmi < 25:
    print('norma')
elif bmi < 30:
    print('nadwaga')
else:
    print('otyłość')


input('Naciśnij jakiś klawisz...')
