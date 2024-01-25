# scope - zasieg zmiennych
x = 1 # ma zasieg globalny (caly plik)

def fn():
    x = 2 # zasieg tylko na funkcje
    print(x)

def fn2():
    global x # edytuje globalny x
    x += 5
    print(x)

fn()

fn2()

print(x)