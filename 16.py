#Dictionary - słownik
#zbiór wartości
#nie ma indexu
#zawiera pary klucz-wartosc
#mutowalne
opcje = {
    'env': 'produkcja',
    'db' : 'mysql',
    'version' : 1.0,
    'show_errors' : True
}

opcje['user'] = 'admin' # dodanie

opcje['version'] = 2.0 # update

print(opcje['db'])
print(opcje['version'])
print(opcje['user'])

