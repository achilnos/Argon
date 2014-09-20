#F1D_Enrichment_Calc.py

import numpy as np
import matplotlib.pylab as plt
import matplotlib.animation as animation
from F1D_Parameters import nx, nt, UL, UR, dx, UnL, UnR
from F1D_BC_Vector import Dsp, D_secsp, bc, bc_sec
from F1D_Initial_Condition import condition
import scipy as sp
from scipy.sparse import csr_matrix, linalg
#from F1D_Calculation import 

def Calculator(vis, vis_sec):
    u = (condition[:, 0])
    u_sec = condition[:, 0]
    for timestep in range(0, nt):
        if u[1] > 0.00001:
            print 'Optimal runtime is', timestep, 'seconds.'
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

def Plot(vis, vis_sec):
    u, u_sec = Calculator(vis, vis_sec)
    x = condition[:, 1]
    plt.plot(x, u, 'b-', x, u_sec, 'r-')
    plt.xlabel('distance (x)')
    plt.ylabel('Concentration (u)')
    plt.title('Argon Concentration')
    plt.grid(True)
    plt.savefig("F1D_result.png")
    plt.show()

def KIF_Mag():
    #Temperature (Kelvin)
    T = 1100
    #Pressure (MPa)
    P = 1000
    #Water Concentration (weight percent)
    W = 0.1669364
    #mass slection coefficent
    E = 0.1
    vis = (np.exp((14.627-17913/T-2.569*P/T)+(35936/T+27.42*P/T)*W))*10**-12
    vis_sec = vis*(40.0/36.0)**(E/2.0)
    return vis, vis_sec
    
vis, vis_sec = KIF_Mag()
Plot(vis,vis_sec)