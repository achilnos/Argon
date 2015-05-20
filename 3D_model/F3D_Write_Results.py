#F3D_Write_Results.py

import numpy as np
import matplotlib.pylab as plt
import matplotlib.animation as animation
from F3D_Parameters import nx, nt, UL, UR, dx, UnL, UnR
from F3D_BC_Vector import Dsp, D_secsp, bc, bc_sec
from F3D_Initial_Condition import condition
import scipy as sp
from scipy import shape
from scipy.sparse import csr_matrix, linalg
from decimal import *
getcontext().prec = 50
def En_Calc():
    global n
    global u
    global u_sec
    global nt
    global en_data
    i = 0
    u = (condition[:, 0])
    u_sec = (condition[:, 0])
    while (i < nt):
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
        Ar40[i,:] = u
        Ar36[i,:] = u_sec
        en_data[i,:] = u-u_sec
        i = i + 1
    return en_data, Ar40, Ar36

en_data = np.empty([nt, len(condition)])
Ar40 = np.empty([nt, len(condition)])
Ar36 = np.empty([nt, len(condition)])
en_data, Ar40, Ar36 = En_Calc()
#for line in en_data:
#    for num in line:
#        num = Decimal(num)
#        print num
np.savetxt('enrichment_result', en_data, delimiter=' ')
np.savetxt('Ar40', Ar40, delimiter=' ')
np.savetxt('Ar36', Ar36, delimiter=' ')
np.savetxt('Final 36Ar', Ar36[13672,:], delimiter=' ')
exit()