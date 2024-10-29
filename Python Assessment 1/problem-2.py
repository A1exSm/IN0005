print('Armstrong Number')
number = str(input('Enter a number: \n'))
power = (len(number))
sum_number = 0
for i in number:
    sum_number += (int(i))**power
if sum_number == int(number):
    answer = 'is'
elif sum_number != int(number):
    answer = 'is not'
print(f'{number} {answer} a Armstrong Number.')
#input stored as string in order to get len and itteratre through in for loop
#power set to the length so that we can ** numbers regardless of their length
#for loop sums each interger to the power of length which makes up the input
#if the total is equal to the original input as an int then it is an armstrong number
