'''
The program should do the following:

Prompt the user to select a shape

Depending on the shape the user selects, calculate the area of that shape

Print the area of that shape to the user
'''
from math import pi
from time import sleep
from datetime import datetime
now = datetime.now()

print '%s/%s/%s/%s/%s/%s' % (now.month, now.day, now.year, now.hour, now.minute, now.second)
sleep(1)
                    
hint = "Units = Inches\n"

entry = raw_input("Print C to calculate a Circle or T to calculate a Triangle: " + hint)

if entry == "C":
    r = float(raw_input("Enter radius: "))
    area = pi * r**2
    print "The pie is baking . . ."
    sleep(1)
    print area

elif entry == "T":
    h = float(raw_input("Enter height: "))
    b = float(raw_input("Enter base: "))
    area = ((0.5 * b)  * h)
    print "Uni Bi Tri . . ."
    sleep(1)
    print area







    