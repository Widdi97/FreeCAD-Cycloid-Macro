# FreeCAD-Cycloid-Macro
 Small python macro for FreeCAD which generates a sketch for a disk of a cycloidal drive. The parametrization of the curve is taken from https://blogs.solidworks.com/teacher/wp-content/uploads/sites/3/Building-a-Cycloidal-Drive-with-SOLIDWORKS.pdf .
![alt text](https://raw.githubusercontent.com/Widdi97/FreeCAD-Cycloid-Macro/main/cycloid_sketch.png?raw=true)

## Parameters
 Five parameters can be set by the user inside of the python macro:
 
 - Number of Rollers *N*
 - Radius of the Rotor *R*
 - Radius of the Rollers *R_r*
 - Excentricity / offset from the input shaft to the center of the rotor *E*
 - Steps of the parametrization *steps*

When setting the debug flag to *True*, the cycloid is also plotted in matplotlib.

## Usage
 Just copy *cycloid.py* to your FreeCAD macro directory. 
 Default on Windows: *C:/Users/--user--/AppData/Roaming/FreeCAD/Macro*)
 Set the parameters of the cycloid disk between line 8 and 12 in the python file.
 Open a FreeCAD project and run the macro.
