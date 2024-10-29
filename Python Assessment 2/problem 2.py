n = int(input('Please input a value for n: '))
first = False
for i in range(n-1):
    e = n-i
    temp = e
    #finds factorial of the numbers less than and equal to n
    for y in range(1, e):
       total = temp *(e-y)
       temp = total
    #if this is the first itteration it sets the sf to the current total, if not it times the sf by the current total, by the end of all itterations they will sum to the super factorial
    if first == False:
        sf = total
        first = True
    else:
        sf = sf*total
print(sf)
       



