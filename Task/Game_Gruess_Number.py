import random

number = random.randint(1, 50)

tries = 0

while tries < 6:
    grues = int(input('Guess the number: '))

    tries += 1

    if grues < number:
        print(f'Number in greater.You have {tries}/6 tries')
    if grues > number:
        print(f'Number is less.You have {tries}/6 tries')
    if grues == number:
        print(f'You gruess the number! You have {tries}/6 tries')

    if grues != number and tries == 6:
        print(f'You didn\'t gruess the number. The number was {number}.')


