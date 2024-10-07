import math
#define operation logics
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def square(x,y):
    return x**y

def square_root(x,y):
    return x**(1/y)

# percentage
def percentage(x,y):
    return (x*y)/100

# log base 10
def log_base_10(x):
    return math.log10(x)

# log base e
def log_e(x):
    return math.log(x)

# exponential function
def exponential(x):
    return math.exp(x)


# sin
def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)



# main program
calculator_art = r"""
        _____________________
       |  _________________  |
       | |               0 | |
       | |_________________| |
       |  ___ ___ ___   ___  |
       | | 7 | 8 | 9 | | + | |
       | |___|___|___| |___| |
       | | 4 | 5 | 6 | | - | |
       | |___|___|___| |___| |
       | | 1 | 2 | 3 | | x | |
       | |___|___|___| |___| |
       | | . | 0 | = | | / | |
       | |___|___|___| |___| |
       |_____________________|
"""
print(calculator_art)
print("*****************************************************")
print("*                                                   *")
print("💖🌟 Welcome to Your Friendly Calculator 🌟💖")
print("✨ We're so excited to help you with your calculations today! ✨")
print("😊 Let's make math fun and easy together! 😊")
print("*                                                   *")
print("*****************************************************\n")

# Your calculator options
print("""
1. Add ➕       2. Subtract ➖          3. Multiply ✖️       4. Divide ➗
5. Square ⬛    6. Square Root√         7. Percentage %       8. Log Base 10 (log₁₀)
9. Log e (ln)   10. Exponential (eˣ)    11. Sin (sinθ)        12. Cos (cosθ) 
13. Tan (tanθ)
""")





while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4/5/6.............): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4','5','6','7','8','9','10','11','12','13'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(add(num1, num2))

        elif choice == '2':
            print(subtract(num1, num2))

        elif choice == '3':
            print(multiply(num1, num2))

        elif choice == '4':
            print(divide(num1, num2))

        elif choice == '5':
            print(square(num1, num2))
        
        elif choice == '6':
            print(square_root(num1, num2))
        
        elif choice == '7':
            print(percentage(num1, num2))
        
        elif choice == '8':
            print(log_base_10(num1))
        
        elif choice == '9':
            print(log_e(num1))
        
        elif choice == '10':
            print(exponential(num1))
        
        elif choice == '11':
            print(sin(num1))
        
        elif choice == '12':
            print(cos(num1))
        
        elif choice == '13':
            print(tan(num1))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            print('I hope you enjoyed🎉 this program 🧑‍💻... Have a good ⌛ with you ❤️')
            break
    else:
        print("Invalid Input")