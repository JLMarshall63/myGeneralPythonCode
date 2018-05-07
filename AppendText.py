fileName = "C:\University of Washington GIS\UOWSummer2017\GEOG565\TextDocs\myTestB.txt"
x = raw_input("Enter correspondence to append here.")

with open(fileName, 'a') as fObj:
    fObj.write(x)