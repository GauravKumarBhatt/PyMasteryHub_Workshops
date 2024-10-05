#add two numbers
# num1 = input()
# num2 = input()
# sum = num1 + num2
# print('the sum of {0} and {1} is {2}'.format(num1,num2,sum))


#-----squre_root
# n = float(input())
# num_sqrt = n**0.5
# print('the sqrt of %f is %f'%(n, num_sqrt))

# import cmath
# num = 1 + 2j
# num_sqrt = cmath.sqrt(num)

# print(num_sqrt)

#----------Area of Triangle------------
# b = float(input('enter the base of triangle'))
# h = float(input('enter the height of triangle'))

# area = 0.5 * b * h
# print('the area of triangle is %f' % area)

# a = float(input('enter side a'))
# b = float(input('enter side b'))
# c = float(input('enter side c'))
# s = (a+b+c) / 2

# area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
# print('the area of triangle is %f' % area)


#-----------solve quardic Quactions------------
import cmath
a = float(input('enter a: '))
b = float(input('enter b: '))
c = float(input('enter c: '))

#----calculate the discriminat
d = (b**2) - (4*a*c)
#find two solutions
sol1 = (-b - cmath.sqrt(d)) / 2*a
sol2 = (-b + cmath.sqrt(d)) / 2*a

# sol1 = (-b + (b*b-4*a*c)**0.5) / 2*a
# sol2 = (-b + (b*b-4*a*c)**0.5) / 2*a
print('The solution are {0} and {1}'.format(sol1,sol2))