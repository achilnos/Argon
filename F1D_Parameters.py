#F1D_Parameters.py
#Use this module to set the parameters for the model. 
#This script hold the parameters for a method to solve 1D Fouriers equation using an upwind scheme with an infite step function centered at zero as the intial condition. 
#Dir should be /Users/Nicholas/Documents/Python/Argon

#Number of steps in space
nx = 4000
#Number of steps in time
nt = 5000
#Width of the time step
dt = 0.001
#Width of the space step
dx = 2 / ( nx - 1.0 )
#With of model/ range of x
#grid = range(0, 2, dx)
#Diffusion coefficent
vis = 0.01
vis_sec = 0.05
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
