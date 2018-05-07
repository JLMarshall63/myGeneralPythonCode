try:
    import math
    def distance_from_zero(x):
        if type(x) == float or type(x) == int:
            result = abs(x)
            print result
            return result
        else:
            #return False
            print "Nope"
            return "Nope"
    z = "h"
    distance_from_zero("h")
except Exception , e:
    str(e)