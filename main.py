import random
def number_guess():
    lives = 0

    difficulty = input('welcome to the guessing game would you like easy or hard: ')

    if difficulty == 'easy':
        lives = 10
    else:
        lives = 5
    random_number = random.choice(range(100))
    user_pick = ''
    while user_pick != random_number and lives > 0:
        user_pick = int(input('guess the number between 1 - 100: '))
        if user_pick > random_number:
            lives -=1
            print(f'too high try again: {lives} lives left: ')
        elif user_pick < random_number:
            lives -=1
            print(f'too low try again: {lives} lives left: ')
        else:
            print('Correct')
            return
    if lives <= 0:
        print('you lose')
number_guess()



    
    