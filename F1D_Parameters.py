#F1D_Parameters.py
#Use this module to set the parameters for the model. 
#This script hold the parameters for a method to solve 1D Fouriers equation using an upwind scheme with an infite step function centered at zero as the intial condition. 
#Dir should be /Users/Nicholas/Documents/Python/Argon
#An example of acceptable experimental parameters: L = 0.008 m, nt = 36000 s (10h)
#T = 600C --> vis = 2.66384*10**-11
#T = 700C --> vis = 8.54662*10**-11
#T = 800C --> vis = 2.20661*10**-10
#T = 900C --> vis = 4.84651*10**-10
#If computation can't do it try at 10 or 100 times speed by rasing vis and lowing nt. Currently at 100 times

import numpy as np

def KIF_Mag():
    #Temperature (Kelvin)
    T = 1000
    #Pressure (MPa)
    P = 1000
    #Water Concentration (weight percent)
    W = 0.1669364
    #mass slection coefficent
    E = 0.43
    vis = (np.exp((14.627-17913/T-2.569*P/T)+(35936/T+27.42*P/T)*W))*10**-12
    vis_sec = vis*(40.0/36.0)**(E/2.0)
    return vis, vis_sec

#Length of System
L = 0.008
#Number of steps in space
nx = 100
#Number of steps in time
nt = 36000
#Width of the time step (what are the units for this?)
dt = 0.1
#Width of the space step
dx = L / ( nx - 1.0 )
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
UR = 1
#Left Neumann B.C.
UnL = 1
#Left Neumann B.C.
UnR = 1

