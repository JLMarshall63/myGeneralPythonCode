try:
    import arcpy
    arcpy.env.workspace = "C:\EsriPress\Python\Data\Exercise06\Results\NM.gdb"
    dataItem = "railroad"
    desc = arcpy.Describe(dataItem)
    print "Dataset type: " + desc.datasetType

except Exception, e:
    print str(e)