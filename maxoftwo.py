# 
import math
num1 = int(input('Integer Number: '))
num2 = int(input('Integer Number: '))

if num1 > num2:
    print('Largest Number = ', num1) 
else:
    print('Largest Number = ', num2) 


largest = max(num1 , num2)
print('Largest Number = ', largest)