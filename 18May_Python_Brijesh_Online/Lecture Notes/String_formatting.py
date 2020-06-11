############### The note is for educational purpose only ###############

# Basics of string formatting
>>> foo = 1
>>> bar = 'bar'
>>> baz = 3.14

# str.format
# Using baracket pairs
>>> print('{}, {} and {}'.format(foo, bar, baz))
1, bar and 3.14

# Using indexes
>>> print('{0}, {1}, {2}, and {1}'.format(foo, bar, baz))
1, bar, 3.14, and bar
>>> print('{0}, {1}, {2}, and {3}'.format(foo, bar, baz))
IndexError: tuple index out of range
  
# Names arguments
>>> print("X value is: {x_val}. Y value is: {y_val}.".format(x_val=2, y_val=3))
X value is: 2. Y value is: 3.
    
# Referencing object attributes
>>> class car(object):
	def __init__(self, color):
		self.color = color

>>> my_car = car('Red')
>>> print('My car is: {0.color}'.format(my_car))
My car is: Red
  
# Referecing dictionary keys
>>> lang_dict = {'language': 'Python', 'creator':'Guido van Rossum'}
>>> print("'{0[creator]}' is the creator of the '{0[language]}' programming langauge".format(lang_dict))
'Guido van Rossum' is the creator of the 'Python' programming langauge

# Referecing list and tuple indices
my_list = [0,1,2,3]
>>> print("'{0[1]}' is the 1st element of the list '{0}'".format(my_list))
'1' is the 1st element of the list '[0, 1, 2, 3]'

# Note: Module operator %-- string formatting or interpollation operator -- for formatting strings
# str.format is a successor of % and it offers greater flexibilty. Hence, not including examples using % opearator

# Alignment and padding
# Format expression of the form
#	{:[fill_char][align_operator][width]}
# where, align_operator is one of:
#	   > -- forces the field to be right-aligned within width
#	   < -- forces the field to be left-aligned within width
#	   ^ -- forces the field to be centered within width
#	   = -- forces the padding to be placed after the sign (numeric types only)
#	 fill_char (if omitted, default is whitespace) is the character used for the padding

>>> '{:~<9s}, World'.format('Hello')
'Hello~~~~, World'

>>> '{:->9s}, World'.format('Hello')
'----Hello, World'

>>> '{:~^9s}'.format('Hello')
'~~Hello~~'

'{:0=6d}'.format(-123)
# '-00123'

>>> '{:^7s}'.format(foo)
'  bar  '

# Format literals (f-string)








