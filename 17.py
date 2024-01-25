opcje = {
    'env': 'produkcja',
    'db' : 'mysql',
    'version' : 1.0,
    'show_errors' : True
}

del opcje['show_errors'] #usuwa klucz-wartosc
print(opcje.get('db')) 
# get sprawdza czy klucz istnieje jeśli tak zwaraca wartosc
print(opcje.get('show_errors'))

opcje.update({ #update słownika
    'user' : 'admin',
    'pass' : 'haslo',
    'version' : 2.2
})
print(opcje)

print('*****************************')
for key in opcje:
    print(key) #poda nazwy kluczy
    print(opcje[key]) # poda wartosc
    print('*****************************')
    
# można zrobic to berz for

print(opcje.values()) #zwraca wartosci jako lista
print(opcje.keys()) #zwraca klucze jako lista
