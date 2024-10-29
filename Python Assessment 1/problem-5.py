print('Stern-Brocot Sequence')
stern_list = [1,1]
n = int(input('Input how many numbers you want in the Stern-Brocot sequence:\n'))
stern_list = [1,1]
#loops through 1 to the inputed n, this means we can access the relevant values from the list using i
#set the considered to the current list index i, i.e the current value
#set the preceding value as the previous list value using the current i-1 as the index
#appends to the list the sum of the considered and preceding
#checks whether the length of the list is greater than our inputed length
#we do this again after appending the concidered value as for each itteration we are actually appending two to the list, so we must check if we have exceed n after each is appended
for i in range(1,  n):
    numC = stern_list[i]
    numP = stern_list[i-1]
    stern_list.append(numC + numP)
    if len(stern_list) == n:
        break
    stern_list.append(numC)
    if len(stern_list) == n:
        break
#printing the list length is to ensure that we can visually see there is n values as requested without having to manually count.
print(f'list length = {len(stern_list)}')
print('\nOutput:')
print(stern_list)
#Using a loop which increments by 2, allows me to use addition to format the real numbers
#I append the real numbers as string as to allow me to use the / symbol
#I have placed a break statement to ensure that when n is odd the loop won't go out of range, since the last value would anyways be formated and appended in the previous itteration.
#the second break statement is to prevent going out of range if n is equal since i+2 would be n+1 so we need to check that we are at n-2
print('\nReal Number Output:')
real_stern_list = []
for i in range(0, len(stern_list), 2):
    if i == n-1:
        break
    real_stern_list.append(str(stern_list[i])+'/'+str(stern_list[i+1]))
    if i == n-2:
        break
    real_stern_list.append(str(stern_list[i+1])+'/'+str(stern_list[i+2]))
print(real_stern_list)
