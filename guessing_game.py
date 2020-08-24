import random

LOW_NUMBER = 0
HIGH_NUMBER = 100

random_number = random.randint(LOW_NUMBER, HIGH_NUMBER)


def get_guess():
    guess = ''
    entered_int = False
    while not entered_int:
        try:
            guess = input(f'Guess an integer between {LOW_NUMBER} and {HIGH_NUMBER} (inclusive): ')
            number = int(guess)
            entered_int = True
        except ValueError:
            print(f'"{guess}" is not an integer!')

    return number


def evaluate_guess(guess):
    result = ''
    if guess > random_number:
        result = 'high'
    elif guess < random_number:
        result = 'low'
    else:
        result = 'equal'

    return result


def tellUser(result):
    print(f'Your guess is too {result}')


def main():
    number_guesses = 0
    
    name = input('Enter your name: ')
    print(f'\nHello, {name}!')

    isGuessed = False
    while not isGuessed:
        result = evaluate_guess(get_guess())
        number_guesses += 1
        if result == 'equal':
            isGuessed = True
        else:
            tellUser(result)
        
    print(f'\nYou guessed it in {number_guesses} guesses!')
    print(f'\nGoodbye, {name}!\n')


if __name__ == '__main__':
    main()
