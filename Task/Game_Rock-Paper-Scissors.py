import random

should_conitue = True
while should_conitue:
    win = (('R','P'),('R','S'),('S','P'))

    player_choice = str(input('Player choice: [ R/P/S ] ')).upper()

    if player_choice not in ("R","P","S"):
        print('Incorect input, try again. ')
        continue

    gen = {1:'R',2:'P',3:'S'}
    comp_choice = random.randint(1,3)

    if player_choice == comp_choice:
        print('A drow')
    if (player_choice,comp_choice) in win:
        print('You win ! ')
    else:
        print("Computer win ")

    should_conitue = str(input('Did you want proced? [y/n]')).lower() == 'y'

