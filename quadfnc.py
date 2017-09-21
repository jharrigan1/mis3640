def print_lyrics():
    print("Hey Jude. Don't make it bad.")
    print("Take a sad song and make it better.")



print_lyrics()

print(type(print_lyrics))

def repeat_lyrics():
    print_lyrics()
    print('Na - na - na - na - na, na - na - na - na')
    print_lyrics()

#repeat_lyrics()

def print_twice(name):
    print(name)
    print(name)

#print_twice('Andrew')

my_name = 'Julia'
#print_twice(my_name)


def cat_twice (part1, part2):
    cat = part1 + part2
    print_twice(cat)

line1 = 'Bing tiddle '
line2 = 'tiddle bang.'
cat_twice(line1, line2)


def give_me_a_break():
    str1 = 'break'
    return str1
print(give_me_a_break()*10)

def give_me_a_break():
    str1 = 'break'
    return str1
    print('another break')
print(give_me_a_break)

result = print_twice('Bing')
print(result)

def nop():
    pass

age= int(input())
if age >= 18:
    pass

import math
def move(x, y, step, angle):
    nx = x + step + math.cos(angle)
    ny = y - step + math.sin(angle)
    return nx, ny
x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

def quadratic(a, b, c):
    discriminant = b**2 - 4 * a * c #calculate the discriminant

    if discriminant >= 0:
        x_1 = ((-b + math.sqrt(discriminant)) / 2 * a)
        x_2 = ((-b - mathsqrt(discriminant)) / 2 *a)
        return x_1, x_2
    
    else:
        print('No real number solution.')
        return None

print(quadratic(2,2,2))

a = float(input('enter number'))
b = float(input('enter number.'))
c = float(input('enter number.'))
print('Results are')

    
#Solving a quadratic function
import math
import cmath

#Define the quadratic variables
def quadratic(a,b,c):
   A = (b**2)-(4*a*c)
if A >= 0:
       X1 = ((-b + math.sqrt(A)) / 2*a)
       X2 = ((-b - math.sqrt(A)) / 2*a) 
return X1, X2
else:
    print('No Real Solution')

#output of variables
a = int(input('Enter a number:'))
b = int(input('Enter a number:'))
c = int(input('Enter a number:'))

#print equation solution(s)
print('results are: ')
print(quadratic(a,b,c))

input()