############### The note is for educational purpose only ###############
# Set: Unordered collection of data type, iterable, mutable, no duplicate elements
# Usage: Basic uses include membership testing and eliminating duplicate entries.

# Creating the set
>>> s = set()
>>> s = {}                             # Create dictionary, not a set
>>> type(s)                            # Printing type of s
<class 'dict'>
>>> s = {'a','b','c','a','d'}
>>> s
{'a','b','c','d'}
>>> a = set('abracadabra')
>>> a                                  # unique letters in a
{'a', 'r', 'b', 'c', 'd'}
>>> a = {x for x in 'abracadabra' if x not in 'abc'}
>>> a
{'r', 'd'}
>>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>> print(basket)                      # show that duplicates have been removed
{'orange', 'banana', 'pear', 'apple'}
>>> 'orange' in basket                 # fast membership testing
True
>>> 'crabgrass' in basket
False
>>> 2 in {1,2,3}                       # Existence check
True
>>> 4 in {1,2,3}                       # Existence check
False
>>> 4 not in {1,2,3}                   # Existence check
True

# Set methods
# with other sets
>>> a = {1, 2, 2, 3, 4}
>>> b = {3, 3, 4, 4, 5}

# Intersection(a & b) - returns a new set with elements present in both a and b
>>> {1, 2, 3, 4, 5}.intersection({3, 4, 5, 6})
{3, 4, 5}
>>> {1, 2, 3, 4, 5} & {3, 4, 5, 6}
{3, 4, 5}
>>> a.intersection(b)
{3, 4}

# Union(a | b)- returns a new set with elements present in either a and b
>>> {1, 2, 3, 4, 5}.union({3, 4, 5, 6})
{1, 2, 3, 4, 5, 6}
>>> {1, 2, 3, 4, 5} | {3, 4, 5, 6}
{1, 2, 3, 4, 5, 6}
>>> a.union(b)
{1, 2, 3, 4, 5}

# Difference(a - b) - returns a new set with elements present in a but not in b
>>> {1, 2, 3, 4}.difference({2, 3, 5})
{1, 4}
>>> {1, 2, 3, 4} - {2, 3, 5}
{1, 4}
>>> a.difference(b)
{1, 2}
>>> b.difference(a)
{5}

# Symmetric difference(a ^ b) - returns a new set with elements present in either a or b but not in both
>>> {1, 2, 3, 4}.symmetric_difference({2, 3, 5})
{1, 4, 5}
>>> {1, 2, 3, 4} ^ {2, 3, 5}
{1, 4, 5}
>>> a.symmetric_difference(b)
{1, 2, 5}
>>> b.symmetric_difference(a)
{1, 2, 5}
# NOTE: a.symmetric_difference(b) == b.symmetric_difference(a)
# NOTE: a.difference(b) != b.difference(a)

# Superset check(a >= b) - tests whether each element of b is in a.
>>> {1, 2}.issuperset({1, 2, 3})
False
>>> {1, 2} >= {1, 2, 3}
False
>>> c = {1, 2}
>>> c.issubset(a)
True

# Subset check(a <= b) - tests whether each element of a is in b.
>>> {1, 2}.issubset({1, 2, 3})
True
>>> {1, 2} <= {1, 2, 3}
True
>>> a.issuperset(c)
True

# Disjoint check - tests whether both the sets have no common elements
>>> {1, 2}.isdisjoint({3, 4})
True
>>> {1, 2}.isdisjoint({1, 4})
False
>>> d = {5, 6}
>>> a.isdisjoint(b)
False
>>> a.isdisjoint(d)
True

# with single elements
# Add
>>> s = {1,2,3}
>>> s.add(4)
>>> s
{1,2,3,4}

# Discard
>>> s.discard(3)
>>> s
{1,2,4}
>>> s.discard(5)
>>> s
{1,2,4}

# Remove - it generates KeyError if the element is not found in the set
>>> s.remove(2)
>>> s
{1,4}
>>> s.remove(2)
KeyError: 2

# method                in-place operation      in-place method
# ------                ------------------      ---------------
# union                   s |= t                  update
# intersection            s &= t                  intersection_update
# difference              s -= t                  difference_update
# symmetric_difference    s ^= t                  symmetric_difference_update

# Get the unique elements of a list
>>> restaurants = ["McDonald's", "Burger King", "McDonald's", "Chicken Chicken"]
>>> restaurants
["McDonald's", "Burger King", "McDonald's", "Chicken Chicken"]
>>> list(set(restaurants))
['Burger King', "McDonald's", 'Chicken Chicken']

# Set of sets
>>> {{1,2}, {3,4}}                   # leads to unhashable type error
    {{1,2}, {3,4}}
TypeError: unhashable type: 'set'
# Instead, use frozenset
>>> {frozenset({1, 2}), frozenset({3, 4})} # What is frozenset - <PENDING DESCRIPTION>









