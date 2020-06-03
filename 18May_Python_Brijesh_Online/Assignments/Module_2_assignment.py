################################################################################################
# ----------------------------------------------------------------------------------------------
# Module 2 [Collections] Assignment
# Topic: List
# Introduction,Accessing List,OperationWorking with list,function and method
# Assignment Level Basic
# ----------------------------------------------------------------------------------------------
################################################################################################

################################################################################################
# B1: What is List? How will you reverse a list?
################################################################################################
# Answer: List is a collection of same or different data objections. Lists are ordered and
#         mutable in nature. Lists can have duplicate values.
#         list provides the reverse() method to reverse the contents of the itself.
################################################################################################
# B2: How will you remove last object from a list?
################################################################################################
# Answer: Using pop() method, or using del() method

################################################################################################
# B3: Suppose list1 is [2, 33, 222, 14, 25], What is list1[-1] ?
################################################################################################
# Answer: 25

################################################################################################
# B4: Differentiate between append() and extend() methods.?
################################################################################################
# Answer: Append() method adds single element at the end of the list whereas extend() method
#         adds iterable at the end of the list

################################################################################################
# B5: Write a Python function to get the largest number, smallest num and sum of all from a list
################################################################################################
lst = [x for x in range(5)]
print(f"Largest number in the list {lst} is: {max(lst)}")

################################################################################################
# B6: How will you compare two lists?
################################################################################################

################################################################################################
# ----------------------------------------------------------------------------------------------
# Assignment Level Intermediate
# ----------------------------------------------------------------------------------------------
################################################################################################

################################################################################################
# I1: Write a Python program to count the number of strings where the string length is 2 or more
#     and the first and last character are same from a given list of strings.
################################################################################################
lst = ['apple', 'orange', 'a', 'b', 'aaa', 'aba', 'ada', 'xyz', 'zzz']
match_count = 0
for item in lst:
    if (len(item) > 1) and (item[0] == item[-1]):
        match_count += 1
print(f"Number of the string elements in a list where the string length is 2 or more and the "
      f"first and last character are same is: {match_count}")

################################################################################################
# I2: Write a Python program to remove duplicates from a list
################################################################################################
lst = ['a' for n in range(10)]
print(f"List after removing duplicate items from {lst} is: {list(set(lst))}")

################################################################################################
# I3: Write a Python program to check a list is empty or not.
################################################################################################
lst = []
if len(lst) > 0:
    print(f"List {lst} is empty")
else:
    print(f"List {lst} is not empty")

################################################################################################
# I4: Write a Python function that takes two lists and returns True if they have at least one
#     common member
################################################################################################
def check_if_isdisjoin(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    if set1.isdisjoint(set2):
        print(f"Lists \"{list1}\" and \"{list2}\" do not have any common member")
    else:
        print(f"Lists \"{list1}\" and \"{list2}\" have at least one common member")
list1 = [1,2,3,4]
list2 = [4,5,6,7]
check_if_isdisjoin(list1, list2)

################################################################################################
# I5: Write a Python program to generate and print a list of first and last 5 elements where the
#     values are square of numbers between 1 and 30
################################################################################################
lst = [x**2 for x in range(31)]
print(f"First 5 elements: {lst[:5]} and last 5 elements: {lst[-5:]}")

################################################################################################
# I6: Write a Python function that takes a list and returns a new list with unique elements of the first list
################################################################################################
def get_unique_elements(lst):
    return(list(set(lst)))
lst = [10 for x in range(10)]
new_list = get_unique_elements(lst)
print(f"List \"{lst}\" after removing duplicate elements: \"{new_list}\"")

################################################################################################
# I7: Write a Python program to convert a list of characters into a string
################################################################################################
alphabet_list = ['a','e','i','o','u']
string = ''.join(alphabet_list)
print(f"Converting list \"{alphabet_list}\" to string: \"{string}\")

################################################################################################
# ----------------------------------------------------------------------------------------------
# Assignment Level Advance
# ----------------------------------------------------------------------------------------------
################################################################################################

################################################################################################
# A1: Write a Python program to select an item randomly from a list.
################################################################################################
import random
lst = ['a','e','i','o','u']
print(f"Randomly chosen element from list \"{lst}\" is \"{random.choice(lst)}\"")

################################################################################################
# A2: Write a Python program to find the second smallest number in a list.
################################################################################################
import random
lst = [n for n in range(10)]
random.shuffle(lst)
list_with_unique_integers = list(set(lst))
list_with_unique_integers.sort()
print(f"Second smaller number in a list \"{lst}\" is: \"{list_with_unique_integers[1]}\"")

################################################################################################
# A3: Write a Python program to get unique values from a list
################################################################################################
lst = [n%3 for n in range(10)]
list_with_unique_elements = list(set(lst))
print(f"Original list \"{lst}\" after keeping only unique values: "
      f"\"{list_with_unique_elements}\"")
################################################################################################
# A4: Write a Python program to check whether a list contains a sublist
################################################################################################
import random
list_1 = [random.randint(0,10) for n in range(random.randint(1,5))]
list_2 = [random.randint(0,10) for n in range(random.randint(1,10))]

if len(list_1) > len(list_2):
    if all(n in list_1 for n in list_2):
        print(f"list \"{list_1}\" contains list \"{list_2}\"")
    else:
        print(f"No list is subset of other list")
else:
    if all(n in list_2 for n in list_1):
        print(f"list \"{list_2}\" contains list \"{list_1}\"")
    else:
        print(f"No list is subset of other list")

################################################################################################
# A5: Write a Python program to split a list into different variables.
################################################################################################
lst = [n for n in range(5)]
a,b,c,d,e = lst
print(f"(a,b,c,d,e) = {lst} => a = {lst[0]}, b = {lst[1]}, c = {lst[2]}, d = {lst[3]}, "
      f"e = {lst[4]}")
################################################################################################
# ----------------------------------------------------------------------------------------------
# Module 2 [Collections] Assignment
# Topic: Tuple
# Introduction,Accessing tuple,Operations, Working, function and method
# Assignment Level Basic
# ----------------------------------------------------------------------------------------------
################################################################################################

################################################################################################
# B1: What is tuple? Difference between list and tuple
################################################################################################
# Answer: A tuple is a immutable list of values. It can be indexed and sliced but can't be
#         changed.
#         List is mutable data type whereas Tuple is immutable in nature.

################################################################################################
# B2: Write a Python program to create a tuple with different data types
################################################################################################
random_data = 'Boy', 21, 2+5j, 0o14, 0xff, 15.5
print(f"Tuple with random data: {random_data}")

################################################################################################
# B3: Write a Python program to create a tuple with numbers
################################################################################################
numeric_tuple = 1,2,3,4,5
print(f"Tuple with numbers: {numeric_tuple}")

################################################################################################
# B4: Write a Python program to convert a tuple to a string
################################################################################################
char_tuple = 'p','r','a','t','i','k'
string = ''.join(char_tuple)
print(f"Converting tuple of characters {char_tuple} into string: '{string}'")

################################################################################################
# B5: Write a Python program to check whether an element exists within a tuple
################################################################################################
char_tuple = 'p','r','a','t','i','k'
char = 'a'
if char in char_tuple:
    print(f"character '{char}' is in tuple {char_tuple}")
else:
    print(f"character '{char}' is not in tuple {char_tuple}")

################################################################################################
# B6: Write a Python program to convert a list to a tuple
################################################################################################
char_list = ['p','r','a','t','i','k']
char_tuple = tuple(char_list)
print(f"Converting list of characters '{char_list}' into tuple of characters '{char_tuple}'")

################################################################################################
# B7: Write a Python program to find the length of a tuple.
################################################################################################
char_tuple = 'p','r','a','t','i','k'
print(f"Length of the tuple '{char_tuple}' is : {len(char_tuple)}")

################################################################################################
# ----------------------------------------------------------------------------------------------
# Assignment Level Intermediate
# ----------------------------------------------------------------------------------------------
################################################################################################

################################################################################################
# I1: Write a Python program to reverse a tuple
################################################################################################
char_tuple = 'p','r','a','t','i','k'
print(f"Printing tuple '{char_tuple}' in reverse order: {char_tuple[::-1]}")

################################################################################################
# I2: Write a Python program to replace last value of tuples in a list
################################################################################################
list_of_tuples = [(1,2,3),(4,5,6),(7,8,9)]
updated_list_of_tuple = []
for tuple in list_of_tuples:
    updated_list_of_tuple.append(tuple[:-1] + (10,))

print(f"List of tuples '{list_of_tuples}' after replacing last element of each tuple: "
      f"'{updated_list_of_tuple}'")

################################################################################################
# I3: Write a Python program to find the repeated items of a tuple
################################################################################################
tuple = 1,2,2,3,3,3,4,4,4,4
set_from_tuple = set(tuple)
for n in set_from_tuple:
    if tuple.count(n) > 1:
        print(f"Frequency of element '{n}' in tuple '{tuple} 'is: {tuple.count(n)}")

################################################################################################
# ----------------------------------------------------------------------------------------------
# Assignment Level Advance
# ----------------------------------------------------------------------------------------------
################################################################################################

################################################################################################
# A1: Write a Python program to remove an empty tuple(s) from a list of tuples.
################################################################################################
list_of_tuples = [(), (1,), (2,2), (), (1,), (2,2)]
list_of_tuples_without_empty_tuples = list_of_tuples[:]
for n in list_of_tuples:
    if len(n) == 0:
        list_of_tuples_without_empty_tuples.remove(n)
print(f"List of tuples '{list_of_tuples}' after removing empty tuples: "
      f"{list_of_tuples_without_empty_tuples}")

################################################################################################
# A2: Write a Python program to unzip a list of tuples into individual lists
################################################################################################

################################################################################################
# A3: Write a Python program to convert a list of tuples into a dictionary
################################################################################################
list_of_tuples = [('A',1),('B',2),('C',3),('D',4)]
dictionary = dict(list_of_tuples)
print(f"Converting list of tuples '{list_of_tuples}' into dictionary: {dictionary}")

################################################################################################
# ----------------------------------------------------------------------------------------------
# Module 2 [Collections] Assignment
# Topic: Dictionary
# Introduction, Accessing value in Dictionaries, Working with dictionaries, properties
# Assignment Level Basic
# ----------------------------------------------------------------------------------------------
################################################################################################

################################################################################################
# B1: What is Dictionaries?
################################################################################################

################################################################################################
# B2: How will you create a dictionary in python?How will you get all the keys from the dictionary? How will you get all the values from the dictionary?
################################################################################################

################################################################################################
# B3: How will you create a dictionary using tuples in python?
################################################################################################

################################################################################################
# B4: Write a Python script to sort (ascending and descending) a dictionary by value
################################################################################################

################################################################################################
# B5: Write a Python script to concatenate following dictionaries to create a new one
################################################################################################

################################################################################################
# B6: Write a Python script to check if a given key already exists in a dictionary
################################################################################################

################################################################################################
# B7: How Do You Traverse Through A Dictionary Object In Python?
################################################################################################

################################################################################################
# B8: How Do You Check The Presence Of A Key In A Dictionary?
################################################################################################

################################################################################################
# ----------------------------------------------------------------------------------------------
# Assignment Level Intermediate
# ----------------------------------------------------------------------------------------------
################################################################################################

################################################################################################
# I1: Write a Python script to print a dictionary where the keys are numbers between 1 and 15
#     (both Sample Dictionary {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81,
#     10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
################################################################################################

################################################################################################
# I2: Write a Python program to check multiple keys exists in a dictionary
################################################################################################

################################################################################################
# I3: Write a Python script to merge two Python dictionaries
################################################################################################

################################################################################################
# I4: Write a Python program to map two lists into a dictionary
################################################################################################

################################################################################################
# I5: Write a Python program to combine two dictionary adding values for common keys.
#     d1 = {'a': 100, 'b': 200, 'c':300} d2 = {'a': 300, 'b': 200, 'd':400}
#     Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
################################################################################################
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d2_copy = dict(d2)

for key in d1.keys():
    if key in d2.keys():
        d2_copy[key] = d1[key] + d2[key]
    else:
        d2_copy[key] = d2[key]

print(d2_copy)
################################################################################################
# I6: Write a Python program to print all unique values in a dictionary.
################################################################################################

################################################################################################
# I7: Why Do You Use The Zip() Method In Python?
################################################################################################

################################################################################################
# ----------------------------------------------------------------------------------------------
# Assignment Level Advance
# ----------------------------------------------------------------------------------------------
################################################################################################

################################################################################################
# A1: Write a Python program to create and display all combinations of letters, selecting each
#     letter from a different key in a dictionary.
#     Sample data : {'1':['a','b'], '2':['c','d']}
#     Expected Output: ac ad bc bd
################################################################################################

################################################################################################
# A2: Write a Python program to find the highest 3 values in a dictionary
################################################################################################

################################################################################################
# A3: Write a Python program to combine values in python list of dictionaries.
#     Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300},
#                   {'item': 'item1', 'amount': 750}]
#     Expected Output: Counter({'item1': 1150, 'item2': 300})
################################################################################################

################################################################################################
# A4: Write a Python program to create a dictionary from a string. Note: Track the count of the
#     letters from the string.
#     Sample string : 'w3resource'
#     Expected output: {'3': 1, 's': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}
################################################################################################