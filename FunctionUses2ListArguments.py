m = [1, 2, 3]
n = [4, 5, 6]

# Add your code here!
def join_lists(x,y):
    z = x + y
    return z
# You want this to print [1, 2, 3, 4, 5, 6]

# Add your code here!
def join_lists(x,y):
    z = zip(x,y)
    
    return z

print join_lists(m, n)