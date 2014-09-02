#F1D_Enrichment_Calc.py
#Use this module to get data from the Calculation and Animation modules for two different diffusivities, then plot them together (normalized to 1: being the starting concentration of the isotope) and animate them together. More importantly, this needs to subtract the two isotope concnetration gradients in order to define the enrichment along the (long) x-axis of the experiment. I would also like to put the "stop" at a point where the diffusion reaches the end of the grid, so It will automatically give the ned result that I need. 

import numpy as np
import matplotlib.pylab as plt
import matplotlib.animation as animation
from F1D_Parameters import nx, nt, UL, UR, dx, UnL, UnR
from F1D_BC_Vector import D, D_sec, bc
from F1D_Initial_Condition import condition


def run_animate_two(timestep):
    global u
    global u_sec
    global nt
    if timestep > nt:
        return None
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
    line1.set_ydata(u)
    line2.set_ydata(u_sec)
    return line1, line2

x = condition[:, 1]
u = condition[:, 0]
u_sec = condition[:, 0]
fig1 = plt.figure()
line1, line2 = plt.plot(x, u, x, u_sec, 'r-')
plt.xlabel('Distance (x)')
plt.ylabel('Concentration (u)')
plt.title('Argon Isotope Concentrations')
ani = animation.FuncAnimation(fig1, run_animate_two)
plt.show()
exit()
