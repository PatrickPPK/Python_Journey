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
#         programming

################################################################################################
# B4: Why was the language called as Python?
################################################################################################
# Answer: Language name 'Python' is named after the BBC show "Monty Python's Flying Circus"

################################################################################################
# B5: Write a Python program to check if a number is positive, negative or zero.
################################################################################################
number = int(input("Enter an integer number: "))
if number > 0:
    print(f"{number} is positive")
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
#          constructs to perform the similar operation

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
print(f"{number}! = {factorial(number)}")

################################################################################################
# B11: Write a Python program to get the Fibonacci series of given range
################################################################################################
number = int(input("Enter an integer number to find the Fibonacci series of the range within: "))
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
base = float(input("Enter the base dimension of a triangle: "))
height = float(input("Enter the height dimension of a triangle: "))
area = (base * height) / 2
print(f"The area of a triangle with {base} and {height} dimensions is {area} square unit")

#2) Area of a circle
from math import pi
radius = float(input("Enter the radius of a circle: "))
area = pi * radius * radius
print(f"The area of a circle with {radius} is {area} square unit")

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
P = float(input("Enter the principal amount: "))
R = float(input("Enter the rate of interest: "))
N = float(input("Enter the number of years: "))
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
# Answer: A decorator is a function that takes another function and extends the behavior of the
#         latter function without explicitly modifying it.

################################################################################################
# I8: What is PEP 8?
################################################################################################
# Answer: PEP 8 defines set of rules to format Python code to maximize its readability

################################################################################################
# ----------------------------------------------------------------------------------------------
# Assignment Level Advance
# ----------------------------------------------------------------------------------------------
################################################################################################

################################################################################################
# A1: Write a Python program to sort three integers without using conditional statements and
#     loops.
################################################################################################
int_1 = int(input("Enter the integer 1: "))
int_2 = int(input("Enter the integer 2: "))
int_3 = int(input("Enter the integer 3: "))
max_int = max(int_1, int_2, int_3)
min_int = min(int_1, int_2, int_3)
middle_int = sum((int_1, int_2, int_3)) - max_int - min_int
print("Sorted integers: {}, {}, {}".format(min_int, middle_int, max_int))

################################################################################################
# A2: Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
################################################################################################
n = input("Enter an integer: ")
nnn = int(n + n + n)
nn = int(n + n)
n = int(n)
value = n + nn + nnn
print(f"{n} + {nn} + {nnn} = {value}")

################################################################################################
# A3: Write a Python program to sum of three given integers. However, if two values are equal
#     sum will be zero.
################################################################################################
int_1 = int(input("Enter the integer 1: "))
int_2 = int(input("Enter the integer 2: "))
int_3 = int(input("Enter the integer 3: "))
if (int_1 == int_2) or (int_1 == int_3) or (int_2 == int_3):
    print(f"There are at least two values equal in ({int_1},{int_2},{int_3}). Hence setting sum "
          f"to 0")
    sum = 0
else:
    sum = int_1 + int_2 + int_3
print("{0} + {1} + {2} = {3}".format(int_1, int_2, int_3, sum))

################################################################################################
# A4: Write a Python program that will return true if the two given integer values are equal or
#     their sum or difference is 5.
################################################################################################
int_1 = int(input("Enter the integer 1: "))
int_2 = int(input("Enter the integer 2: "))
if (int_1 == int_2) or ((int_1 + int_2) == 5) or ((int_1 - int_2) == 5) or ((int_2 - int_1) == 5):
    print("True")
    
################################################################################################
# A5: Write a python program to sum of the first n positive integers
################################################################################################
integer = int(input("Enter an integer: "))
sum = 0
for n in range(integer+1):
    sum += n
print("sum of the first %d positive integers is %d" %(integer, sum))

################################################################################################
# ----------------------------------------------------------------------------------------------
# Topic: String manipulation
# Accessing String,Basic Operation,String slice,Function and method
# Assignment Level Basic
# ----------------------------------------------------------------------------------------------
################################################################################################

################################################################################################
# B1: Write a Python program to calculate the length of a string.
################################################################################################
string = input("Enter a string: ")
print(f"Length of the string '{string}' is {len(string)}")

################################################################################################
# B2: Write a Python program to count the number of characters (character frequency) in a string
################################################################################################
string = input("Enter a string: ")
unique_characters = set()
for c in string:
    unique_characters.add(c)
for n in unique_characters:
    print(f"character frequency of '{n}' in '{string}' is: {string.count(n)}")
    
################################################################################################
# B3: What are negative indexes and why are they used?
################################################################################################
# Answer: In python, negative indexes are used to index any indexable data type from the end of
#         collection. Negative indexes are believed to be more readable.

################################################################################################
# B4: Explain split(), sub(), subn() methods of “re” module in Python.
################################################################################################
# Answer: Not covered in module-1

################################################################################################
# B5: How do you perform pattern matching in Python? Explain.
################################################################################################
# Answer: In Python, pattern matching or string parsing is handled by regular expressions. The
#         "re" module comes with python installation provides regular expression supports.

################################################################################################
# B6: Write a Python program to count occurrences of a substring in a string
################################################################################################
string = input("Enter a string: ")
substring = input("Enter a substring: ")
print(f"Occurrences of the '{substring}' in a string '{string}' is: {string.count(substring)}")

################################################################################################
# B7: Write a Python program to count the occurrences of each word in a given sentence
################################################################################################
string = input("Enter a string: ")
unique_words = set(string.split(' '))
for word in unique_words:
    print(f"Occurrences of the '{word}' in a string '{string}' is: {string.count(word)}")

################################################################################################
# ----------------------------------------------------------------------------------------------
# Assignment Level Intermediate
# ----------------------------------------------------------------------------------------------
################################################################################################

################################################################################################
# I1: Write a Python program to get a single string from two given strings, separated by a space
#     and swap the first two characters of each string.
################################################################################################
string_1, string_2 = input("Enter two strings separated by comma(,): ").split(',')
updated_string = string_2[:2] + string_1[2:] + ' ' + string_1[:2] + string_2[2:]
print("A single string from two given string, after swapping the first two characters of each "
      "string is : '%s'" %(updated_string))
      
################################################################################################
# I2: Write a Python program to add 'ing' at the end of a given string (length should be at
#     least 3). If the given string already ends with 'ing' then add 'ly' instead If the string
#     length of the given string is less than 3, leave it unchanged
################################################################################################
string = input("Enter a string: ")
if len(string) < 3:
    print("Length of the string is less than 3, hence not changing the string")
    updated_string = string
elif string[-3:] == 'ing':
    print("String ends with 'ing', hence appending 'ly' at the end")
    updated_string = string + 'ly'
else:
    print("Appending 'ing' at the end")
    updated_string = string + 'ing'
print(f"Updated string: '{updated_string}'")

################################################################################################
# I3: Write a Python program to find the first appearance of the substring 'not' and 'poor' from
#     a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring
#     with 'good'. Return the resulting string.
################################################################################################
string = input("Enter a string: ")
index_of_not_word = string.find('not')
index_of_poor_word = string.find('poor')
if index_of_not_word < index_of_poor_word and index_of_not_word > 0 and index_of_poor_word > 0:
    print("'not' word follows the 'poor' word in the string, hence replacing 'not'...'poor' "
          "substring with 'good'")
    updated_string = string[:index_of_not_word] + 'good' + string[(index_of_poor_word+4):]
else:
    updated_string = string
print(f"Updated string: '{updated_string}'")

################################################################################################
# I4: Write a Python function that takes a list of words and returns the length of the longest
#     one.
################################################################################################
words = input("Enter the list of words separated by comma(,): ").split(',')
length_of_longest_word = 0
for n in words:
    if len(n) > length_of_longest_word:
        length_of_longest_word = len(n)
print(f"The length of the longest word is: {length_of_longest_word}")

################################################################################################
# I5: Write a Python function to reverses a string if it's length is a multiple of 4
################################################################################################
string = input("Enter a string: ")
if ((len(string) % 4) == 0):
    print("length of the string is multiple of 4, hence reversing the string")
    updated_string = string[::-1]
else:
    updated_string = string
print(f"Updated string: '{updated_string}'")

################################################################################################
# ----------------------------------------------------------------------------------------------
# Assignment Level Advance
# ----------------------------------------------------------------------------------------------
################################################################################################

################################################################################################
# I1: Write a Python program to get a string made of the first 2 and the last 2 chars from a
#     given a string. If the string length is less than 2, return instead of the empty string.
#     Go to the editor
#     Sample String : 'w3resource'
#     Expected Result : 'w3ce'
#     Sample String : 'w3'
#     Expected Result : 'w3w3'
#     Sample String : ' w'
#     Expected Result : Empty String
################################################################################################
string = input("Enter a string: ")
if len(string) < 2:
    updated_string = ''
else:
    updated_string = string[:2] + string[-2:]
print(f"Updated string: '{updated_string}'")

################################################################################################
# I2: Write a Python program to get a string from a given string where all occurrences of its
#     first char have been changed to '$', except the first char itself
################################################################################################
string = input("Enter a string: ")
first_char = string[0]
updated_string = first_char + string[1:].replace(first_char, '$')
print(f"Updated string: '{updated_string}'")

################################################################################################
# I3: Write a Python function to insert a string in the middle of a string.
################################################################################################
string_1 = input("Enter a string: ")
string_2 = input(f"Enter a string to put in the middle of a string '{string_1}': ")
updated_string = string_1[:(len(string_1)//2)] + string_2 + string_1[(len(string_1)//2):]
print(f"Updated string: '{updated_string}'")
