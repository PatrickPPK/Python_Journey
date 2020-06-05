############### The note is for educational purpose only ###############
# String: - contiguous set of characters represented in the quotation marks
#         - immutable sequence data type, i.e any changes to a string creates completely new string object
#         - pairs of single, double quotes
#         - Python does not have a character data type, a single character is simply a string with a length of 1

# Creating the strings using
>>> 'spam eggs'  # single quotes
'spam eggs'
>>> 'doesn\'t'  # use \' to escape the single quote...
"doesn't"
>>> "doesn't"  # ...or use double quotes instead
"doesn't"
>>> '"Yes," they said.'
'"Yes," they said.'
>>> "\"Yes,\" they said."
'"Yes," they said.'
>>> '"Isn\'t," they said.'
'"Isn\'t," they said.'

# Escape sequences
# \newline	- backslash and newline ignored
# \\		- backslash
# \'		- single quote
# \"		- double quote
# \a		- ASCII bell
# \b		- ASCII backspace
# \f		- ASCII formfeed
# \n		- ASCII linefeed
# \r		- ASCII carriage return
# \t		- ASCII horizontal tab
# \v		- ASCII vertical tab
# \ooo		- character with octal value ooo
# \xhh		- character with hexadecimal value hh

>>> s = 'First line.\nSecond line.'  # \n means newline
>>> s  # without print(), \n is included in the output
'First line.\nSecond line.'
>>> print(s)  # with print(), \n produces a new line
First line.
Second line.

# use raw strings by adding an r before the first quote
>>> print(r'C:\some\name')  # note the r before the quote
C:\some\name

# Multi-line strings using triple quotes
>>> s = '''Food
       For 
       Thought'''
>>> print(s)
Food
For
Thought
>>> s = """How
Are
You!"""
>>> print(s)
How
Are
You!

# Two or more string literals (i.e. the ones enclosed between quotes) next to each other are automatically concatenated.
>>> 'Py' 'thon'
'Python'

# Breaking long strings over multiple lines
>>> text = ('Put several strings within parentheses '
...         'to have them joined together.')
>>> text
'Put several strings within parentheses to have them joined together.'
>>> multiline_str = "I'm learning Python. " \
"This note explains string data type. " \
"Let me know if you find any errors in this note."
print(multiline_str)

# Indexing - Accessing single character in a string
# +---+---+---+---+---+---+
#  | P | y | t | h | o | n |
# +---+---+---+---+---+---+
#  0   1   2   3   4   5   6
# -6  -5  -4  -3  -2  -1

>>> s = 'Python'
>>> s[0]
'P'
>>> s[5]
'n'
>>> s[-1]
'n'
>>> s[-3]
'h'

# Slicing - To access a range of characters(to obtain substring) in a String
>>> s[0:2]  # characters from position 0 (included) to 2 (excluded)
'Py'
>>> s[2:5]  # characters from position 2 (included) to 5 (excluded)
'tho'
# Note how the start is always included, and the end always excluded. This makes sure that s[:i] + s[i:] is always equal to s
>>> s[:2] + s[2:]
'Python'





