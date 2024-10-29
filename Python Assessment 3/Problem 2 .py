import random
#Using A dict for our die allows allows us to easily call them later when generating random numbers
#BTW i made these die myself :) 
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
#The loop here means that we don't have to repetitavely call the code.
while True:
    #This section here checks whether the players would like to exit the game programme
    status = (str(input('If you would like to exit input end: '))).lower()
    if status == 'end':
        break
    else:
        print('The game is starting!')
    #Here i have used a dict to init the players lives, they can easily be accessed and opperated
    players = {1:5,2:5,3:5,4:5,5:5,6:5}
    #This loop here calls the actual game code repeadetly until someone wins or the game ends
    while True:
        temp2=5
        #First the programme checks whether any player has won the game, or if everyone has run out of lives
        for i in players.values():
            if int(i) == 0:
                temp2-=1
            else:
                temp2-=0
        if temp2 < 2:
            draw = 0
            for i in range(1,7):
                if int(players[i]) > 0:
                    print('------------------------------')
                    print(f'Player{i} has won! Game over!')
                    print('------------------------------')
                else:
                    draw+=1
                    if draw == 6:
                        print('-----------------------------')
                        print('Everyone has lost! Game over!')
                        print('-----------------------------')
                        
            break
        else:
        #the following functions were created as such to help me develop this (thought process)
            def player_guess():
                return {i:int(input(f'Player{i} | Guess the sum of the 3 die: ')) for i in range(1,7)}
            guess = player_guess()
            #Here is where we geneare 3 random intergers between 1 and 6 using import random
            def threeR():
                temp = {1 : random.randint(1,6),2 : random.randint(1,6),3 : random.randint(1,6)}
                for value in temp.values():
                    print(dice[value])
                return (temp[1] + temp[2] + temp[3])

            sum1 = threeR()
            #Here we update the users remaining guesses, these can be easily accessed through the players dict
            for i in range(1,7):
                if guess[i] != sum1:
                    players[i]-=1
                    print(f'Player{i} has {players[i]} guesses left!')
                else:
                    print(f'Player{i} has {players[i]} guesses left!')
