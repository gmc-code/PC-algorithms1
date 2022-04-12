num = 12
guess = 0
guess_limit=3
guess_number = 0
while guess_number < guess_limit:
    guess = int(input(f'Guess # {guess_number+1} a number 1-20: last guess:{guess} '))
    if guess == num:
        print(f'You Win! You Guessed it: {guess}')
        break
    else:
        print(f'No, not {guess}!')
        guess_number += 1
if guess != num:
    print(f'Sorry you lose! It was {num}')