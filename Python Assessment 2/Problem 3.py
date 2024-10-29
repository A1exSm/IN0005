word = ['A', 'P', 'P', 'L', 'E', 'S']
display = ['_', '_', '_', '_', '_', '_']
guessed = ''
k = 10
g = 0
game = True
print('If you would like to quit the game at any point simply input stop')
while game == True:
    if not '_' in display:
        print(f'------------------------\nYou won in {g}/{k} guessess\n------------------------')
        break
    else:
        print('\n\nGuessing game\n')
        print(' '.join(display))
        print(f'\nSo far used letters: {guessed}')
        guess = input('Guess the word: ')
        #changes the input into an uppercase string which allows for communication between the guess & word list
        guess = str(guess).upper()
        guessed = guessed + guess
        g += 1
        if guess in word:
            #itterates through, to make sure, if needed, multiple letters can be uncovered in the display list
            for i in range(len(word)):
                if word[i] == guess:
                    display[i] = guess
                else:
                    continue
            print(f'{g}/{k} guessess used')
            print(' '.join(display))
            continue
        elif guess == 'APPLES':
            #this checks if the player has guessed the whole word
            print(f'You won in {g}/{k} guessess')
            break
        elif g == k:
            #this is to end the game if all guesses are used without having won
            print(f'Sorry, you have lost! all {g} guessess were used')
            break
        elif guess == 'STOP'.upper():
            #This facilitates the players ability to terminate the game
            print('--------------------------\ngame forcefully terminated\n--------------------------')
            game = False
        else:
            continue
