class Animal(object):
    """Makes cute animals."""
    is_alive = True
    health = "good"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        print self.name
        print self.age

hippo = Animal("Charley", 35)
sloth = Animal("Freddy", 6) 
ocelot = Animal("Suzy", 8)

print hippo.health
print sloth.health
print ocelot.health