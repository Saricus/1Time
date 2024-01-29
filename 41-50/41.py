from random import randint

zakres1 = int(input('Podaj pierwszą liczbę zakresu -> '))
zakres2 = int(input('Podaj drugą liczbę zakresu -> '))



print('Zgadnij liczbe od {} do {}'.format(zakres1,zakres2))

num = randint(zakres1, zakres2)

guessing = True

while guessing:
    guess = int(input('Jaka jest twoja liczba?: '))
    if guess > num:
        print('Za wysko')
    elif guess < num:
        print('Za nisko')
    else:
        print('Brawo zgadles')
        guessing = False