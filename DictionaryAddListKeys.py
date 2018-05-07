# dictionaries
try:
    
    aDictionary = { 1 : "January", 2 : "February", 3 : "March", 4 : "April", 5 : "May", 6 : "June", 7 : "July", 8 : "August", 9 : "September", 10 : "October", 11 : "November" }
    aDictionary[ 12 ] = "December" # add item to dictionary


    print "The raw dictionary data is:", aDictionary
    print "\nThe entries in the dictionary are:"


    for item in aDictionary.keys():
        print "aDictionary[ ", item, " ] = ", aDictionary[ item ]

except Exception, e:
    print str(e)