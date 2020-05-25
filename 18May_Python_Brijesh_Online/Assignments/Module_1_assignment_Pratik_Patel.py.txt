################################################################################################
# ----------------------------------------------------------------------------------------------
# Module 1 Assignment
# Topic: Core Python concepts Introduction of python,If, If- else, Nested if-else,while,for-loop
# Assignment Level Basic
# ----------------------------------------------------------------------------------------------
################################################################################################

################################################################################################
# B1: What is Python. Name some of the features of Python.
################################################################################################
# Answer:
# Python is a high level, object oriented and interpreted programming language.
# Features: Easy to learn, efficient high level data structures, object oriented,
#           open source(free), cross platform compatible(windows,linux,macos,etc..),
#           large set of libraries

################################################################################################
# B2: Write a Python program to get the Python version you are using?
################################################################################################
import sys
print(sys.version)

################################################################################################
# B3: Is python the right choice for Web based Programming?
################################################################################################
# Answer: Web frameworks like Django, Flash make python one of the best choice for web based
# programming

################################################################################################
# B4: Why was the language called as Python?
################################################################################################
# Answer: Language name 'Python' is named after the BBC show "Monty Python's Flying Circus"

################################################################################################
# B5: Write a Python program to check if a number is positive, negative or zero.
################################################################################################
number = int(input("Enter an integer number: "))
if number > 0:
    print(f"{number} is position")
elif number < 0:
    print("{0} is negative" .format(number))
else:
    print("%d is zero" %(number))
################################################################################################
# B6: What is the language from which Python has got its features or derived its features?
################################################################################################
# Answer: Python language got or derived its features from C and Java language.

################################################################################################
# B7: Write a Python program to check if variable is of integer or string.
################################################################################################
variable = "Python"
# variable = 10
if isinstance(variable, str) is True:
    print(f"{variable} is of type 'str'")
elif isinstance(variable, int) is True:
    print(f"{variable} is of type 'int'")

################################################################################################
# B8: Does python support switch or case statement in Python? If not what is the reason for
#     the same?
################################################################################################
# Answer : Python doesn't support switch or case statement. Python has if, elif, else
#          constructs to perform the same operation

################################################################################################
# B9: How Python is interpreted?
################################################################################################
# Answer: In Python, the source code is first converted into bytecode (which creates a file with
#         extension .pyc) and then they are executed by the software called a virtual machine.

################################################################################################
# B10: Write a Python program to get the Factorial number of given number
################################################################################################
number = int(input("Enter an integer number to find the factorial: "))
def factorial(n):
    if n <= 0:
        return 1
    else:
        return n * factorial(n-1)
factorial(number)
################################################################################################
# B11: Write a Python program to get the Fibonacci series of given range
################################################################################################
number = int(input("Enter an integer number to find the factorial: "))
def fibonacci(n):
    a = 0
    b = 1
    while b <= n:
        b, a = a+b, b
        print(a, end=' ')
fibonacci(number)
################################################################################################
# B12: How memory is managed in Python?
################################################################################################
# Answer: Everything in Python is an object. Memory allocator allocates the space in the memory
#         for the all kinds of data and when objects are no longer needed, the python memory
#         management (garbage collector) will automatically reclaim memory from them.

################################################################################################
# B13: What is namespace in Python?
################################################################################################
# Answer: A namespace is a system to have a unique name for each and every object in Python.

################################################################################################
# B14: What is the purpose of continue statement in python?
################################################################################################
# Answer: The continue statement skips the remaining loop block and continues with the next
#         cycle of the nearest enclosing loop.

################################################################################################
# ----------------------------------------------------------------------------------------------
# Assignment Level Intermediate
# ----------------------------------------------------------------------------------------------
################################################################################################

################################################################################################
# I1: Write python program that swap two number with temp variable and without temp variable
################################################################################################
# With temp variable
a = 10
b = 20
temp = a
a = b
b = temp

# Without temp variable
a = 10
b = 20
a, b = b, a
################################################################################################
# I2: Write a Python program to find whether a given number is even or odd, print out an
#     appropriate message to the user.
################################################################################################
number = int(input("Enter an integer number: "))
if (number % 2) == 0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")
################################################################################################
# I3: Write a Python program that compute the area of following
#     1) Triangle (accepts base and height)
#     2) Circle (accept radius)
################################################################################################
#1) Area of a triangle
base = int(input("Enter the base dimension of a triangle: "))
height = int(input("Enter the height dimension of a triangle: "))
area = (base * height) / 2
print(f"The area of a triangle with {base} and {height} dimensions is {area}")

#2) Area of a circle
from math import pi
radius = int(input("Enter the radius of a circle: "))
area = pi * radius * radius
print(f"The area of a circle with {radius} is {area}")
################################################################################################
# I4: Write a Python program to test whether a passed letter is a vowel or not
################################################################################################
letter = input("Enter an alphabet letter: ")
vowels = ['a','e','i','o','u']
if letter.casefold() in vowels:
    print(f"The alphabet letter '{letter}' is a vowel")
else:
    print(f"The alphabet letter '{letter}' is not a vowel")
################################################################################################
# I5: Write a Python program to compute the value of a specified principal amount, rate of
#     interest, and a number of years
################################################################################################
P = int(input("Enter the principal amount: "))
R = int(input("Enter the rate of interest: "))
N = int(input("Enter the number of years: "))
interest_after_n_years = P * R * N / 100
total_value_after_n_years = P + interest_after_n_years
print(f"The value of a principal amount '{P}' with rate of interest '{R}' after '{N} years is "
      f"'{total_value_after_n_years}'")
################################################################################################
# I6: What are the tools that help to find bugs or perform static analysis?
################################################################################################
# Answer: PyChecker, debugger, PyLint

################################################################################################
# I7: What are Python decorators?
################################################################################################

################################################################################################
# I8: What is PEP 8?
################################################################################################
# Answer: PEP 8 defines set of rules to format Python code to maximize its readability

