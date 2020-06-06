############### The note is for educational purpose only ###############
# String: - contiguous set of characters represented in the quotation marks
#         - immutable sequence data type, i.e any changes to a string creates completely new string object
#         - pairs of single, double quotes
#         - Python does not have a character data type, a single character is simply a string with a length of 1

# ---------------------------------------------------
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

# ---------------------------------------------------
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

# ---------------------------------------------------
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
# Attempting to use an index that is too large will result in an error
>>> s[10]  # the word only has 6 characters
IndexError: string index out of range
# Python strings cannot be changed
>>> s[0] = 'J'
TypeError: 'str' object does not support item assignment

# ---------------------------------------------------
# Slicing - To access a range of characters(to obtain substring) in a String
>>> s[0:2]  # characters from position 0 (included) to 2 (excluded)
'Py'
>>> s[2:5]  # characters from position 2 (included) to 5 (excluded)
'tho'

# Note how the start is always included, and the end always excluded. This makes sure that s[:i] + s[i:] is always equal to s
>>> s[:2] + s[2:]
'Python'

# Slice indices have useful defaults; an omitted first index defaults to zero, an omitted second index defaults to the 
#  size of the string being sliced
>>> s[:2]   # character from the beginning to position 2 (excluded)
'Py'
>>> s[4:]   # characters from position 4 (included) to the end
'on'
>>> s[-2:]  # characters from the second-last (included) to the end
'on'

# Out of range slice indexes are handled gracefully
>>> s[4:42]
'on'
>>> s[42:]
''

# Python strings cannot be changed
>>> s[0:2] = 'Jy'
TypeError: 'str' object does not support item assignment

# ---------------------------------------------------
# String Methods - Most frequently used methods only
# ---------------------------------------------------
# ---------------------------------------------------
# Changing capitalization of a string
# ---------------------------------------------------

# (1) str.casefold - Return a casefolded copy of the string, used for caseless matching, not intended for display purposes
>>> "XßΣ".casefold()
'xssσ'
>>> "XßΣ".lower()
'xßς'
>>> str.casefold("XßΣ")
'xssσ'

# (2) str.upper - all characters converted to its uppercase equivalent
>>> "This is a 'string'.".upper()
"THIS IS A 'STRING'."
>>> str.upper("This is a 'string'.")
"THIS IS A 'STRING'."

# (3) str.lower - all characters converted to its lowercase equivalent
>>> "This IS a 'string'.".lower()
"this is a 'string'."
>>> str.lower("This IS a 'string'.")
"this is a 'string'."

# (4) str.capitalize - first character have upper case and the rest lower
>>> "this Is A 'String'.".capitalize()
"This is a 'string'."
>>> str.capitalize("this Is A 'String'.")
"This is a 'string'."

# (5) str.title - every letter in the beginning of a word is made upper case
>>> "this Is a 'String'".title()
"This Is A 'String'"
>>> str.title("this Is a 'String'")
"This Is A 'String'"

# (6) str.swapcase - all lower case characters are swapped to upper case and all upper case characters to lower
>>> "this iS A STRiNG".swapcase()
"THIS Is a strIng"
>>> str.swapcase("this iS A STRiNG")
"THIS Is a strIng"

# ---------------------------------------------------
# Stripping unwanted leading/trailing characters from a string
# ---------------------------------------------------

# (1) str.strip([chars]) - strips any leading or trailing characters contained in the argument chars; 
#                          if chars is not supplied or is None, all white space characters are removed by default
>>> " a line with leading and trailing space ".strip()
'a line with leading and trailing space'
>>> ">>> a Python prompt".strip('> ') # strips '>' character and space character
'a Python prompt'

# (2) str.lstrip([chars]) - strips any leading characters
>>> "    spacious string    ".lstrip()
'spacious string    '

# (3) str.rstrip([chars]) - strips any trailing characters
>>> "    spacious string    ".rstrip()
'    spacious string'

# ---------------------------------------------------
# Replace each character in the string using the given translation table
# ---------------------------------------------------

# Make the translation table using the maketrans() method
>>> translation_table = str.maketrans("aeiou", "12345")
>>> my_string = "This is a string!"
# The translate method returns a string which is a translated copy of the original string
>>> translated = my_string.translate(translation_table)
'Th3s 3s 1 str3ng!'
# Set the table argument to None if you only need to delete characters.
>>> 'this syntax is very useful'.translate(None, 'aeiou')
'ths syntx s vry sfl'

# ---------------------------------------------------
# String (not 'str') module's useful constants
# ---------------------------------------------------

>>> import string
# (1) string.ascii_letters - concatenation of ascii_lowercase and ascii_uppercase
>>> string.ascii_letters
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# (2) string.ascii_lowercase - contains all lower case ASCII characters
>>> string.ascii_lowercase
'abcdefghijklmnopqrstuvwxyz'

# string.ascii_uppercase - contains all upper case ASCII characters
>>> string.ascii_uppercase
'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# string.digits - contains all decimal digit characters
>>> string.digits
'0123456789'

# string.hexdigits - contains all hex digit characters
>>> string.hexdigits
'0123456789abcdefABCDEF'

# string.octaldigits - contains all octal digit characters
>>> string.octaldigits
'01234567'

# string.punctuation - contains all characters which are considered punctuation in the C locale
>>> string.punctuation
'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

# string.whitespace - contains all ASCII characters considered whitespace
>>> string.whitespace
' \t\n\r\x0b\x0c'

# string.printable - contains all characters which are considered printable; a combination of string.digits, 
#  string.ascii_letters, string.punctuation, and string.whitespace.
>>> string.printable
'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~\t\n\r\x0b\x0c'

# ---------------------------------------------------
# Reversing a string
# ---------------------------------------------------

# (1) reversed() function - takes a string and returns an iterator in reverse order.
>>> [char for char in reversed('hello')]
['o', 'l', 'l', 'e', 'h']
>>> ''.join(reversed('hello'))
'olleh'

# Using extended slicing with a step of -1 is faster and more concise
>>> 'hello'[::-1]
'olleh'

# ---------------------------------------------------
# Split a string based on a delimiter into a list of strings
# ---------------------------------------------------

# (1) str.split(sep=None, maxsplit=-1) - takes a string and returns a list of substrings of the original string
>>> "This is a sentence.".split()
['This', 'is', 'a', 'sentence.']
>>> " ".split()
[]
>>> "Earth,Stars,Sun,Moon".split(',')
['Earth', 'Stars', 'Sun', 'Moon']
>>> "This is a sentence.".split('en')
['This is a s', 't', 'ce.']

# maxsplit parameter limits the number of splittings that occur. The default value of -1 means no limit
>>> "This is a sentence.".split('e', maxsplit=0)
['This is a sentence.']
>>> "This is a sentence.".split('e', maxsplit=2)
['This is a s', 'nt', 'nce.']
>>> "This is a sentence.".split('e', maxsplit=-1)
['This is a s', 'nt', 'nc', '.']

# (2) str.rsplit(sep=None, maxsplit=-1) - differs from str.split ("left split") when maxsplit is specified
#                                         The splitting starts at the end of the string rather than at the beginning
>>> "This is a sentence.".rsplit('e', maxsplit=1)
['This is a sentenc', '.']
>>> "This is a sentence.".rsplit('e', maxsplit=2)
['This is a sent', 'nc', '.']


