#create Parcel class that has 2 methods
class Parcel(object):
    #write constructor method to set a parcelclass landuse and value properties / note: first 'self'
    #parameter refers to the object itself and second and third parameters are variables
    # that contains parcel attributes / properies, in this case landuse and value
    def __init__(self, landuse, value):
        self.landuse = landuse
        self.value = value
    #write a method to assess parcel's value
    def assessment(self):
        if self.landuse == "SFR":
            rate = 0.05
        elif self.landuse == "MFR":
            rate = 0.04
        else:
            rate = 0.02
        assessment = self.value * rate
        return assessment
        
#instantiate an object of Parcel class passing in landuse and value as arguments
myParcel = Parcel("SFR", 600000)

#use newly instantiated object displays the parcel's land use and tax
print "My parcel land Use: " , myParcel.landuse
mytax = myParcel.assessment()
print "My parcel assessent: $", myParcel.value
print "My parcel tax: $", mytax


