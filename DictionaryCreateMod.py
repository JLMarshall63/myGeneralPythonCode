import arcpy
install = arcpy.GetInstallInfo()
for key in install:
    print "{0} : {1}".format(key, install[key])

zoning = {}
zoning["RES"] = "Residential"
zoning["IND"] = "Industrial"
zoning["OPEN SPACE"] = "Open Space"
print zoning
#Modify dictionary
zoning["IND"] = "Industry"
print zoning
#delete dictionary item
del zoning["RES"]
print zoning
#method to just display the dic keys
print zoning.keys()
#method to just display the dic values
print zoning.values()
#method to just display the dic items (key + value)
print zoning.items()

import operator
stats = {'a': 1000, 'b' : 2000, 'c' : 3000}
max(stats.iteritems(), key=operator.itemgetter(1))[0]
print max(stats)
