#Zbior - Set
a = set([1, 2, 3, 3, 1, 6, 9, 2])
b = set([1, 2, 3, 5, 11, 23])
print(a) # set podaje tylko uniklane wartosci
print(b)
print(a.intersection(b)) #co jest wspólna dal A i B
print(a.union(b)) # laczy zbiory
print(a.difference(b)) # podaje elementy ktore sa unikalne w A w porownaniu do B
print(a.symmetric_difference(b)) # podaje elementy ktore sa unikalne dla A i B
