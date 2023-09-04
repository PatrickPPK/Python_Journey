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
# \uxxxx	- Unicode character with 16-bit hex value xxxx
# \xxxxxxxxx  - Unicode character with 32-bit hex value xxxx
# \N{<name>}	- Character from Unicode database with given <name>

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
# String operators
# (1) '+' operator - concatenates strings
>>> s = 'abc'
>>> t = '123
>>> u = '!@#'

>>> s + '-' + t
'abc-123'
>>> s + '-' + t + '-' + u
'abc-123-!@#'

>>> print('Hello' + 'World!')
HelloWorld!

# (2) '*' operator - creates multiple copies of the strings
>>> s = 'bla'
>>> s * 3
'blablabla'
>>> s * -1
''

# (3) 'in' operator - membership operator - returns True if first operand is contained within the second
>>> "foo" in "foo.baz.bar"
True

# (4) 'not in' operator - membership operator - returns True if first operand is not contained within the second
>>> "a" not in "test"
True

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

# Note: how the start is always included, and the end always excluded. This makes sure that s[:i] + s[i:] is always equal to s
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

# Specifying a stride in a string slice - Adding an additional : and a third index designates a stride (also called a step), 
#  which indicates how many characters to jump after retrieving each character in the slice.
>>> s = 'Python'
>>> s[::2]
'Pto'
>>> s[1:5:2]
'yh'

# Python strings cannot be changed
>>> s[0:2] = 'Jy'
TypeError: 'str' object does not support item assignment
       
# ---------------------------------------------------
# Built-in String Functions
# ---------------------------------------------------
# (1) chr() - Returns a character value for the given integer
>>> chr(65)
'A'
>>> chr(49)
'1'
>>> chr(10)
'\n'

# (2) ord() - Return an integer value for the given character
>>> ord('a')
97
>>> ord('0')
48
>>> ord('+')
43

# (3) len() - Return the length of a string
>>> s = 'Python is a programming language'
>>> len(s)
32

# (4) str() - Return a string representation of an object
>>> str(1+3j)
'(1+3j)'
>>> str(10.5)
'10.5'
>>> str(10 * 5)
'50'

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
# Removing prefix and suffix substring from the original string
# ---------------------------------------------------
# (1) str.removeprefix(substring) - Returns a new string with trimmed prefix substring if found
#                                 otherwise returns the original string
>>> "blablabla...original string".removeprefix('blablabla')
'...original string'

# (1) str.removesuffix(substring) - Returns a new string with trimmed suffix substring if found
#                                 otherwise returns the original string
>>> "original string...blablabla".removeprefix('blablabla')
'original string...'

# ---------------------------------------------------
# Find a substring in a string
# ---------------------------------------------------
# (1) str.find(sub[, start[, end]]) - searches the target string for a given substring, 
#                                      return lowest index if specified substring is found
#                                      return -1 if specified substring is not found
>>> statement = 'I love Python. You love Python. We love Python. But Pythons do not love Python!'
# Substring is searched in 'hings with great love'
>>> print(statement.find('Python'))
7
>>> print(statement.find('Python', 10))
24
>>> print(statement.find('Python', 30, 50))
40

# (2) str.rfind(sub[, start[, end]]) - searches the target string for a given substring starting at the end, 
#                                      return highest index if specified substring is found
#                                      return -1 if specified substring is not found
>>> statement = 'I love Python. You love Python. We love Python. But Pythons do not love Python!'
>>> print(statement.rfind('Python'))
7
>>> print(statement.rfind('Python', 10))
24
>>> print(statement.rfind('Python', 30, 50))
40

# (3) str.index(sub[, start[, end]]) - searches the target string for a given substring, 
#                                      return lowest index if specified substring is found
#                                      raises an ValueError exception if specified substring is not found
>>> genre = 'Mooooosic'
>>> genre.index('o')
1
>>> genre.index('o', 3)
3
>>> genre.index('o', 4, 6)
4
>>> genre.index('p', 4, 6)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: substring not found

# (2) str.rindex(sub[, start[, end]]) - searches the target string for a given substring starting at the end, 
#                                      return highest index if specified substring is found
#                                      raises an ValueError exception if specified substring is not found
>>> genre = 'Mooooosic'
>>> genre.rindex('o')
5
>>> genre.rindex('o', 3)
5
>>> genre.rindex('o', 1, 4)
3
>>> genre.rindex('p', 4, 6)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: substring not found
       
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
>>> string.octdigits
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

# (3) str.splitlines(keepends=False) - Return a list of the lines in the string, breaking at line boundaries. 
#                                      Line breaks are not included in the resulting list unless keepends is given and true.

# This method splits on the following line boundaries. In particular, the boundaries are a superset of universal newlines.

# Representation       -           Description
# \n                   -           Line Feed
# \r                   -           Carriage Return
# \r\n                 -           Carriage Return + Line Feed
# \v or \x0b           -           Line Tabulation
# \f or \x0c           -           Form Feed
# \x1c                 -           File Separator
# \x1d                 -           Group Separator
# \x1e                 -           Record Separator
# \x85                 -           Next Line (C1 Control Code)
# \u2028               -           Line Separator
# \u2029               -           Paragraph Separator

>>>
'ab c\n\nde fg\rkl\r\n'.splitlines()
['ab c', '', 'de fg', 'kl']
'ab c\n\nde fg\rkl\r\n'.splitlines(keepends=True)
['ab c\n', '\n', 'de fg\r', 'kl\r\n']

# ---------------------------------------------------
# Partition - divide a string based on a separator 
# ---------------------------------------------------
# (1) str.partition(sep) - splits a string at the first occurence of sep and returns tuple consisting of 
#                           the portion of string before sep, sep and the portion of string after sep
>>> s = 'hello there'
>>> s.partition(' ')
('hello', ' ', 'there')
>>> s = 'hello hello hello there'
# Note: If sep is not found in a string, the returned tuple contains string followed by two empty strings
>>> s = 'hello world'
>>> s.partition('.')
('hello world', '', '')

# (1) str.rpartition(sep) - splits a string at the last occurence of sep and returns tuple consisting of 
>>> s = 'hello hello hello there'
>>> s.rpartition(' ')
('hello hello hello', ' ', 'there')

# ---------------------------------------------------
# Replace all occurrences of one substring with another substring
# ---------------------------------------------------
# (1) str.replace(old, new[, count]) - old sub-string which is to be replaced by the new substring
>>> "Make sure to foo your sentence.".replace('foo', 'spam')
"Make sure to spam your sentence."
>>> "This is the island in Pacific Ocean".replace('is','was', 2)
'Thwas was the island in Pacific Ocean'

# ---------------------------------------------------
# Character classification - Testing what a string is composed of
# ---------------------------------------------------
# (1) str.isalnum() - returns True if all characters in the given string are alphanumeric
>>> "Hello2World".isalnum()
True
>>> "2016".isalnum()
True
>>> "Hello World".isalnum() # contains whitespace
False

# (2) str.isalpha() - returns True if the all characters in a given string are alphabetic
>>> "Hello World".isalpha() # contains a space
False
>>> "HelloWorld".isalpha()
True

# (3) str.isascii() - returns True if the string is empty or it contains only ascii characters
>>> "Ž".isascii()
False
>>> "Z".isascii()
True
>>> "ć".isascii()
False
>>> "".isascii()
True

# (4) str.isdecimal() - returns whether the string is a sequence of decimal digits, suitable for representing a decimal number.
# Can't find good example.

# (5) str.isdigit() - includes digits not in a form suitable for representing a decimal number, such as superscript digits.
# Can't find good example.

# (6) str.isidentifier() - returns True if the string is a valid Python identified
>>> "name".isidentifier()
True
>>> "_name".isidentifier()
True
>>> "name1".isidentifier()
True
>>> "$name".isidentifier()
False
# Note: the method returns True for a string that matches a Python keyword
>>> "and".isidentifier()
True
# Note: To ensure that a string would serve as a valid Python identifier, check that .isidentifier() is True and that iskeyword() is False.
>>> from keyword import iskeyword
>>> s = 'and'
>>> s.isidentifier() is True and iskeyword(s) is False
False
>>> s = 'apple'
>>> s.isidentifier() is True and iskeyword(s) is False
True

# (7) str.islower() - returns True if all characters in a given string are lowerrcase
>>> "Hello world".islower()
False
>>> "hello world".islower()
True

# (8) str.isnumeric() - includes any number values, even if not digits, such as values outside the range 0-9.
# Can't find good example.

# (9) str.isprintable - returns True if the string is empty or it contains only printable characters.
>>> "\t\r\n".isprintable()
False
>>> "a b".isprintable()
True
>>> "a\bb".isprintable()
False

# (10) str.isspace - returns True if the string contains only whitespace characters.
>>> "\t\r\n".isspace()
True
>>> " ".isspace()
True
>>> "".isspace()
False

# (11) str.istitle() - returns True if every word begins with an uppercase character followed by lowercase characters
>>> "Hello world".istitle()
False
>>> "Hello World".istitle()
True

# (12) str.isupper() - returns True if all characters in a given string are uppercase
>>> "HeLLO WORLD".isupper()
False
>>> "HELLO WORLD".isupper()
True

# ---------------------------------------------------
# String Contains - membership operator ('in', 'not in')
# ---------------------------------------------------
>>> "foo" in "foo.baz.bar"
True
>>> "a" not in "test"
True

# ---------------------------------------------------
# Join a list of strings into one string
# ---------------------------------------------------
>>> " ".join(["once","upon","a","time"])
"once upon a time"
>>> "---".join(["once", "upon", "a", "time"])
"once---upon---a---time"

# ---------------------------------------------------
# Counting number of times a substring appears in a string
# ---------------------------------------------------
# (1) str.count(sub[, start[, end]]) - counts the number of occurrences of a sub-string in another string
>>> s = "She sells seashells by the seashore."
>>> s.count("sh")
2
>>> s.count("sh", 10)
2
>>> s.count("sh", 10, 20)
1
>>> s.count("seashells")
1

# ---------------------------------------------------
# Justify strings
# ---------------------------------------------------
# (1) str.ljust(width[, fill]) - returns a string consisting of str left-justified in a field of width
#                                By default, padding consists of the ASCII space character, unless fill argument is specified
>>> 'foo'.ljust(10)
'foo       '
>>> 'foo'.ljust(10, '-')
'foo-------'

# (2) str.rjust(width[, fill]) - returns a string consisting of str right-justified in a field of width
#                                By default, padding consists of the ASCII space character, unless fill argument is specified
>>> 'foo'.rjust(10)
'       foo'
>>> 'foo'.rjust(10, '-')
'-------foo'

# (3) str.center(width[, fill]) - returns a string consisting of str centered in a field of width. 
#                             By default, padding consists of the ASCII space character
>>> 'foo'.center(10)
'   foo    '
>>> 'bar'.center(10, '-')
'---bar----'

# (4) str.expandtabs(tabsize=8) - replaces each tab character ('\t') with spaces; By default eighth spaces
>>> 'a\tb\tc'.expandtabs()
'a       b       c'
>>> 'aaa\tbbb\tc'.expandtabs()
'aaa     bbb     c'
>>> 'aaa\tbbb\tc'.expandtabs(tabsize=4)
'aaa bbb c'

# (5) str.zfill(width) - returns a copy of str left-padded with '0' characters to the specified width
>>> '42'.zfill(5)
'00042'
>>> '+42'.zfill(8)
'+0000042'
>>> '-42'.zfill(8)
'-0000042'

# ---------------------------------------------------
# Test the starting and ending characters of a string
# ---------------------------------------------------
# (1) str.startswith(prefix[, start[, end]]) - test whether a given string starts with the given characters in prefix
>>> s = "This is a test string"
>>> s.startswith("T")
True
>>> s.startswith("Thi")
True
>>> s.startswith("is", 2)
True

# (2) str.endswith(prefix[, start[, end]]) - test whether a given string ends with the given characters in prefix
>>> s = "this ends in a full stop."
>>> s.endswith('.')
True
>>> s.endswith('!')
False
# use a tuple to check if it ends with any of a set of strings
>>> s.endswith(('.', 'something'))
True








