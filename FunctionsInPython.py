def biggest_number(*args):
    print max(args)
    return max(args)
    
def smallest_number(*args):
    print min(args)
    return min(args)

def distance_from_zero(arg):
    print abs(arg)
    return abs(arg)


biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)

'''
The max() function takes any number of arguments and returns the
largest one. ("Largest" can have odd definitions here, so it's best
to use max() on integers and floats, where the results are
straightforward, and not on other objects, like strings.)
For example, max(1,2,3) will return 3 (the largest number in the
set of arguments).
'''

# Set maximum to the max value of any set of numbers 
maximum = max(3, -9, 78, 99, -92)

print maximum

# Set minimum to the min value of any set of numbers on line 3!

minimum = min(12, -99, 78, 3456, -12689)

print minimum

absolute = abs(-99)

print absolute

'''
Finally, the type() function returns the type of the data it
receives as an argument. If you ask Python to do the following:

print type(42)
print type(4.2)
print type('spam')
Python will output:
<type 'int'>
<type 'float'>
<type 'str'>

Instructions

Have Python print out the type of an int, a float, and a str string
in the editor. You can pick any values on which to call type(), so
long as they produce one of each.
'''
from types import *

print type(42)
print type(42.34)
print type('spam')
  
