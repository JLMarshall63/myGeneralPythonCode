from math import sqrt
for i in range(1001, 0, -1):
    root = sqrt(i)
    if root == int(root):
        print i
        break