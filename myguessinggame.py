from random import randint
welcome_string = ('Welcome to THE GUESSING GAME!!! \n'
                  'Guess please number from 1 to 100. \n'
                  'If your guess is within 10 of the number I will tell you "YOU ARE WARM!" \n'
                  'If your guess is further than 10 away from the number I will tell you "YOU ARE COLD!" \n'
                  'If your further guesses are closer to the previous ones I will tell you WARMER! \n'
                  'If your further guesses are farther than the previous ones I will tell you "COLDER!" \n'
                  'GOOD LUCK!!! \n'
                  "Let's play. Are you ready?")
print(welcome_string)

def next_game(play_again):
    while play_again != 'Y' and play_again != 'N':
        play_again = input('Do you want to play again? Type Y for yes or N for no: ').upper()
        print('\n' * 30)
        if play_again == 'Y':
            play_game(True, True)
        elif play_again == 'N':
            pass
        else:
            print("You didn't choose the right character.")

def play_game(x, y):
    num = randint(1, 100)
    while y == True:
        guesses_list = []
        guess = input('Please type here your guess from 1 to 100:')
        print('\n' * 30)
        if guess.isdigit():
            guess = int(guess)
        else:
            print("You didn't type a digit.")
            continue

        if guess < 1 or guess > 100:
            print("Your guess was OUT OF BOUNDS.")
            continue

        elif guess == num:
            print(f'Congratulations!!! The answer is {guess}. It took you only 1 guess to find the number.')
            x = False
            y = False
            next_game('')

        elif (num - 10) <= guess <= (num + 10):
            print('YOU ARE WARM! Try again.')
            y = False
            guesses_list.append(guess)
        else:
            print('YOU ARE COLD! Try again.')
            y = False
            guesses_list.append(guess)

    while x == True:
        guess = input('Please type here your guess from 1 to 100:')
        print('\n' * 30)

        if guess.isdigit():
            if int(guess) in guesses_list:
                print('You typed that number before. Choose another number.')
                continue
            guess = int(guess)
            guesses_list.append(guess)
        else:
            print("You didn't type a digit.")
            continue

        if guess < 1 or guess > 100:
            print("Your guess was OUT OF BOUNDS.")
            guesses_list.pop(-1)
            continue

        elif guess == num:
            print(f'Congratulations!!! The answer is {guess}. It took you only {len(guesses_list)} guesses to find the right number.')
            x = False
            next_game('')

        elif abs(num-guess) < abs(num-guesses_list[-2]):
            print('YOU ARE WARMER! Please try again.')

        elif abs(num - guess) == abs(num - guesses_list[-2]):
            print('Your guess is same close like previous one! ;) Please try again.')

        else:
            print('YOU ARE COLDER! Please try again.')


if_ready = ''
while if_ready != 'Y' and if_ready != 'N':
    if_ready = input('Please type Y for yes or N for no: ').upper()
    if if_ready == 'N':
        print('\n' * 50)
        pass

    elif if_ready == 'Y':
        print('\n' * 50)
        play_game(True, True)

    else:
        print('\n' * 50)
        print(welcome_string)
        print('\n')
        print("You didn't choose the right character.")

print('GAME OVER! \n'
      'GOOD BYE!')
