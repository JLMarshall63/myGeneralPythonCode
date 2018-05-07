array = [2,4,6,8,10]
num = 0
for x in array:    
    num = num + 1
    print num, x

for num, x in enumerate(array):
    print num +1, x

direction = ["left","right","up","down"]

for i in range(len(direction)):
    print(i + 1, direction[i])

for i, j, in enumerate(direction):
    print i + 1, j

new_dict = dict(enumerate(direction))
print(new_dict)

##[print(i, j) for i, j in enumerate(new_dict)]