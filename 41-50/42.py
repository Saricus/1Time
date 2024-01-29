#kamien papier nozyce
import random

def kamien_papier_noz():
    opcje = {'K': 'Kamien', 'P': 'Papier', 'N': 'Nozyce'}
    ai_pick = random.choice(list(opcje.keys()))
    info = 'K - Kamien, P - Papier, N - Nozyce -> '
    user_pick = input(info).upper()

    while user_pick not in list(opcje.keys()):
        print('Zły wybór')
        user_pick = input(info).upper()
    print('Wybór AI', ai_pick)

    if (user_pick == 'P' and ai_pick == 'K') \
        or (user_pick == 'K' and ai_pick == 'N') \
        or (user_pick == 'N' and ai_pick == 'P'):
        print(opcje[user_pick], 'pokonuje', opcje[ai_pick])
        return 'Wygrana'
    elif user_pick != ai_pick:
        print(opcje[ai_pick], 'pokonuje', opcje[user_pick])
        return 'Przegrana'
    else:
        return 'Remis'
        

def play_ag():
    return input('Chcesz zagrać jeszcze raz? (T/N) -> ').upper()


start = input('Czy chcesz rozpocząć rozgrywkę? (T/N) -> ').upper()

while True:
    if start == 'T':
        game_res = kamien_papier_noz()
        if game_res == 'Wygrana':
            print('Gratulacje, wygrałeś')
            start = play_ag()
            continue
        elif game_res == 'Przegrana':
            print('Przegrana sadge :/')
            start = play_ag()
            continue
        else:
            print('REMIS, spróbuj ponownie!')
    elif start == 'N':
        print('No to naura!')
        break
    else:
        print('Zła odpowiedź. Spróbuj ponownie.')
        start = input('T/N -> ').upper()