#Instrukcja raise

def devide(a, b):
    if b == 0:
        raise ZeroDivisionError('Ogolny blad!')
    return a // b

try:
    r = devide(4,0)
    print(r)
except ZeroDivisionError:
    print('Nie mozna podzielic przez 0')