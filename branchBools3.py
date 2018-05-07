# Make sure that the_flying_circus() returns #True

var = 9

def the_flying_circus():
    if var > 1:    
        return "True"
    elif var != "A" or var < 1:
       return "False"
    else:
        return 0
print the_flying_circus()
