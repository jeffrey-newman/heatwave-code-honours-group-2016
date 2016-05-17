# Name: Kriging_Ex_02.py
# Description: Interpolates a surface from points using kriging.
# Requirements: Spatial Analyst Extension
# Import system modules

import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
#env.workspace = "C:/sapyexamples/data"

for i in range(2006,2050):
    # Set local variables
    inFeatures = r"C:\Users\a1091793\Desktop\Heatwave risk mapping\arcgis_workspace\RCP45.shp"
    field = str(i)
    cellSize = 0.001
    outVarRaster = r"C:\Users\a1091793\Desktop\Heatwave risk mapping\arcgis_workspace\Kriging_var_RCP45_" + field + ".tif"
    lagSize = 2000
    majorRange = 2.6
    partialSill = 542
    nugget = 0
    
    # Set complex variables
    kModelOrdinary = KrigingModelOrdinary("CIRCULAR", lagSize,
                                    majorRange, partialSill, nugget)
    kRadius = RadiusFixed(20000, 1)
    
    
    
    # Check out the ArcGIS Spatial Analyst extension license
    arcpy.CheckOutExtension("Spatial")
    
    # Execute Kriging
    outKriging = Kriging(inFeatures, field, kModelOrdinary, cellSize,
                        kRadius, outVarRaster)
    
    # Save the output 
    outKriging.save(r"C:\Users\a1091793\Desktop\Heatwave risk mapping\arcgis_workspace\Kriging_RCP45_" + field + ".tif")
