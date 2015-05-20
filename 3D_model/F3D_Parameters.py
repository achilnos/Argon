#F3D_Parameters.py
#Use this module to set the parameters for the model. 
#This script hold the parameters for a method to solve 1D Fouriers equation using an upwind scheme with an infite step function centered at zero as the intial condition. 
#Dir should be /Users/Nicholas/Documents/Python/Argon/F3D_[filename]
#parameters are currently set for RLS-40 (Macdonald et al_USGS_Prof_Paper 1523_1992_App)

import numpy as np

def KIF_Mag():
    #Temperature (Kelvin)
    T = 1423.15#less than 1150C or 1423.15 Kelvin is desireable
    #Pressure (MPa)
    P = 150#less than 150 MPa or 1.5 Kilobar is desireable
    #Water Concentration (weight percent)
    W = 0.04
    #mass slection coefficent
    E = 0.43
    vis = (np.exp((14.627-17913/T-2.569*P/T)+(35936/T+27.42*P/T)*W))*10**-12
    vis_sec = vis*(40.0/36.0)**(E/2.0)
    return vis, vis_sec


#the thrshold depth in meters
depth = 0.005
# the excess portion of the grid
excess = 0.002
#Length of System in meters #for system of 0.005. Using longer to avoid boundary condition problem. 
L = depth + excess
#Number of steps in space
nx = 500#1000
#Number of steps in time
nt = 600000
#Width of the time step in seconds
dt = 20
#Width of the space step
dx = L / ( nx - 1.0 )
#Calculation for the threshold value of the grid
a = np.array([[1,1],[1,-(excess/depth)]])
b = np.array([(excess+depth)/dx,0])
c = np.linalg.solve(a,b)
nx_excess = c[0]
nx_depth = c[1]
#Diffusion coefficent
vis, vis_sec = KIF_Mag()
#vis = 2.66384*10**-9
#vis_sec = 2.0*10**-9
#stability criterion
beta = vis*dt/(dx*dx)
beta_sec = vis*dt/(dx*dx)
#Left Dirichlet B.C. (y'' + y = 0)
UL = 0
#Right Boundary condition is Dirichlet B.C: (y'' + y = 0)
UR = 0.075998883
#Left Neumann B.C.
UnL = 0
#Left Neumann B.C.
UnR = 0.075998883

