matrix = {
    1 : ['_','_','_'],
    2 : ['_','_','_'],
    3 : ['_','_','_']
}
#symbols used for players
player1, player2 = 'X', 'O'
print('-----------How to play-----------\nPlayer ? enter your move: 2,1\n output: \n_ _ _\nO _ _\n_ _ _\n-----------How to play-----------\n')
notWon = True
p1_count = 0
p2_count = 0
player = 1
print(f'Player 1 is {player1} and Player 2 is {player2}')
print(f"{' '.join(matrix[1])}\n{' '.join(matrix[2])}\n{' '.join(matrix[3])}\n")
while notWon:
    if player == 1:
        input1 = str(input('Player 1 enter your move: '))
        print()
        #ensures that the first condition for the correct input syntax is fulfilled, if not points it out and starts again
        if len(input1) != 3:
            print("Please enter your input in the same format as shown in the 'How to play' section ")
            print("If the input is incorrect the game will be terminated, please consult the 'How to play' section before inputing")
            input1 = input('Player 1 enter your move: ')
            print()

            if len(input1) != 3:
                print('Game ended due to repeated incorrect input')
                break
        #checks whether the total of both inputs are greater than six, the largest possible combinations of outputs (i.e row three and column three)
        if int(input1[0]) + int(input1[-1]) > 6:
            print("You have inputed a number that exceeds the possible values to input")
            print("If the input is incorrect for a second time the game will be terminated")
            input1 = input('Player 1 enter your move: ')
            print()

            #game ends, as what is the point of playing when one cannot follow the rules
            if int(input1[0]) + int(input1[-1]) > 6:
                print('Game ended due to repeated incorrect input')
                break

        elif matrix[int(input1[0])][int(input1[-1])-1] == player2 or matrix[int(input1[0])][int(input1[-1])-1] == player1:
            print("You have chosen a place that is already occupied")
            print("If the input is incorrect for a second time the game will be terminated")
            input1 = input('Player 1 enter your move: ')
            print()
            
            if matrix[int(input1[0])][int(input1[-1])-1] == player2 or matrix[int(input1[0])][int(input1[-1])-1] == player1:
                print('Game ended due to repeated incorrect input')
                break
        p1_count +=1
        
        matrix[int(input1[0])][int(input1[-1])-1] = player1
        print(f"{' '.join(matrix[1])}\n{' '.join(matrix[2])}\n{' '.join(matrix[3])}\n")
    #A copy of the code for player 1, the same logic, however for player 2.
    elif player == 2:
        input1 = str(input('Player 2 enter your move: '))
        print()
        if len(input1) != 3:
            print("Please enter your input in the same format as shown in the 'How to play' section ")
            print("If the input is incorrect the game will be terminated, please consult the 'How to play' section before inputing")
            input1 = input('Player 2 enter your move: ')
            print()

            if len(input1) != 3:
                print('Game ended due to repeated incorrect input')
                break
            
        if int(input1[0]) + int(input1[-1]) > 6:
            print("You have inputed a number that exceeds the possible values to input")
            print("If the input is incorrect for a second time the game will be terminated")
            input1 = input('Player 2 enter your move: ')
            print()
            
            if int(input1[0]) + int(input1[-1]) > 6:
                print('Game ended due to repeated incorrect input')
                break

        elif matrix[int(input1[0])][int(input1[-1])-1] == player2 or matrix[int(input1[0])][int(input1[-1])-1] == player1:
            print("You have chosen a place that is already occupied")
            print("If the input is incorrect for a second time the game will be terminated")
            input1 = input('Player 2 enter your move: ')
            print()
            
            if matrix[int(input1[0])][int(input1[-1])-1] == player2 or matrix[int(input1[0])][int(input1[-1])-1] == player1:
                print('Game ended due to repeated incorrect input')
                break
        #allows keeping track of how many turns have occured to check for a winner
        p2_count +=1
        #subtracts 1 for indexing
        matrix[int(input1[0])][int(input1[-1])-1] = player2
        print(f"{' '.join(matrix[1])}\n{' '.join(matrix[2])}\n{' '.join(matrix[3])}\n")

    #Checks whether any of the possible combinations to win have occured or a draw has occured, if so the while loop breaks ending the game
    if p1_count > 2 or p2_count > 2:
        if (matrix[1][0] == player1 and matrix[1][1] == player1 and matrix[1][2] == player1) or (matrix[2][0] == player1 and matrix[2][1] == player1 and matrix[2][2] == player1) or (matrix[3][0] == player1 and matrix[3][1] == player1 and matrix[3][2] == player1):
            print('Player 1 is the Winner!')
            break
        elif (matrix[1][0] == player1 and matrix[2][0] == player1 and matrix[3][0] == player1) or (matrix[1][1] == player1 and matrix[2][1] == player1 and matrix[3][1] == player1) or (matrix[1][2] == player1 and matrix[2][2] == player1 and matrix[3][2] == player1):
            print('Player 1 is the Winner!')
            break
        elif (matrix[1][0] == player1 and matrix[2][1] == player1 and matrix[3][2] == player1) or (matrix[1][2] == player1 and matrix[2][1] == player1 and matrix[3][0] == player1):
            print('Player 1 is the Winner!')
            break
        elif (matrix[1][0] == player2 and matrix[1][1] == player2 and matrix[1][2] == player2) or (matrix[2][0] == player2 and matrix[2][1] == player2 and matrix[2][2] == player2) or (matrix[3][0] == player2 and matrix[3][1] == player2 and matrix[3][2] == player2):
            print('Player 2 is the Winner!')
            break
        elif (matrix[1][0] == player2 and matrix[2][0] == player2 and matrix[3][0] == player2) or (matrix[1][1] == player2 and matrix[2][1] == player2 and matrix[3][1] == player2) or (matrix[1][2] == player2 and matrix[2][2] == player2 and matrix[3][2] == player2):
            print('Player 2 is the Winner!')
            break
        elif (matrix[1][0] == player2 and matrix[2][1] == player2 and matrix[3][2] == player2) or (matrix[1][2] == player2 and matrix[2][1] == player2 and matrix[3][0] == player2):
            print('Player 1 is the Winner!')
            break
        elif (matrix[1].count('_') == 0 and matrix[2].count('_') == 0 and matrix[3].count('_') == 0):
            print('Draw!\nGame over!')
            break
    #checks who's turn just occured and ensures the next turn is given to the other player
    if player == 1:
        player = 2
    elif player == 2:
        player = 1
    

