plik = open('kappa.txt', 'w') # r - odczytaj w- wprowadz
plik.write('lubie placki')
plik.close

with open('kappa.txt') as plik: #odczytanie zawartosci
    zawartosc_pliku = plik.read()
    print(zawartosc_pliku)