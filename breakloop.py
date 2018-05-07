# Name: John Marshall
# Date: March 7, 2017
# Description: This script executes a break loop that determines
# the largest square below 1,000. A range of integers is created,
# starting at 1,000 and counting down to zero ( 0 ). The negative
# step is used to iterate downward. When the square root of the
# integer is identical to the integer of the square root, you have
# the solution, and there is no need to continue. The solution is
# printed, and the loop ends.



from math import sqrt
for i in range(99999, 0, -1):
    root = sqrt(i)
    if root == int(root):       #This evaluates whether the root is an integer
        print i
        break