lista = [10, 20, 30, 40]
print(lista[0:2])
print(lista[1:])
lista2 = [50, 60]
main_list = lista + lista2 * 2
main_list.sort()
print(main_list)
print(50 in main_list) # czy 50 jest na liscie