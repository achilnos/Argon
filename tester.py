#tester
#script testing file; current: an animation script

import numpy as np
from scipy import shape
import matplotlib.pylab as plt
import matplotlib.animation as animation
from F1D_Parameters import nx, nt, UL, UR, dx, UnL, UnR
from F1D_BC_Vector import D, D_sec, bc
from F1D_Initial_Condition import condition


def En_Calc(timestep):
    global n
    global u
    global u_sec
    global nt
    global en_data
    i = 0
    while (i < nt + 1):
        i = i + 1
        U = u
        U_sec = u_sec
        U = np.delete(U, [0, nx-1], axis = 0)
        U_sec = np.delete(U_sec, [0, nx-1], axis = 0)
        U = U + bc
        U_sec = U_sec + bc
        U = np.linalg.solve(D, U.T).T
        U_sec = np.linalg.solve(D_sec, U_sec.T).T
        u = np.append(np.append(U, UR)[::-1], UL)[::-1]
        u_sec = np.append(np.append(U_sec, UR)[::-1], UL)[::-1]
        en_data = np.vstack((en_data, abs(u-u_sec)))
    return en_data

#f = open('enrichment_data', 'a')#opens this file for appending new data to end. 
x = condition[:, 1]
u = condition[:, 0]
u_sec = condition[:, 0]
en_data = np.zeros(len(condition))
fig1 = plt.figure()
line1, line2, line3 = plt.plot(x, u, 'b-', x, u_sec, 'r-', x, en_data, 'y-')
plt.xlabel('Distance (x)')
plt.ylabel('Concentration (u)')
plt.title('Argon Isotope Concentrations')
ani = animation.FuncAnimation(fig1, En_Calc)
en_data = En_Calc(nt)
print shape(en_data)