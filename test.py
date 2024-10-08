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


# def fibonacci(n):
#     if n <= 0:
#         print("incorrect input")
#     elif n==1:
#         return 0
#     elif n==2:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
# print(fibonacci(10))


##---------------sum of natural number up to -----------------------
# num = int(input('Enter the number: '))
# sum = 0
# for i in range(1, num+1):
#     sum = sum + i
# print('The sum is:',sum)

##------------------powers of 2 using anonymous function-------------------------
# power = lambda a : a**2
# result = power(2)
# print(result)

# terms = int(input('Enter the terms: '))
# result = list(map(lambda x: 2**x, range(terms)))
# print("The total terms are:",terms)
# for i in range(terms):
#     print("2 raised to power", i, "is", result[i])


##-------------------find numbers divisible by another numbers-------------------
# num1 = list(map(int, input("Enter the first number (dividend): ").split()))
# num2 = int(input("Enter the second number (divisor): "))

# if num2 == 0:
#     print("Division by zero is not allowed!")
# elif num1 % num2 == 0:
#     print(f"{num1} is divisible by {num2}.")
# else:
#     print(f"{num1} is not divisible by {num2}.")


# # Take a list of numbers
# my_list = [12, 65, 54, 39, 102, 339, 221,]

# # use anonymous function to filter
# result = list(filter(lambda x: (x % 13 == 0), my_list))

# # display the result
# print("Numbers divisible by 13 are",result)



# numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
# divisor = int(input("Enter the divisor: "))

# divisible_numbers = [num for num in numbers if num % divisor == 0]
# if divisible_numbers:
#     print(f"Numbers divisible by {divisor}: {divisible_numbers}")
# else:
#     print(f"No numbers are divisible by {divisor}")


##---------------find simple interest---------------
# P = int(input('enter P: '))
# T = int(input('enter T: '))
# R = int(input('enter R: '))
# SI = (P*T*R)/100
# print(f'Simple Interest is {SI}')

##------------------finding compound interest-----------------
# p = int(input('enter P: '))
# t = int(input('enter T: '))
# r = int(input('enter R: '))
# amount = p*(1+r/100)**t

# compound_Interest = amount - p
# print(f'Compound Interest is {compound_Interest}')

## ------------Python program to find H.C.F of two numbers--------------

# def compute_hcf(x, y):
#     if x > y:
#         smaller = y
#     else:
#         smaller = x
#     for i in range(1, smaller+1):
#         if((x % i == 0) and (y % i == 0)):
#             hcf = i 
#     return hcf

# num1 = 54 
# num2 = 24

# print("The H.C.F. is", compute_hcf(num1, num2))

# Function to find HCF the Using Euclidian algorithm
# def compute_hcf(x, y):
#    while(y):
#        x, y = y, x % y
#    return x

# hcf = compute_hcf(300, 400)
# print("The HCF is", hcf)

##-----------reverse a string------------
# string = 'a#b@c'
# result = string[ : :-2]
# print(result)  # Output: 'c@b#a'



##------------------Python Program to find the L.C.M. of two input number---------------------
# def compute_lcm(x,y):
#     if x>y:
#         greater = x
#     else:
#         grater = y
#     while(True):
#         if((greater % x == 0) and (greater % y == 0)):
#             lcm = greater
#             break
#         greater += 1
#     return lcm

# num1 = 54
# num2 = 24
# print("the L.C.M is", compute_lcm(num1,num2))

# def compute_gcd(x, y):
#     while(y):
#         x, y = y, x%y
#     return x

# def compute_lcm(x, y):
#     lcm = (x*y)//compute_gcd(x, y)
#     return lcm

# num1 = 54
# num2 = 24
# print("The LCM is", compute_lcm(num1, num2))

##--------------find factor of a number--------------------------
# def print_factors(x):
#     print("the factors of", x, "are")
#     for i in range(1, x+1):
#         if x % i == 0:
#             print(i)
# num = 320
# print_factors(num)

##----------------display the calender----------------------
# import calendar, datetime
# def display_calendar():
#     today = datetime.date.today()
#     year = today.year
#     month = today.month

#     print(f"Here is the calendar for {calendar.month_name[month]} {year}:")
#     print(calendar.month(year, month))

# display_calendar()

##------------python program suffle Deck of Cards----------------
# import itertools, random
# deck = list(itertools.product(range(1,14), ['spade', 'heart', 'diamond', 'club']))
# random.shuffle(deck)

# print("you got: ")
# for i in range(5):
#     print(deck[i][0], 'of', deck[i][1])


##---------------add two Matrix---------------
# X = [[12,7,3],
#     [4 ,5,6],
#     [7 ,8,9]]

# Y = [[5,8,1],
#     [6,7,3],
#     [4,5,9]]

# result = [[0,0,0],
#          [0,0,0],
#          [0,0,0]]

# for i in range(len(X)):
#     for j in range(len(X[0])):
#         result[i][j] = X[i][j] + Y[i][j]

# for r in result:
#     print(r)

##------------------Program to transpose a matrix using a nested loop--------------------------
# X = [[12,7],
#     [4 ,5],
#     [3 ,8]]

# result = [[0,0,0],
#          [0,0,0]]

# # iterate through rows
# for i in range(len(X)):
#    # iterate through columns
#    for j in range(len(X[0])):
#        result[j][i] = X[i][j]

# for r in result:
#    print(r)



##-------------------Program to multiply two matrices using nested loops-----------------------

# # 3x3 matrix
# X = [[12,7,3],
#     [4 ,5,6],
#     [7 ,8,9]]
# # 3x4 matrix
# Y = [[5,8,1,2],
#     [6,7,3,0],
#     [4,5,9,1]]
# # result is 3x4
# result = [[0,0,0,0],
#          [0,0,0,0],
#          [0,0,0,0]]

# # iterate through rows of X
# for i in range(len(X)):
#    # iterate through columns of Y
#    for j in range(len(Y[0])):
#        # iterate through rows of Y
#        for k in range(len(Y)):
#            result[i][j] += X[i][k] * Y[k][j]

# for r in result:
#    print(r)

##-----------Palindrome or Not---------------
# def palindrome(s):
#     return s == s[::-1]
# word = input("enter the string: ")
# if palindrome(word):
#     print(word,"is a palindrome")
# else:
#     print(word,"is not a palindrome")


##-----------Remove Punctuations from a string------------------

# punctuations = '''!()-[]{};"' \,<>./!@#$%^&*_~'''
# my_str = "Hello!!! , he said --- and went."
# no_punct = ""
# for char in my_str:
#     if char not in punctuations:
#         no_punct = no_punct + char
# print(no_punct)



##-------------sort words in alphabet order---------------
# def sort_word(sentence):
#     words = sentence.split()
#     words.sort()
#     return ' ' .join(words)

# # test the function
# sentence = "hello Gaurav this is python programming"
# print(sort_word(sentence))



##---------------------count the number of each vowels---------------------------

# def count_vowels(text):
#     # Dictionary to store the count of each vowel
#     vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
#     # Convert the text to lowercase to handle both upper and lower case letters
#     text = text.lower()
    
#     # Loop through the characters in the text
#     for char in text:
#         if char in vowels:
#             vowels[char] += 1
    
#     return vowels


# text = input("Enter a string: ")
# vowel_count = count_vowels(text)

# # Display the count of each vowel
# print("Vowel count in the given text:")
# for vowel, count in vowel_count.items():
#     print(f"{vowel}: {count}")

