#F1D_Grid.py
#This script defines the grid for F1D
#It imports "dx" from the F1D_Parameters module and uses a decimal range function to generate the grid and place this string into "grid". Formats the numbers to display as exponentials if very small. 

from F1D_Parameters import dx

def drange(start, stop, step):
     r = start
     while r <= stop:
     	yield r
     	r += step
     #yield r

gridx = []
["%g" % x for x in drange(0.0, 2.0, dx)]
for x in drange(0.0, 2.0, dx):
    gridx.append(x)
