# ################################################################################################
# # ----------------------------------------------------------------------------------------------
# # Module 3 [functions]
# # Topic : Function and method
# # Assignment Level Basic
# # ----------------------------------------------------------------------------------------------
# ################################################################################################
#
# ################################################################################################
# # B1: Write a Python function to calculate the factorial of a number (a non-negative integer)
# ################################################################################################
# number = int(input("Enter an integer number to find the factorial: "))
# def factorial(n):
#     if n <= 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(f"{number}! = {factorial(number)}")
#
# ################################################################################################
# # B2: Write a Python function to check whether a number is in a given range
# ################################################################################################
# number = int(input("Enter an integer number to check if it is between 0 and 100 inclusive: "))
# def check_in_rage(n):
#     if n in range(0,101):
#         print(f"The number '{number}' is in a range of [0:100]")
#         return True
#     else:
#         print(f"The number '{number}' is not in a range of [0:100]")
#         return False
# check_in_rage(number)
#
# ################################################################################################
# # B3: Write a Python function to check whether a number is perfect or not.
# ################################################################################################
# def check_if_perfect_number(n):
#     divisors = []
#     for i in range(1,(n//2+1)):
#         if n % i == 0:
#             divisors.append(i)
#     if sum(divisors) == n:
#         return True
#     return False
# for n in range(0,100)
#     if check_if_perfect_number(n) is True:
#         print(f"Number {n} is a perfect number")
#     else:
#         print(f"Number {n} is not a perfect number")
#
# ################################################################################################
# # B4: Write a Python function that checks whether a passed string is palindrome or not
# ################################################################################################
# def check_if_palindrome_string(s):
#     reverse_str = s[::-1]
#     if s[:(len(s)//2)] == reverse_str[:(len(reverse_str)//2)]:
#         return True
#     return False
# list_of_words = ['radar','banana','anna','jackfruit','orange','mom','11011']
# for word in list_of_words:
#     if check_if_palindrome_string(word) is True:
#         print(f"'{word}' is a palindrome string")
#     else:
#         print(f"'{word}' is not a palindrome string")
#
# ################################################################################################
# # B5: How do you perform pattern matching in Python? Explain
# ################################################################################################
# Not covered yet
#
# ################################################################################################
# # B6: What is lambda function in python? What we call a function which is incomplete version of
#       a function?
# ################################################################################################
# Answer: Lambda function is a anonymous function single line function which can have only one
#          expression. Incomplete version of a function is called a Stub.
#
# ################################################################################################
# # B7: How Many Basic Types Of Functions Are Available In Python?
# ################################################################################################
# Answer: There are two types of functions in Python. Built-in functions and user defined
#         functions
#
# ################################################################################################
# # ----------------------------------------------------------------------------------------------
# # Assignment Level Intermediate
# # ----------------------------------------------------------------------------------------------
# ################################################################################################
#
# ################################################################################################
# # I1: Write a Python program to access a function inside a function.
# ################################################################################################
# def greetings():
#     print('I love ',end='')
#     def programming_language(p):
#         print(f'{p} programming language.')
#     return programming_language
# f = greetings()
# f('Python')
#
# ################################################################################################
# # I2: Write a Python program to detect the number of local variables declared in a function.
# ################################################################################################
# def greetings(person):
#     print(f"Hello, {person}")
# print(f"the number of local variables declared in a function is {greetings.__code__.co_nlocals}")
#
# ################################################################################################
# # I3: What is map function in Python?
# ################################################################################################
# Answer: Map function is used to apply specified function(in the argument list of map function)
#         on all the elements of the iterable. The map(which is iterator) object can be converted
#         back to list, tuple, etc.
#
# ################################################################################################
# # I4: Does Python Have A Main() Method?
# ################################################################################################
# Answer: Python doesn't have a main() method like C language.

# ################################################################################################
# # I5: What Does The *Args Do In Python? What Does The **Kwargs Do In Python?
# ################################################################################################
# Answer: The *args is used in the function argument list to pass variable number of non-keyword
#         arguments, whereas the **args is used in the function argument list to pass variable
#         number of keyword arguments.
#
# ################################################################################################
# # I6: What Does The __name__ Do In Python? What Is The Purpose Of “End” In Python?
# ################################################################################################
# Answer: The __name__variable defines whether the script is being run as the main module or it is
#         being run as an imported module.
#         end argument is used in print function to specify the custom ending character, by
#         default it is set to new line(\n) character.
#
# ################################################################################################
# # I7: What Does The Len() Function Do In Python? What Does The Ord() Function Do In Python?
# ################################################################################################
# Answer: len() function returns the length of the iterable passed as an argument to it.
#         ord() function returns unicode point representation of the passed single length
#         character string as an argument.
#
# ################################################################################################
# # ----------------------------------------------------------------------------------------------
# # Assignment Level Advance
# # ----------------------------------------------------------------------------------------------
# ################################################################################################
#
# ################################################################################################
# # A1: Name few methods that are used to implement Functionally Oriented Programming in Python?
# ################################################################################################
# Answer: filter(), map() and reduce() are some of the examples of functionally oriented
#         programming in Python.
#
# ################################################################################################
# # A1: Write a program in Python to reverse a string without using inbuilt function reverse
# #     string?
# ################################################################################################
# string = input("Please enter a string: ")
# print(f"Reverse of a string '{string}' is: '{string[::-1]}'")