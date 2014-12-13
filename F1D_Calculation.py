#F1D_Calculation.py
#/Users/nicholas/documents/Python/Argon/F1D_Calculation.py
#This script calculates the result of each timestep and plots the result at the final timestep. 
#has been edited to find the time until equilibration for a 3mm length. 

import numpy as np
import matplotlib.pylab as plt
import matplotlib.animation as animation
from F1D_Parameters import nx, nt, UL, UR, dx, UnL, UnR, dt
from F1D_BC_Vector import Dsp, bc
from F1D_Initial_Condition import condition
import scipy as sp
from scipy.sparse import csr_matrix, linalg

def Calculator():
    u = (condition[:, 0])
    for timestep in range(0, nt):
        if u[1] + u[1]/50. > u[nx-1]:
            print 'Runtime to equilibrium is ', timestep*dt, ' seconds ', 'or ', timestep*dt/60./60., ' hours.'
        #if u[1] > 0.00001:
        #    print 'Optimal runtime is', timestep*dt, 'seconds.'
            return u
        U = u
        U = np.delete(U, [0, nx-1], axis = 0)
        U = U + bc
        U = sp.sparse.linalg.spsolve(Dsp, U.T).T
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

