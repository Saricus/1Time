a = int(input('Podaj 1 cyfre: '))
print('Wybierz znak')
print('1. +')
print('2. -')
print('3. *')
print('4. /')
b = int(input('Jaki znak?: '))
c = int(input('Podaj 2 cyfre: '))

if b == 1:
    print(a + c)
elif b == 2:
    print(a - c)
elif b == 3:
    print(a * c)
elif b == 4:
    print(a / c)
else:
    print('Niepoprawny wybór znaku wybierz numer 1-4')

