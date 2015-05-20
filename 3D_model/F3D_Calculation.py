#F3D_Calculation.py
#/Users/nicholas/documents/Python/Argon/F1D_Calculation.py
#This script calculates the result of each timestep and plots the result at the final timestep. 
#has been edited to find the time until equilibration for a 3mm length. 

import numpy as np
import matplotlib.pylab as plt
import matplotlib.animation as animation
from F3D_Parameters import nx, nt, UL, UR, dx, UnL, UnR, dt, nx_excess
from F3D_BC_Vector import Dsp, bc
from F3D_Initial_Condition import condition
import scipy as sp
from scipy.sparse import csr_matrix, linalg
from matplotlib import mpl
import matplotlib as m
import matplotlib.colors as mcolors


def threedprojection(u):
    cylinder_width = 1000
    cylinder_length = 1000
    circle_correction =  np.linspace(1.0, 2.0, num=cylinder_width/2)
    circle_correction = np.append(circle_correction, circle_correction[::-1])#is this operation being saved? 
    m = np.empty(cylinder_width)#empty vector representing the width part of the cylinder
    n = np.empty(cylinder_length)#empty vector representing the length part of the cylinder    
    u_tail_m = np.empty(0)
    count = 0
    while len(u) > cylinder_width:
        u_trunc_m, u_tail_m = np.split(u,cylinder_width)
        u = u_tail_m
        if count is even:
            m = m + u_trunc_m
        else:
            m = m + u_trunc_m[::-1]
        count = count + 1
    count = 0
    while len(u) > cylinder_length:
        u_trunc_n, u_tail_n = np.split(u,cylinder_length)
        u = u_tail_n
        if count is even:
            n = n + u_trunc_n
        else:
            n = n + u_trunc_n[::-1]
        count = count + 1
    #for now I am not incorporating the last part of the tail...
    m = (m + m[::-1])*circle_correction#is this multiplication element wise? #is it vertical?
    n = n + n[::-1]
    #construct the state of the cylinder from m and n. efficently pls. 
    A = m
    B = n
    count = 1
    while count < cylinder_width:
        A = np.vstack((A, m))
        count = count + 1
    count = 1
    while count < cylinder_length:
        B = np.vstack((B, n))
        count = count + 1
    #G = (A.T + B)
    G = B
    np.savetxt('G', G, delimiter=' ')
    return G
    
def Calculator():
    u = (condition[:, 0])
    for timestep in range(0, nt):
        print timestep
        if timestep > 8*60*60:
#        if u[nx_excess] > u[nx-9]/100.:#threshold is 99%
#            print 'Runtime to equilibrium is ', timestep*dt, ' seconds ', 'or ', timestep*dt/60./60., ' hours.'
            G = threedprojection(u)
            return u, G
        U = u
        U = np.delete(U, [0, nx-1], axis = 0)
        U = U + bc
        U = sp.sparse.linalg.spsolve(Dsp, U.T).T
        u = np.append(np.append(U, UR)[::-1], UL)[::-1]
        #u = np.append(np.append(U, U[0]-UnL*dx)[::-1], U[nx-3]+UnR*dx)[::-1]
        #G = threedprojection(u)
        print timestep
    return u

def Plot():
    u, G = Calculator()
    print 'G is', G
    print np.amax(G), np.amin(G)
    zvals = G
    # make a color map of fixed colors

    # tell imshow about color map so that only set colors are used
    #img = plt.imshow(zvals)
    img = plt.imshow(zvals,interpolation='nearest')

    # make a color bar
    plt.pcolor(zvals, vmin=0, vmax=0.05)
    plt.colorbar()
    #plt.colorbar(img,cmap=cmap,
    #            norm=norm,boundaries=bounds,ticks=[-5,0,5])

    plt.show()
    
    #x = condition[:, 1]
    #plt.plot(x, u)
    #plt.xlabel('distance (x)')
    #plt.ylabel('Concentration (u)')
    #plt.title('Argon Concentration')
    #plt.grid(True)
    #plt.savefig("F1D_result.png")
    #plt.show()

Plot()



