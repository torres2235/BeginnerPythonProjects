import random

def guess(x):
    random_num = random.randint(1,x)
    guess = 0
    while guess != random_num:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        
        if guess < random_num:
            print('Too low')
        if guess > random_num:
            print('Too high')

    print(f'Correct! The number is {andom_num}!')

guess(10)