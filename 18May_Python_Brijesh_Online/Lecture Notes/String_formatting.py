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
