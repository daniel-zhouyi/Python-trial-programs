"""
#1 Bagels
2023 Nov. 7
daniel.yi.zhou@outlook.com

"""
import random
NUM_DIGITS = 3
MAX_GUESS = 10

def main():
    print('''Bagels, a deductive logic game.
    I'm thinking of a {}-digit number with no repeated digits.'''.format(NUM_DIGITS))

    while True:
        secret_num = getSecretNum()
        print('I''ve thought up a number.')
        print('You have {} guesses to get it.'.format(MAX_GUESS))

        numGuesses = 1
        while numGuesses <= MAX_GUESS:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}'.format(numGuesses))
                guess = input('> ')

                clues = getClues(guess, secret_num)
                print(clues)
                numGuesses += 1

                if guess == secret_num:
                    break

        if numGuesses > MAX_GUESS:
            print('You ran out of guesses.')
            print('The answer was {}'.format(secret_num))

            print('Do you want to play again?(yes or no)')
            if not input('> ').lower().startswith('y'):
                break

    print('Thanks for playing!')

def getSecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)

    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])

    return secretNum

def getClues(guess, secretNum):
    if guess == secretNum:
        return 'You got it!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi ')
        elif guess[i] in secretNum:
            clues.append('Pico ')

    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()

    return ''.join(clues)


if __name__ == '__main__':
    main()
