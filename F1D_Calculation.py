#F1D_Calculation.py
#This script calculates the result of each timestep and plots the result at the final timestep. 

import numpy as np
import matplotlib.pylab as plt
import matplotlib.animation as animation
from F1D_Parameters import nx, nt, UL, UR, dx, UnL, UnR
from F1D_BC_Vector import D, bc
from F1D_Initial_Condition import condition

def Calculator():
    u = condition[:, 0]
    for timestep in range(0, nt):
        U = u
        U = np.delete(U, [0, nx-1], axis = 0)
        U = U + bc
        U = np.linalg.solve(D, U.T).T
        u = np.append(np.append(U, UR)[::-1], UL)[::-1]
    return u

def Plot():
    u = Calculator()
    x = condition[:, 1]
    plt.plot(x, u)
    plt.xlabel('distance (x)')
    plt.ylabel('Concentration (u)')
    plt.title('Argon Concentration')
    plt.grid(True)
    plt.savefig("F1D_result.png")
    plt.show()

Plot()

