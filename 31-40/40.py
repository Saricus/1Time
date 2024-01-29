from random import randint
from DiceFaceDiagram import DiceFaceDiagram

def parse_input(input_string):
    if input_string in {'1', '2', '3', '4', '5', '6'}:
        return int(input_string)
    else:
        print('Podaj numer od 1 do 6')
        exit()

def roll_a_dice(dice):
    roll_results = []
    for _ in range(dice):
        roll = randint(1,6)
        roll_results.append(roll)
    return roll_results


dice_input = input('Iloma koscmi wykonac rzut: ')
dice = parse_input(dice_input)


roll_reslts = roll_a_dice(dice)


dice_face_diagram = DiceFaceDiagram(roll_results=roll_reslts)

dice_face_diagram.display_results()

