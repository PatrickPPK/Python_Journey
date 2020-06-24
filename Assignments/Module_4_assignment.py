################################################################################################
# ----------------------------------------------------------------------------------------------
# Module 4 [Modules]
# Topic: Module
# Importing module, math module, random module, packages
# Assignment Level Basic
# ----------------------------------------------------------------------------------------------
################################################################################################

################################################################################################
# B1: How can you pick a random item from a list or tuple?
################################################################################################
# from random import choice
# l = [1,10,20,30,40,49]
# print(f"Randomly chosen element from list {l} is: {choice(l)}")
#
################################################################################################
# B2: How can you pick a random item from a range?
################################################################################################
# from random import randrange
# print(f"Randomly chosen item from a range [0:100) is: {randrange(0,100)}")
#
################################################################################################
# B3: How can you get a random number in python?
################################################################################################
# from random import randint
# print(f"Random number: {randint(0,1000000)}")
#
################################################################################################
# B4: How will you set the starting value in generating random numbers?
################################################################################################
# Answer: In Python, in random module, seed() method sets the integer starting value used in
#         generating random numbers.
#
################################################################################################
# B5: How will you randomizes the items of a list in place?
################################################################################################
# Answer: In Python, in random module, shuffle() method shuffles the list in place and
#         randomizes the order of the items in the original list.
#
################################################################################################
# ----------------------------------------------------------------------------------------------
# Assignment Level Intermediate
# ----------------------------------------------------------------------------------------------
################################################################################################

################################################################################################
# I1: Write a Python program to read a random line from a file.
################################################################################################
# from random import choice
# l = []
# with open('test.txt','r') as f:
#     l = f.readlines()
# print(f"Random line read from the file 'test.txt': {choice(l)}")
#
################################################################################################
# I2: Write a Python program to convert degree to radian
################################################################################################
# import numpy
# while True:
#     try:
#         degree = float(input("Please enter angle in degrees: "))
#         break
#     except ValueError:
#         print(f"Numbers in integer or floating point formats only. Please try again!")
# print(f"{degree}° = {round(numpy.deg2rad(degree),4)} Rad")
#
################################################################################################
# I3: Write a Python program to calculate the area of a trapezoid
################################################################################################
# def calc_area(b1,b2,h):
#     return (((b1 + b2) * h) / 2)
# base_1 = float(input("Enter one of the base dimension of a trapezoid: "))
# base_2 = float(input("Enter another base dimension of a trapezoid: "))
# height = float(input("Enter height of a trapezoid: "))
# print(f"Area of the trapezoid with base lengths and height dimensions respectively {base_1}, "
#       f"{base_2} and {height} is: {round(calc_area(base_1,base_2,height),2)} square unit")
#
################################################################################################
# I4: Write a Python program to calculate the area of a parallelogram
################################################################################################
# def calc_area(b,h):
#     return (b * h)
# base = float(input("Enter base dimension of a parallelogram: "))
# height = float(input("Enter height of a parallelogram: "))
# print(f"Area of the parallelogram with base and height dimensions respectively {base}, "
#       f"and {height} is: {round(calc_area(base,height),2)} square unit")
#
################################################################################################
# I5: Write a Python program to calculate surface volume and area of a cylinder
################################################################################################
# from math import pi
# def calc_surface_area(r,h):
#     return (2 * pi * r) * (r + h)
# def calc_volume(r,h):
#     return (pi * r * r * h)
# radius = float(input("Enter radius of the base dimension of a cylinder: "))
# height = float(input("Enter height of a cylinder: "))
# print(f"Area of a cylinder with radius and height dimensions respectively {radius}, and "
#       f"{height} is: {round(calc_surface_area(radius,height),2)} square unit")
# print(f"Volume of a cylinder with radius and height dimensions respectively {radius}, and "
#       f"{height} is: {round(calc_volume(radius,height),2)} cubic unit")
#
################################################################################################
# I6: Write a Python program to returns sum of all divisors of a number
################################################################################################
# def calc_sum_of_divisors(n):
#     divisors = [1]
#     for i in range(2,(n//2+1)):
#         if n % i == 0:
#             divisors.append(i)
#     divisors.append(n)
#     return sum(divisors)
# for n in range(0,100):
#     print(f"The sum of all divisors of a number '{n}' is: {calc_sum_of_divisors(n)}")

################################################################################################
# I7: Write a Python program to find the maximum and minimum numbers from the specified decimal
#     numbers.
################################################################################################
# from decimal import Decimal
# from random import randrange
# decimal_list = [Decimal(randrange(0,100)) for n in range(10)]
# print(f"Maximum and minimum numbers from the list of decimal numbers {decimal_list} are "
#       f"respectively: {max(decimal_list)} and {min(decimal_list)}")

################################################################################################
# ----------------------------------------------------------------------------------------------
# Assignment Level Advance
# ----------------------------------------------------------------------------------------------
################################################################################################

################################################################################################
# A1: Write a Python program to find the sum of the following decimal numbers and display the
#     numbers in sorted order
#     Decimal numbers : 2.45, 2.69, 2.45, 3.45, 2.00, 0.04, 7.25
#     Expected Output : Sum: 20.33
#     Sorted order: [Decimal('0.04'), Decimal('2.00'), Decimal('2.45'), Decimal('2.45'),
#                    Decimal('2.69'), Decimal('3.45'), Decimal('7.25')]
################################################################################################
# from decimal import Decimal
# decimal_list = [Decimal('2.45'), Decimal('2.69'), Decimal('2.45'), Decimal('3.45'),
#                 Decimal('2.0'), Decimal('0.04'), Decimal('7.25')]
# print(f"Expected Output : {sum(decimal_list)}")
# print(f"Sorted order : {sorted(decimal_list)}")
#
################################################################################################
# A2: Write a Python program to get the square root and exponential of a given decimal number
################################################################################################
# from decimal import Decimal, getcontext
# getcontext().prec = 5
# decimal_number = Decimal(input("Enter a decimal number: "))
# print(f"Square root of a number '{decimal_number}' is: {decimal_number.sqrt()}")
# print(f"Exponential of a number '{decimal_number}' is: {decimal_number.exp()}")
#
################################################################################################
# A3: Write a Python program to add, subtract, multiply and divide two fractions.
#     Expected Output :
#     2/3 + 3/7 = 23/21
#     2/3 - 3/7 = 5/21
#     2/3 * 3/7 = 2/7
#     2/3 / 3/7 = 14/9
################################################################################################
# from fractions import Fraction
# frac_1 = Fraction('2/3')
# frac_2 = Fraction('3/7')
# add = frac_1 + frac_2
# sub = frac_1 - frac_2
# mul = frac_1 * frac_2
# div = frac_1 / frac_2
# print(f'{frac_1} + {frac_2} =',add)
# print(f'{frac_1} - {frac_2} =',sub)
# print(f'{frac_1} * {frac_2} =',mul)
# print(f'{frac_1} / {frac_2} =',div)

