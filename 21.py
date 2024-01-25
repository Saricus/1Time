def kappa(a, b=0, c=0):
    print('A:', a, 'B:', b, 'C:', c)

kappa(2, c=8) # pominicie b


def fn(a , *args, **dict_args):
    # * opcjonalne argumenty (zostaja zebrane w tuple)
    # ** - slownik/zbior
    print(a)
    print(args)
    print(dict_args)
fn(2, 33, 4, 55, True, 'XP', user='admin', passwd='haslo')

print('**********************************')

def auto(a , *args, **dict_args):
    for arg in args:
        print(arg)
    for key in dict_args:
        print(dict_args[key])
auto(2, 33, 4, 55, True, 'XP', user='admin', passwd='haslo')