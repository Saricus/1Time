name = input('Podaj Nick: ')

if len(name) < 3: # Jeśli mniejsze od 3
    print('Nick musi zawierać co najmniej 3 znaki')
elif name.isalnum(): # Jeśli jest literą lub cyfrą
    print('Brawo nick poprawny')
else:
    print('Podaj nick bez znaków specjalnich')