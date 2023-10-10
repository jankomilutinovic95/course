import random


def guess(x):
    random_num = random.randint(1, x)
    gues = 0
    while guess != random_num:
        gues = int(input(f"Guess a number between 1 and {x}: "))
        if gues < random_num:
            print("Num too low")
        elif gues > random_num:
            print("Num too high")
        else:
            print("Correct!")


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            gues = random.randint(low, high)
        else:
            gues = low
        gues = random.randint(low, high)
        feedback = input(f'Is {gues} too high (H), too low (L), or correct (C)? ').lower()
        if feedback == 'h':
            high = gues - 1
        elif feedback == 'l':
            low = gues + 1
        else:
            print('Correct!')


computer_guess(10)
