print('Pointless Game')
n = 4
south_africa = 26
new_zealand = 22
australia = 23
england = 29
france = 0
count = 0
points = 0
#Function used to calculate score, can be called within while loop
#function allows for construction outside of while loop for better readability
def point_score(q_input):
    if q_input == 'south africa':
        return 26
    elif q_input == 'new zealand':
        return 22
    elif q_input == 'australia':
        return 23
    elif q_input == 'england':
        return 29
    elif q_input == 'france':
        return 0
print(f'You have {n} guesses:')
print('Name a country that has played in the rugby world cup final')
while count < n:
    question = (input(f'Guess {count+1}:\n')).lower()
    points += point_score(question)
    if point_score(question) == 0:
        pointless = 'guessed pointless correctly'
        print('congrats!')
        break
    else:
        pointless = 'did not guess pointless correctly'
    count+=1
print(f'you {pointless} with {points} accumulated points.')
#counts score using point_score function, ends the loop if it is greater than n
#Also ends loop if pointless is guessed i.e if the function outputs 0
