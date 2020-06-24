################################################################################################
# ----------------------------------------------------------------------------------------------
# Module 6 [Excption Handling]
# Topic: Exception Handling Exception, Except clause, ry and finally
# Assignment Level Basic
# ----------------------------------------------------------------------------------------------
################################################################################################

################################################################################################
# B1: Explain Exception handling? What is an Error in Python?
################################################################################################
# Answer: An exception is an event, which occurs during the execution of a program that disrupts
#         the normal flow of the program's instructions.
#         An Error in Python is an event when a certain statement is not in accordance with the
#         appropriate usage.
#
################################################################################################
# B2: How many except statements can a try-except block have? Name Some built-in exception
#     classes:
################################################################################################
# Answer: A try-except block can have as many except statements as you can write.
#         Exception, SyntaxError, ValueError, IndexError, ZeroDivisionError, etc..
#
################################################################################################
# B3: When will the else part of try-except-else be executed?
################################################################################################
# Answer: The else part of try-except-else clause will be executed when there are no exceptions
#         raised while executing try clause.
#
################################################################################################
# B4: Can one block of except statements handle multiple exception?
################################################################################################
# Answer: Yes, of course. Try below code snippet to handle multiple exception in one except
#         clause.
#         try:
#               ...
#         except (ValueError, TypeError, NameError):
#               ...
#
################################################################################################
# B5: When is the finally block executed?
################################################################################################
# Answer: Every single time, no matter exceptions are raised or not
#
################################################################################################
# B6: What happens when "1" == 1 is executed?
################################################################################################
# Answer: We get 'False' as an answer
#
################################################################################################
# B7: How Do You Handle Exceptions With Try/Except/Finally In Python? Explain with coding
#     snippets.
################################################################################################
# Answer: Put the statement(s) which might raise exception(s) in try clause,
#         Put the statement(s) handling exception(s) in except clause
#         Use finally clause to free up shared or crucial resources
#         try:
#               <Statement(s) which might raise an exception(s)>
#         except (ExceptionClass or ExceptionObject):
#               <Handle the raised exception>
#         finally:
#               Free up shared or crucial resource
#
################################################################################################
# B8: Write python program that user to enter only odd numbers, else will raise an exception.
################################################################################################
# while True:
#     try:
#         odd_number = int(input("Enter an odd number: "))
#         if (odd_number % 2) == 0:
#             raise ValueError
#     except ValueError:
#         print("Only odd numbers, you Stupid! Try again...")
#     else:
#         print("Thanks for entering an odd number. Bye now. Hope to see you next time..")
#         break
#
################################################################################################
# ----------------------------------------------------------------------------------------------
# Assignment Level Intermediate
# ----------------------------------------------------------------------------------------------
################################################################################################

################################################################################################
# I1: Write program for Catching Specific Exceptions in Python
################################################################################################
# try:
#     raise NameError("This exception is raised when python program tries to access the "
#                     "variable before defining it..")
# except NameError:
#     print("I'm a NameError exception handler. Go figure..")
#     raise
#
################################################################################################
# I2: Write python program for file operations to makes sure the file is closed even if an
#     exception occurs.
################################################################################################
# f = None
# try:
#     f = open('unknown_file.txt','r')
# except FileNotFoundError:
#     print("Can't find file or directory with name 'unknown_file.txt'")
# finally:
#     if f is not None:
#         f.close()
#         print("Closing the file 'unknown_file.txt'")
#
################################################################################################
# I3: Explain Python Errors and Built-in Exceptions with coding snippets
################################################################################################
# Answer: Python Errors are reported when a certain statement is not in accordance with the
#         appropriate usage. e.g. Syntax Error or Parsing Error
#         Python language defines different exception classes, which are called built-in
#         exceptions
# Error example:
# for a in 10
#     a += 1
# SyntaxError
# # built-in exception example
# l = [1,2,3,4]
# for i in range(10):
#     print(l[i])
# IndexError: list index out of range
################################################################################################
# ----------------------------------------------------------------------------------------------
# Assignment Level Advance
# ----------------------------------------------------------------------------------------------
################################################################################################

################################################################################################
# A1: Explain User-Defined Exception in Python
################################################################################################
# class OddNumberException(ArithmeticError):
#     """Raised when an odd number is supplied where even number is expected."""
#
# while True:
#     try:
#         even_number = int(input("Enter an even number: "))
#         if even_number % 2 != 0:
#             raise OddNumberException
#     except OddNumberException:
#         print("OddNumberException occurred: Only even numbers, you Stupid! Try again...")
#     else:
#         print("Thanks for entering an even number. Bye now. Hope to see you next time..")
#         break
#
################################################################################################
# A2: Write a program that will ask the user to enter a number until they guess a stored number
#       correctly
################################################################################################
# import random
# number = random.randrange(0,101)
# number_of_guesses = 0
# while True:
#     guess_number = int(input("Guess a number between 0 and 100: "))
#     if guess_number < number:
#         print("Naah.... You entered small number, guess bigger number..")
#     elif guess_number > number:
#         print("Naah.... You entered big number, guess smaller number..")
#     else:
#         print("Bingo.. You guessed it right.")
#         break
#     number_of_guesses += 1
# print(f"The right answer is {number}")
# print(f"You took {number_of_guesses} attempts to guess the right answer.")
#
################################################################################################
# A3: What is Assertions in Python? Write function that converts a temperature from degrees
#     Kelvin to degrees Fahrenheit
################################################################################################
# Answer: Assert keyword is used for debugging purpose. Using assert keyword, you can test
#         a condition to be True, and if it's not True, AssertionError exception is raised
#
################################################################################################
# A4: Write program that except Clause with No Exceptions
# ################################################################################################
# try:
#     raise Exception
# except:
#     print("I'm an except clause with no exception. I catch all the exceptions raised while"
#           "executing try clause")
# finally:
#     print('Bye Bye.. Have a good one!')
#
################################################################################################
# A5: What is Argument of an Exception? Explain with coding snippets
################################################################################################
# Answer: Except clause accepts exception class or exception class instance as an argument.

# Example 1: Except clause with exception class as an argument
# try:
#     ...
# except ArithmeticError:
#     print("I'm in exception clause - with ArithmeticError exception class as an argument")

# # Example 2: Except clause with exception class instance as an argument
# class MyException(ArithmeticError):
#     """This is my exception class"""
# MyException_h = MyException()
# try:
#     ...
# except MyException_h:
#     print("I'm in exception clause - with MyException_h instance as an argument")

# # Example 3: Except clause with multiple exception classes as an argument
# try:
#     ...
# except (IndexError, NameError, ValueError):
#     print("I'm in exception clause - with (IndexError, NameError, ValueError) as an argument")

# # Example 4: Except clause with no arguments
# try:
#     ...
# except:
#     print("I'm in exception clause - with no arguments")