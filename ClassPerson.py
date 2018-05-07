#create Person class that has 2 methods
class Person(object):
    #write method to set a name / note: first 'self' parameter refers to the
    #object itself and second parameter is a variable that contains an attribute
    #of the object, in this case name
    def setname(self, name):
        self.name = name
    #write a method to set a greeting
    def greeting(self):
        print "My name is {0}.".format(self.name)
        
#instantiate an object of person class
me = Person()

#call setname and greeting methods and pass a name to new object of
#person class as argument

me.setname("Pat Wilson")
me.greeting()