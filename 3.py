print('Maxymalna pojemnośc magazynu to 100 miejsc')
max = 100
psc = int(input('Podaj ilość towaru w magazynie: '))
dostawa = int(input('Podaj ilość towaru w dostawei: '))
razem = psc + dostawa
wolne = max - (psc + dostawa)
if psc + dostawa > max:
    print('Magazyn nie pomieści tyle towaru')
else:
    print('Można pakowac. Nowy stan magazynu to {} sztuk. W magazynie pozostanie {} miejsc'.format(razem, wolne))
