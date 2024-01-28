#Dekoratory

# zmienia jej zachowanie, dekoratorem jest inna funkacja 

def decorator(fn):
    def wrapper():
        print('Początek odliczania')
        fn()
        print('Koniec odliczania')
    return wrapper

@decorator
def get_5_values():
    for v in range(1,6):
        print(v)

#get_5_values_decorator = decorator(get_5_values)  #z dekoratorem
#get_5_values_decorator()

get_5_values()