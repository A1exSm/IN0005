#root finder
tol = 0.000001
nMax = 5000
#a, b, c... = co, assigns values to co
def f(x, co):
    a, b, c, d, e, f = co
    return a*x**5 + b*x**4 + c*x**3 + d*x**2 + e*x + f
#function created based on pseudo code, with minor changes in logic (changes are explained)
def rootFinder(co, a, b):
    n = 0
    #limit iterations to prevent infinite loop
    while n < nMax:
        c = (a + b) /2
        
        if f(c, co) == 0 or (b - a) /2 < tol: # solution found
            return c

#comment below is on the basis of the intermediate value theorem (found on google search)
#new interval, we multiply since they share a sign function if the product is positive there is a root in the interval i.e > 0, thus we change the interval if it is < 0 since this means there is no root in the current interval 
        if f(c, co) * f(a, co) < 0:
            b = c
        else:
            a = c
        n += 1
    return False

#inputing the coefficients and appending them to the coef list
coef = []
for i in range(6):
    coef_Temp = float(input(f'coefficient {i+1}: '))
    coef.append(coef_Temp)

#asks for interval values
a = float(input('Enter value of "a": '))
b = float(input('Enter value of "b": '))

soln = rootFinder(coef, a, b)

if soln: #solution found
    print(f'Root: {soln}')
else:
    print('Method failed.')
