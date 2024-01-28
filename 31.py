#Funkcja jako obiekt pierwszej klasy
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def apply(fn, a, b): #funkcja wywoluje funkcje dla a i b
    return fn(a, b)  #fn wywolane z a i b #wraper do argumentu 

r1 = apply(add, 4, 5)
r2 = apply(multiply, 4, 8)
print(r1, r2)