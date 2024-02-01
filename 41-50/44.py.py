#Lista pracowników + stanowisko + zarobki (zapisuje się w pliku)
#Dodawanie pracownika, usuwanie pracownika
#Zmiana stanowiska oraz zarobku


lista_pracowników = {}
lista_pracowników_stanowisko = {}
lista_pracowników_placa = {}

def lista_ppl():
    for key in lista_pracowników:
        
        print('ID:',(key),'|','Pracownik:',lista_pracowników[key],'|','Stanowisko:', lista_pracowników_stanowisko[key],'|','Płaca:', lista_pracowników_placa[key])

def dodanie_prac():
    print('Dodawanie pracownika')
    id_prac = input('Podaj Unikalne ID -> ')
    lista_pracowników.update({id_prac : input('Podaj Imię i Nazwisko -> ')})
    lista_pracowników_stanowisko.update({id_prac : input('Stanowisko -> ')})
    lista_pracowników_placa.update({id_prac : input('Podaj płace -> ')})

def usuniecie_pracownika():
    print('Usuwanie pracownika')
    id_prac = input('Podaj unikalne ID pracownika -> ')

    del lista_pracowników[id_prac]
    del lista_pracowników_stanowisko[id_prac]
    del lista_pracowników_placa[id_prac]


def zmiana_stanowiska():
    print('Zmiana stanowiska pracownika')

    for key in lista_pracowników:
        
        print('ID:',(key),'|','Pracownik:',lista_pracowników[key],'|','Stanowisko:', lista_pracowników_stanowisko[key])
    
    id_prac = input('Podaj Unikalne ID -> ')
    lista_pracowników_stanowisko.update({id_prac : input('Nowe Stanowisko -> ')})

def zmiana_placy():
    print('Zmiana płacy pracownika')

    for key in lista_pracowników:
        
        print('ID:',(key),'|','Pracownik:',lista_pracowników[key],'|','Stanowisko:', lista_pracowników_stanowisko[key])
    
    id_prac = input('Podaj Unikalne ID -> ')
    lista_pracowników_placa.update({id_prac : input('Nowa płaca -> ')})



while True:

    print('\nMenadzer pracowników\n'
          '1. Lista pracowników\n'
          '2. Dodanie pracownika\n'
          '3. Usunięcie pracownika\n'
          '4. Zmiana stanowiska\n'
          '5. Zmiana płacy\n'
          '6. Exit\n'
          )
    select = input('Wybierz opcje -> ')

    if select == '1':
        lista_ppl()
    elif select == '2':
        dodanie_prac()
    elif select == '3':
        usuniecie_pracownika()
    elif select == '4':
        zmiana_stanowiska()
    elif select == '5':
        zmiana_placy()
    else:
        break







