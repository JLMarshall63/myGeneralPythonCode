'''
What Good are Functions?
You might have considered the situation where you would like to reuse
a piece of code, just with a few different values. Instead of rewriting
the whole code, it's much cleaner to define a function, which can then
be used repeatedly.

Instructions

Check out the code in the editor. If you completed the [Tip Calculator]
[1] project, you'll remember going through and calculating tax and
tip in one chunk of program. Here you can see we've defined two
functions: tax to calculate the tax on a bill, and tip to compute
the tip.  See how much of the code you understand at first glance
(we'll explain it all soon). When you're ready, click Save & Submit
to continue.
'''
def tax(bill):
    """Adds 8% tax to a restaurant bill."""
    bill *= 1.08
    print "With tax: %f" % bill
    return bill

def tip(bill):
    """Adds 15% tip to a restaurant bill."""
    bill *= 1.15
    print "With tip: %f" % bill
    return bill
    
meal_cost = 100
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)

var = 95

def sam(result):
    result *= 1.16
    print "With foo: %f" % result
    return result
sam(var)

def spam():
    '''I say breakfast is here!'''
    print "Eggs!"
'''
After defining a function, it must be called
to be implemented. In the next exercise, spam() in the
last line tells the program to look for the function called spam
and execute the code inside it while passing to it an argument (10)
to evaluate.

'''
# Define the spam function above this line.
spam()

def square(n):
    """Returns the square of a number."""
    squared = n**2
    print "%d squared is %d." % (n, squared)
    return squared
    
# Call the square function on line 9! Make sure to
# include the number 10 between the parentheses.
square(10)

'''
Parameters and Arguments

Let's reexamine the first line that defined square in the previous
exercise:

def square(n):

n is a parameter of square. A parameter acts as a variable name for a
passed in argument. With the previous example, we called square with
the argument 10. In this instance the function was called, n holds
the value 10.

A function can require as many parameters as you'd like, but when you
call the function, you should generally pass in a matching number of
arguments.

Instructions

Check out the function in the editor, power. It should take two
arguments, a base and an exponent, and raise the first to the power
of the second. It's currently broken, however, because its parameters
are missing.

'''
def power(base, exponent):  # Add your parameters here!
    result = base**exponent
    print "%d to the power of %d is %d." %(base, exponent, result)

power(37,4)  # Add your arguments here!

'''
Functions Calling Functions

We've seen functions that can print text or do simple arithmetic,
but functions can be much more powerful than that. For example, a
function can call another function:

def fun_one(n):
    return n * 5

def fun_two(m):
    return fun_one(m) + 7
    
Instructions 

Let's look at the two functions in the editor: one_good_turn
(which adds 1 to the number it takes in as an argument) and
deserves_another (which adds 2).
'''

def one_good_turn(n):
    return n + 1
    print "%Math output = " %(n)
def deserves_another(m):
    return one_good_turn(m) + 2

##one_good_turn(7)

def cube(number):
    cubed = number**3
    print "%d cubed is %d" %(number, cubed)
    return cubed
    
cube(2)

def cubes(number):
    cubed = number**3
    print "%d cubed is %d" %(number, cubed)
    return cubed

def by_three(number):
    if number % 3 == 0:
        cubed = number**3
        print "%d cubed is %d" %(number, cubed)
        return cubed
    else:
        return False

cubes(27)

from math import sqrt
print sqrt(25)

import math
print math.sqrt(25)
x = 100
y = math.sqrt(x)
print "math.sqrt(100): " , (y)
