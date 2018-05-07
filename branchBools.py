# set so both conditions will print

def using_control_once():
    if 7 == 7:
        return "Success #1"

def using_control_again():
    if "A" != "B":
        return "Success #2"

print using_control_once()
print using_control_again()

'''
The else statement complements the if statement. An if/else pair
says: "If this expression is true, run this indented code block;
otherwise, run this code after the else statement."

Unlike if, else doesn't depend on an expression. For example:
if 8 > 9:
    print "I don't printed!"
else:
    print "I get printed!"

Instructions 
Complete the else statements to the right. Note the
indentation for each line!

'''
answer = "'Tis but a scratch!"

def black_knight():
    if answer == "'Tis but a scratch!":
        return True
    else:             
        return False

def french_soldier():
    if answer == "Go away, or I shall taunt you a second time!":
        return True
    else:             
        if answer == "'Tis but a scratch!":
            return False

