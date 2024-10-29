print('HCF & LCM')
import math
print('In the following 2 prompts, input 1 non-zero interger in each')
number1 = int(input('prompt 1:\n'))
number2 = int(input('prompt 2:\n'))
# Uses greatest common devider and lowest common multiple from math library after turning inputs into INT 
if number1 > 0 and number2 > 0:
    hcf = math.gcd(number1, number2)
    lcm = math.lcm(number1, number2)
    print(f'{hcf} (the HCF) and {lcm} (the LCM) for {number1} & {number2} ')
else:
    print('please input non-zero intergers')
