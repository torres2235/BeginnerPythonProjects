import random

def guess(x): #we guess the computer's random number
    random_num = random.randint(1,x)
    guess = 0
    while guess != random_num:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        
        if guess < random_num:
            print('Too low')
        if guess > random_num:
            print('Too high')

    print(f'Correct! The number is {random_num}!')

def computer_guess(x): #the computer guesses our random number
    low = 1
    high = x
    feedback = ''

    while feedback !='c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?'.lower())
        
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'The computer has successfully guessed your number, {guess}')

guess(10)
computer_guess(10)