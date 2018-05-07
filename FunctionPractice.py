def shut_down(s):
    if s >= 212:
        print "Shutting Down"
        return s
    elif s != 212 and s < 212:
        print "Shutdown aborted"
        return s
    else:
        print "Sorry"
        return s
        
shut_down(0)

s = ""
def shut_down(s):
    if s == True:
        s = "Shutting Down"
        print "Shutting Down"
        return s
    elif s != True:
        s = "Shutting aborted"
        print "Shutdown aborted"
        return s
    else:
        print "Sorry"
        return s
        
shut_down("Shutting Down")

s = ""
def shut_down(s):
    if s == "Pear":
        print "Shutting Down"     
        return s
    elif s == "Peach":
        print "Shutdown aborted"
        return s
    else:
        print "Sorry"
        return s
        
shut_down("Peach")