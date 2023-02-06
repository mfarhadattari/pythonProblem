# Find the largest of the three numbers.
import math 

a = int(input('Enter an integer Number: '))
b = int(input('Enter an integer Number: '))
c = int(input('Enter an integer Number: '))

if a > b and a > c:
    print('Largest Number = ', a)
elif b  > c:
    print('Largest Number = ', b)
else:
    print('Largest Number = ', c)

largest = max(a , b , c)
print('Largest Number = ', largest)