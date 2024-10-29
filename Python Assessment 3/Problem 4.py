#import Random for dice and time so that information does not display too fast
import random
import time
#dicts for game board and each individual die outcome
#Using dict like this for the board alows us to use coordinates to plot positions
field = {
    7 : ['|___|', '|___|', '|___|', '|___|', '|___|', '|___|', '|___|', '|___|'],
    6 : ['|___|', '|___|', '|___|', '|___|', '|___|', '|___|', '|___|', '|___|'],
    5 : ['|___|', '|___|', '|___|', '|___|', '|___|', '|___|', '|___|', '|___|'],
    4 : ['|___|', '|___|', '|___|', '|___|', '|___|', '|___|', '|___|', '|___|'],
    3 : ['|___|', '|___|', '|___|', '|___|', '|___|', '|___|', '|___|', '|___|'],
    2 : ['|___|', '|___|', '|___|', '|___|', '|___|', '|___|', '|___|', '|___|'],
    1 : ['|___|', '|___|', '|___|', '|___|', '|___|', '|___|', '|___|', '|___|'],
    0 : ['|___|', '|___|', '|___|', '|___|', '|___|', '|___|', '|___|', '|___|']
}
dice = {
    1 : """
 _ _ _ _ _ _ _
|             |
|             |
|             |
|      *      |
|             |
|             |
|_ _ _ _ _ _ _|""",
    
    2 : """
 _ _ _ _ _ _ _
|             |
|             |
|        *    |
|             |
|    *        |
|             |
|_ _ _ _ _ _ _|""",
    
    3 : """
 _ _ _ _ _ _ _
|             |
|         *   |
|             |
|      *      |
|             |
|   *         |
|_ _ _ _ _ _ _|""",
    
    4 : """
 _ _ _ _ _ _ _
|             |
|             |
|  *      *   |
|             |
|  *      *   |
|             |
|_ _ _ _ _ _ _|""",

    5 : """
 _ _ _ _ _ _ _
|             |
| *        *  |
|             |
|      *      |
|             |
| *        *  |
|_ _ _ _ _ _ _|""",

    6 : """
 _ _ _ _ _ _ _
|             |
|   *     *   |
|             |
|   *     *   |
|             |
|   *     *   |
|_ _ _ _ _ _ _|"""
}
#defining initial global variables
p_pos, q_pos, game =[0,0], [0,0], True
#Created the functions which the game will use to run
#Using functions in this way allows more efficient use of code
def line_update(player):
    #This function moves the player up a line
    global q_pos
    global p_pos
    if player == 'p':
        p_pos[0]+=1
        p_pos[1]=0
    elif player == 'q':
        q_pos[0]+=1
        q_pos[1]=0

def value_check(number, player):
    #Here we copy p_pos/q_pos so that we don't have issues if there is a change in the original p_pos/q_pos
    check = player
    if player == 'p':
        target = p_pos.copy()
    elif player == 'q':
        target = q_pos.copy()
    #checks whether the player has won, and if the number is exactly that needed to win
    if target[0] == 7 and target[1] >= 1:
        if target[1] + number > 7:
            return 0
        elif target[1] + number == 7:
            return 'win'
        else:
            return number
    #Checks whether a new line needs to be taken into account, and calcs
    elif target[1] + number > 7:
        temp = 8 - target[1]
        new = number - temp
        clean(check)
        line_update(check)
        return new
    
    else:
        return number

def clean(player):
    global p_pos
    global q_pos
    #This function clear up the previous square in which the player moved from, and ensures it is updated properly
    pr = player
    if pr == 'p':
        if field[p_pos[0]][p_pos[1]] == '|P Q|':
            field[p_pos[0]][p_pos[1]] = '| Q |'
        else:
            field[p_pos[0]][p_pos[1]] = '|___|'
    elif pr == 'q':
        if field[q_pos[0]][q_pos[1]] == '|P Q|':
            field[q_pos[0]][q_pos[1]] = '| P |'
        else:
            field[q_pos[0]][q_pos[1]] = '|___|'

def refresh(player='both'):
    #This referesh function updates the players new position, and also updates/prints the new board layout to the output
    if player == 'p': 
        if field[p_pos[0]][p_pos[1]] == '| Q |':
            field[p_pos[0]][p_pos[1]] = '|P Q|'
        else:
            field[p_pos[0]][p_pos[1]] = '| P |'
            
    elif player == 'q':     
        if field[q_pos[0]][q_pos[1]] == '| P |':
            field[q_pos[0]][q_pos[1]] = '|P Q|'
        else:
            field[q_pos[0]][q_pos[1]] = '| Q |'
            
    elif player == 'both':
        if field[p_pos[0]][p_pos[1]] == '| Q |':
            field[p_pos[0]][p_pos[1]] = '|P Q|'
        else:
            field[p_pos[0]][p_pos[1]] = '| P |'
            
        if field[q_pos[0]][q_pos[1]] == '| P |':
            field[q_pos[0]][q_pos[1]] = '|P Q|'
        else:
            field[q_pos[0]][q_pos[1]] = '| Q |'
        
    for i in field.values():
        print(' '.join(i))
        print()

def roll(player):
    global game
    global p_pos
    global q_pos
    temp = random.randint(1,6)
    print('rolling...')
    time.sleep(1)
    print(dice[temp])
    pr = (str(player)).lower()
    checked = value_check(temp, pr)
    clean(pr)
    #Here we need to ensure that the game updates and refreshes the board despite a player having won, and not just ending the programme
    if checked != None:
        if checked != 'win':
            temp = checked
        if pr == 'p':
            p_pos[1] += temp
            time.sleep(1)
            print()
            refresh('p')
        elif pr == 'q':
            q_pos[1] += temp
            time.sleep(1)
            print()
            refresh('q')
        if checked == 'win':
            print('----------------------------')
            print(f"Player{pr.upper()} has won!")
            print('----------------------------')
            game = False
#Starting print & Game loop
refresh()
print('The aim of this game is to reach the top (left to right)! \nPlayer P Starts!')
time.sleep(3) 
while game:
    if game == False:
        break
    input(f"It's PlayerP's turn to roll, press the ENTER key to roll: ")
    roll('p')
    time.sleep(1)
    if game == False:
        break
    print()
    input(f"It's PlayerQ's turn to roll, press the ENTER key to roll: ")
    roll('q')
#Thank you for reading my code!