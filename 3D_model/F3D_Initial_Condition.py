#F3D_Initial_Condition.py
#currently set for no ar at all in the grid at the beginning
from scipy import shape
from F3D_Grid import gridx
from F3D_Parameters import nx, dx, L
import numpy as np

#creates a 2d ?x2 matrix containing zeros in the first column and gridx in the second column. 
condition = np.zeros([nx, 2])
condition[:, 1] = np.array(gridx)

gridu = []
for i in gridx:
    if i >= L/2:
        u = 0.0
        #u = 0.0
    else:
        u = 0.0
    gridu.append(u)
condition[:, 0] = np.array(gridu)

