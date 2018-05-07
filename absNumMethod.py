try:
    import math

    def distance_from_zero(x):
        if type(x) == float or type(x) == int:
            result = abs(x)
            print result
            return result
        else:         
            print "Nope"
            return "Nope"
            

    z = -89.55
    distance_from_zero(z)

except Exception , e:
    str(e)