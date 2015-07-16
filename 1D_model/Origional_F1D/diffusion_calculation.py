#diffusion_calculation.py
#/Users/nicholas/documents/Python/Argon/F1D_Calculation.py
#This script calculates the result of each timestep and plots the result at the final timestep. 
#has been edited to find the time until equilibration for a 3mm length. 

import numpy as np
import matplotlib.pylab as plt
import matplotlib.animation as animation
from F1D_Parameters import nx, nt, UL, UR, dx, UnL, UnR, dt
from F1D_BC_Vector import Dsp, bc, bc_sec, D_secsp
from F1D_Initial_Condition import condition
import scipy as sp
from scipy.sparse import csr_matrix, linalg

def Calculator():
    u = (condition[:, 0])
    u_sec = condition[:, 0]
    for timestep in range(0, nt):
        if timestep > 7.71*60.*60.:
        #if u[1000-160]*10. > u[-1]:
            print 'Runtime to finish is ', timestep*dt, ' seconds ', 'or ', timestep*dt/60./60., ' hours.'
        #if u[1] > 0.00001:
        #    print 'Optimal runtime is', timestep*dt, 'seconds.'
            return u, u_sec
        U = u
        U_sec = u_sec
        U = np.delete(U, [0, nx-1], axis = 0)
        U_sec = np.delete(U_sec, [0, nx-1], axis = 0)
        U = U + bc
        U_sec = U_sec + bc_sec
        U = sp.sparse.linalg.spsolve(Dsp, U.T).T
        U_sec = sp.sparse.linalg.spsolve(D_secsp, U_sec.T).T
        u = np.append(np.append(U, UR)[::-1], UL)[::-1]
        u_sec = np.append(np.append(U_sec, UR)[::-1], UL)[::-1]
    return u, u_sec

def Plot():
    u, u_sec = Calculator()
    u = u[::-1]*4.47058
    u_sec = u_sec[::-1]*2.17143
    x = condition[:, 1]*1000000.
    plt.plot(x, u)
    plt.plot(x, u_sec)
    plt.xlabel('micrometers depth')
    plt.ylabel('argon concentration ppm')
    plt.title('Zhang and measured D ranges')
    plt.grid(True)
    plt.savefig("F1D_result.png")
    plt.autoscale(enable=True, axis='y')
    plt.show()

Plot()

