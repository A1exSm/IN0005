#Memory Game
def start():
    status = True
    answers_1 = ['A', 'E', 'C', 'B', 'T', 'Q','Y', 'Z']
    answers_2 = ['E', 'Q', 'A', 'C', 'T', 'Y', 'Z', 'B']
    astrix_1 = ['*', '*', '*', '*', '*', '*', '*', '*']
    astrix_2 = ['*','*', '*', '*', '*', '*', '*', '*']
    inputX = 0
    inputY = 0
#functions input 1 & 2 take the inputed value and subtract 1 to allow use of indexing
    def input1():
        temp = int(input('Position (interger between 1-8): '))
        temp2 = temp -1
        return temp2

    def input2(inputA):
        temp = int(input(f'Guess the position of {answers_1[inputX-1]} in row two (interger betwen 1-8): '))
        temp2 = temp -1        
        if answers_1[inputA] == answers_2[temp2]:
            return temp2
        else:
            return 'wrong'
            
    def input_1x():
        temp = input1()
        astrix_1[temp] = answers_1[temp]
        print(' '.join(astrix_1))
        print(' '.join(astrix_2))
        return temp
#function input_2x & 1x check whether the values match the one in the other list, then return a corrosponding statement
    def input_2x(temp):
        global status
        temp2 = input2(temp)
        if temp2 == 'wrong':
            print('Try again!')
            status = False
            return status
                    
        elif str(temp2) == '0':
#This code for some reason does not recognise that the value 'E' exists in index 0 in answers_2, thus cannot compare the values to see of the values match. This conditional checks if the index is 0 in inputY, if so it will unvail E and pass as correct
            astrix_2[0] = answers_2[0]
            print(' '.join(astrix_1))
            print(' '.join(astrix_2))
            status = True
            return status
                    
        else:
            astrix_2[temp2] = answers_2[temp2]
            print(' '.join(astrix_1))
            print(' '.join(astrix_2))
            status = True
            return status

    print(' '.join(astrix_1))
    print(' '.join(astrix_2))
    n=0
#This while loop runs 8 times (the number of itteration until you can win)
#The while loop ends if an incorrect answer is given and status == False, if the loop ends while status == True, the player has won
    while n < 8:
        temp = input_1x()
        status = input_2x(temp)
        if status == False:
            break
        else: 
            n+=1
    if status == True:
        print('you won')
start()
