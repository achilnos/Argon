#F1D_Parameters.py
#Use this module to set the parameters for the model. 
#This script hold the parameters for a method to solve 1D Fouriers equation using an upwind scheme with an infite step function centered at zero as the intial condition. 
#Dir should be /Users/Nicholas/Documents/Python/Argon
#An example of acceptable experimental parameters: L = 0.008 m, nt = 36000 s (10h)
#T = 700C --> vis = 8.54662*10**-11
#T = 800C --> vis = 2.20661*10**-10
#T = 900C --> vis = 4.84651*10**-10

#Length of System
L = 0.008
#Number of steps in space
nx = 4000
#Number of steps in time
nt = 3600
#Width of the time step
dt = 0.01
#Width of the space step
dx = L / ( nx - 1.0 )
#With of model/ range of x
#grid = range(0, 2, dx)
#Diffusion coefficent
vis = 8.54662*10**-11
vis_sec = 9.0*10**-11
#stability criterion
beta = vis*dt/(dx*dx)
beta_sec = vis_sec*dt/(dx*dx)
#Left Dirichlet B.C. (y'' + y = 0)
UL = 0
#Right Boundary condition is Dirichlet B.C: (y'' + y = 0)
UR = 1
#Left Neumann B.C.
UnL = 1
#Left Neumann B.C.
UnR = 1
