epsilon = 0.00001
def estimate(a):
    #calculates estimates using the formula provided, increasing n by 1 each itteration
    put = a / 2
    n = 0
    while abs(put**2 - a) > epsilon:
        #0.5 instead of 1/2
        put = 0.5 * (put + a / put)
        print(put)
        n += 1
    return put

value = float(input('input a positive interger (a) to see the square root using the Babylonian Method: '))
length = len(str(value))
answers = estimate(value)
print(answers)
