try:
    # Class definition
    class Animal(object):
        """Makes cute animals."""
        # For initializing our instance objects
        def __init__(self, name, age, is_hungry):
            self.name = name
            self.age = age
            self.is_hungry = is_hungry

# Note that self is only used in the __init__()
# function definition; we don't need to pass it
# to our instance objects.

    zebra = Animal("Jeffrey", 2, True)
    giraffe = Animal("Bruce", 1, False)
    panda = Animal("Chad", 7, True)

    print "My zebra is {0} and he is {1} years old. Bool he's hungry: {2} ".format(zebra.name, zebra.age, zebra.is_hungry)
    print "My giraffe is {0} and he is {1} years old. Bool he's hungry: {2} ".format(giraffe.name, giraffe.age, giraffe.is_hungry)
    print "My panda is {0} and he is {1} years old. Bool he's hungry: {2} ".format(panda.name, panda.age, panda.is_hungry)

except IndexError as e:
    print "An error occured: " + str(e)