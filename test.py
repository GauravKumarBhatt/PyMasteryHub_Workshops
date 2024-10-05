#--------add two numbers
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
# import cmath
# a = float(input('enter a: '))
# b = float(input('enter b: '))
# c = float(input('enter c: '))

# #----calculate the discriminat
# d = (b**2) - (4*a*c)
# #find two solutions
# sol1 = (-b - cmath.sqrt(d)) / 2*a
# sol2 = (-b + cmath.sqrt(d)) / 2*a

# # sol1 = (-b + (b*b-4*a*c)**0.5) / 2*a
# # sol2 = (-b + (b*b-4*a*c)**0.5) / 2*a
# print('The solution are {0} and {1}'.format(sol1,sol2))

#----------swap two numbers-----------
# a = 5
# b = 10

# temp = a
# a = b
# b = temp
# print('afer swaping value of a and b is', a,b)

# x = 5
# y = 10

# x, y = y, x
# print("x =", x)
# print("y =", y)

# #----------generate random number----------
# import random
# print(random.randint(0,9))


##------------convert kilometers into miles----------
# km = float(input('enter the distance in km:'))
# miles = km * 0.621371
# print('distance in miles is %f' % miles)


# #-----------------check number is +ve, -ve and 0 ----------------
# num = int(input("enter the number:"))
# if (num>0):
#     print('number is positive')
# elif (num<0):
#     print('number is negative')
# else:
#     print('number is zero')



# #-------------check number is even or odd------------------
# num = int(input('enter the number:'))
# if num%2 == 0:
#     print("{0} is Even".format(num))
# else:
#     print("{0} is Odd".format(num))



# #-------------check leap year--------------
# year = int(input('enter the year to know the leap year: '))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a leap year.")
# else:     
#     print(f"{year} is not a leap year.")
    

# #-----------find the largest among three Numbers---------------
# num1 = 5
# num2 = 8
# num3 = 3
# if ((num1>num2) and (num1>num3)):
#     print(num1,"is greater")
# elif ((num2>num1) and (num2>num3)):
#     print(num2,"is greater")
# else:
#     print(num3,"is greater")


# #-----------------check number is prime or not-------------
# num = int(input("enter the number: "))
# if num == 0 or num == 1:
#     print(num, 'is not prime')
# elif ((num%2) != 0):
#     print(num,"is prime")
# else:
#     print(num,"is not prime")



#---------------factorial of a number----------------
# num = int(input("enter the number: "))
# fact = 1
# for i in range(1,num+1):
#     fact = fact*i
# print(fact)

# def factorial(x):
#     if x == 1:
#         return 1
#     else:
#         return (x * factorial(x-1))

# num = int(input("enter the number: "))
# print("The factorial of", num, "is", factorial(num))



##----------------multiplication table-----------------
# # Recursive function to print multiplication table
# def print_multiplication_table(num, multiplier=1):
#     if multiplier > 10:
#         return
#     print(f"{num} x {multiplier} = {num * multiplier}")
#     print_multiplication_table(num, multiplier + 1)

# # Input from the user
# num = int(input("Enter a number: "))

# # Call the recursive function
# print_multiplication_table(num)


# Multiplication table (from 1 to 10) in Python

# num = 12
# for i in range(1, 11):
#    print(num, 'x', i, '=', num*i)


##--------Python Program to Print the Fibonacci sequence-------------
# def fibonacci(n):
#     if n <= 0:
#         return "Input should be positive integer."
#     elif n == 1:
#         return [0]
#     elif n == 2:
#         return [0, 1]
#     else:
#         fib_list = [0, 1]
#         while len(fib_list) < n:
#             fib_list.append(fib_list[-1] + fib_list[-2])
#         return fib_list
# print(fibonacci(10))


# nterms = int(input("how many terms?"))
# n1, n2 = 0, 1
# count = 0

# if nterms <= 0:
#     print("enter positive integer")
# elif nterms == 1:
#     print("fibonacci sequence upto", nterms, ":")
#     print(n1)
# else:
#     print("fibonacci sequence")
#     while count < nterms:
#         print(n1)
#         nth = n1 + n2
#         n1 = n2
#         n2 = nth
#         count += 1


##---------------sum of natural number up to -----------------------
# num = int(input('Enter the number: '))
# sum = 0
# for i in range(1, num+1):
#     sum = sum + i
# print('The sum is:',sum)


