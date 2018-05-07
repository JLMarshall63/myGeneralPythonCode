try:
    entry = raw_input("Enter letter here: ")
    myString = "Python Rules!"
    found = False
    for x in myString:
        if x == entry:
            found = True
    if found:
        print "{} is here! ".format(entry)
    else:
        print "{} is not here! ".format(entry)

except Exception, e:
    str(e)