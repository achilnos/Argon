#F1D_BC_Vector.py
#This module contains the script to create a vector "D" containing a Dirichlet boundary condition for this system. 

from F1D_Parameters import nx, dt, dx, UL, UR, UnL, UnR, vis, vis_sec
import numpy as np
from scipy.sparse import csr_matrix
#bc is a coefficent matrix for the implict scheme
bc = np.zeros([nx-2, 1])
bc_sec = np.zeros([nx-2, 1])
#Dirichlet boundary conditions
bc[0] = vis*dt*UL/(dx**2)
bc_sec[0] = vis_sec*dt*UL/(dx**2)
bc[nx-3] = vis*dt*UR/(dx**2)
bc_sec[nx-3] = vis_sec*dt*UR/(dx**2)
bc = bc.T
bc_sec = bc_sec.T
#calculates the coefficent matrix for the implicent scheme. 
A = np.delete(np.hstack((np.zeros([nx-2, 1]),np.identity(nx-2))), nx-2, 1)
# Dirichlet B.C.s
B = A + A.transpose() - 2 * np.identity(nx-2)
D = np.identity(nx-2) - (vis*dt/dx**2)*B
D_sec = np.identity(nx-2) - (vis_sec*dt/dx**2)*B
#print D
#print D_sec