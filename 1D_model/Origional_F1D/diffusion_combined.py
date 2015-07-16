#diffusion_combined.py

# program structure : (1) static parameters parameters are passed to the next function (2) grid

# modules

import operator as op
import numpy as np
from scipy import shape
import numpy as np
from scipy.sparse import csr_matrix
import matplotlib.pylab as plt
import matplotlib.animation as animation
import scipy as sp
from scipy.sparse import csr_matrix, linalg

# static parameters

def static_parameters():
    L = 0.001 # L = 0.00169 (meters)
    nx = 1000 # Number of steps in space
    nt = 360000 # Number of steps in time
    dt = 1 # Width of the time step (seconds)
    dx = L / ( nx - 1.0 ) # Width of the space step
    T = 1100 # Temperature (Kelvin)
    P = 100 # Pressure (MPa)
    W = 0.04 # Water Concentration (weight percent)
    E = 0.43 # mass selectivity coefficent
    UL = 0 # Left Dirichlet B.C. (y'' + y = 0)
    UR = 1 # Right Boundary condition is Dirichlet B.C: (y'' + y = 0)
    UnL = 0 # Left Neumann B.C.
    UnR = 1 # Left Neumann B.C.
    dif_40 = (np.exp((14.627-17913/T-2.569*P/T)+(35936/T+27.42*P/T)*W))*10**-12 # diffusivity coefficent calculated using Behrens and Zhang's model
    dif_39 = dif_40*(40.0/39.0)**(E/2.0) # diffusivity argon 39 calculated using mass selectivity cofficent
    dif_38 = dif_40*(40.0/38.0)**(E/2.0) # diffusivity argon 38 calculated using mass selectivity cofficent
    dif_37 = dif_40*(40.0/37.0)**(E/2.0) # diffusivity argon 37 calculated using mass selectivity cofficent
    dif_36 = dif_40*(40.0/36.0)**(E/2.0) # diffusivity argon 36 calculated using mass selectivity cofficent
    beta_40 = dif_40*dt/(dx*dx) # stability criteria for argon 40
    beta_39 = dif_39*dt/(dx*dx) # stability criteria for argon 39
    beta_38 = dif_38*dt/(dx*dx) # stability criteria for argon 38
    beta_37 = dif_37*dt/(dx*dx) # stability criteria for argon 37
    beta_36 = dif_36*dt/(dx*dx) # stability criteria for argon 36
    parameters = (L, nx, nt, dt, dx, T, P, W, E, UL, UR, UnL, UnR, dif_40, dif_39, dif_38, dif_37, dif_36, beta_40, beta_39, beta_38, beta_37, beta_36)    
    return parameters

# mesh

def drange(start, stop, step):
     r = start
     while r <= stop:
     	yield r
     	r += step

def mesh():
    gridx = []
    L, nx, dx = op.itemgetter(0,1,4)(static_parameters())
    #gridx = np.empty([nx, 0])
    ["%g" % x for x in drange(0.0, L, dx)]
    for x in drange(0.0, L, dx):
        gridx.append(x+L/(nx*2))
    return gridx

print 'gridx is', mesh()

# boundary condition

def BC_matrix_gen():  
    #Common parameters
    L, nx, nt, dt, dx, UL, UR, UnL, UnR, dif_40, dif_39, dif_38, dif_37, dif_36, beta_40, beta_39, beta_38, beta_37, beta_36 = op.itemgetter(0,1,2,3,4,9,10,11,12,13,14,15,16,17,18,19,20,21,22)(static_parameters())
    bc_40 = np.zeros([nx-2, 1])
    bc_39 = np.zeros([nx-2, 1])
    bc_38 = np.zeros([nx-2, 1])
    bc_37 = np.zeros([nx-2, 1])
    bc_36 = np.zeros([nx-2, 1])    
    #Dirichlet boundary conditions
    bc_40[0] = dif_40*dt*UL/(dx**2)
    bc_39[0] = dif_39*dt*UL/(dx**2)
    bc_38[0] = dif_38*dt*UL/(dx**2)
    bc_37[0] = dif_37*dt*UL/(dx**2)
    bc_36[0] = dif_36*dt*UL/(dx**2)
    bc_40[nx-3] = dif_40*dt*UR/(dx**2)
    bc_39[nx-3] = dif_39*dt*UR/(dx**2)
    bc_38[nx-3] = dif_38*dt*UR/(dx**2)
    bc_37[nx-3] = dif_37*dt*UR/(dx**2)
    bc_36[nx-3] = dif_36*dt*UR/(dx**2)
    #Neumann boundary conditions
    #bc_40[0] = dif_40*dt*-UnL/(dx) #sets N. B. C. left side (40Ar)
    #bc_39[0] = dif_39*dt*-UnL/(dx) #sets N. B. C. left side (39Ar)
    #bc_38[0] = dif_38*dt*-UnL/(dx) #sets N. B. C. left side (38Ar)
    #bc_37[0] = dif_37*dt*-UnL/(dx) #sets N. B. C. left side (37Ar)
    #bc_36[0] = dif_36*dt*-UnL/(dx) #sets N. B. C. left side (36Ar)
    #bc_40[nx-3] = dif_40*dt*UnR/(dx) #sets N. B. C. right side (40Ar)
    #bc_39[nx-3] = dif_39*dt*UnR/(dx)#sets N. B. C. right side (39Ar)
    #bc_38[nx-3] = dif_38*dt*UnR/(dx)#sets N. B. C. right side (39Ar)
    #bc_37[nx-3] = dif_37*dt*UnR/(dx)#sets N. B. C. right side (39Ar)
    #bc_36[nx-3] = dif_36*dt*UnR/(dx)#sets N. B. C. right side (39Ar)    
    #matrix operation for Neumann or Dirichlet B.C.s
    bc_40 = bc_40.T
    bc_39 = bc_39.T
    bc_38 = bc_38.T
    bc_37 = bc_37.T
    bc_36 = bc_36.T
    #calculates the coefficent matrix for the implicent scheme. 
    A = np.delete(np.hstack((np.zeros([nx-2, 1]),np.identity(nx-2))), nx-2, 1)
    B = A + A.transpose() - 2 * np.identity(nx-2)    
    #matrix operations for Neumann or Dirichlet B.C.s
    B = A + A.transpose() - 2 * np.identity(nx-2)
    D_40 = np.identity(nx-2) - (dif_40*dt/dx**2)*B
    D_39 = np.identity(nx-2) - (dif_39*dt/dx**2)*B
    D_38 = np.identity(nx-2) - (dif_38*dt/dx**2)*B
    D_37 = np.identity(nx-2) - (dif_37*dt/dx**2)*B
    D_36 = np.identity(nx-2) - (dif_36*dt/dx**2)*B
    B = A + A.transpose() - 2 * np.identity(nx-2)    
    #Neumann only B. C. s calcs
    #B[0,0] = -1
    #B[nx-3,nx-3] = -1
    #matrix operations for Neumann or Dirichlet B.C.s
    D_40 = np.identity(nx-2) - (dif_40*dt/dx**2)*B
    D_39 = np.identity(nx-2) - (dif_39*dt/dx**2)*B
    D_38 = np.identity(nx-2) - (dif_38*dt/dx**2)*B
    D_37 = np.identity(nx-2) - (dif_37*dt/dx**2)*B
    D_36 = np.identity(nx-2) - (dif_36*dt/dx**2)*B
    D_40_sp = csr_matrix(np.identity(nx-2) - (dif_40*dt/dx**2)*B)
    D_39_sp = csr_matrix(np.identity(nx-2) - (dif_39*dt/dx**2)*B)
    D_38_sp = csr_matrix(np.identity(nx-2) - (dif_38*dt/dx**2)*B)
    D_37_sp = csr_matrix(np.identity(nx-2) - (dif_37*dt/dx**2)*B)
    D_36_sp = csr_matrix(np.identity(nx-2) - (dif_36*dt/dx**2)*B)
    return D_40_sp, D_39_sp, D_38_sp, D_37_sp, D_36_sp, bc_40, bc_39, bc_38, bc_37, bc_36

# intial condition

def initial_condition():
    gridx = mesh()
    L, nx, nt, dt, dx, UL, UR, UnL, UnR = op.itemgetter(0, 1, 2, 3, 4, 9, 10, 11, 12)(static_parameters())
    condition = np.zeros([nx, 2])
    condition[:, 1] = np.array(gridx)
    gridu = []
    for i in gridx:
        if i >= L/2:
            #u = 1.0
            u = 0.0
        else:
            u = 0.0
        gridu.append(u)
    condition[:, 0] = np.array(gridu)
    return condition

# calculation

def Calculator():
    condition = initial_condition()
    nx, nt, UR, UL = op.itemgetter(1, 2, 9, 10)(static_parameters())
    D_40_sp, D_39_sp, D_38_sp, D_37_sp, D_36_sp, bc_40, bc_39, bc_38, bc_37, bc_36 = BC_matrix_gen()
    u_40 = (condition[:, 0])
    #u_39 = (condition[:, 0])
    #u_38 = (condition[:, 0])
    #u_37 = (condition[:, 0])
    #u_36 = (condition[:, 0])
    for timestep in range(0, nt):
        if timestep > 7.71*60.*60.:
        #if u[1000-160]*10. > u[-1]:
            print 'Runtime to finish is ', timestep*dt, ' seconds ', 'or ', timestep*dt/60./60., ' hours.'
        #if u[1] > 0.00001:
        #    print 'Optimal runtime is', timestep*dt, 'seconds.'
            return u, u_sec
        U_40 = u_40
        #U_39 = u_39
        #U_38 = u_38
        #U_37 = u_37
        #U_36 = u_36
        #U_40 = np.delete(U_40, [0, nx-1], axis = 0)
        #U_39 = np.delete(U_39, [0, nx-1], axis = 0)
        #U_38 = np.delete(U_38, [0, nx-1], axis = 0)
        #U_37 = np.delete(U_37, [0, nx-1], axis = 0)
        #U_36 = np.delete(U_36, [0, nx-1], axis = 0)
        U_40 = U_40 + bc_40
        #U_39 = U_39 + bc_39
        #U_38 = U_38 + bc_38
        #U_37 = U_37 + bc_37
        #U_36 = U_36 + bc_36
        U_40 = sp.sparse.linalg.spsolve(D_40_sp, U_40.T).T
        #U_39 = sp.sparse.linalg.spsolve(D_39_sp, U_39.T).T
        #U_38 = sp.sparse.linalg.spsolve(D_38_sp, U_38.T).T
        #U_37 = sp.sparse.linalg.spsolve(D_37_sp, U_37.T).T
        #U_36 = sp.sparse.linalg.spsolve(D_36_sp, U_36.T).T
        u_40 = np.append(np.append(U_40, UR)[::-1], UL)[::-1]
        #u_39 = np.append(np.append(U_39, UR)[::-1], UL)[::-1]
        #u_38 = np.append(np.append(U_38, UR)[::-1], UL)[::-1]
        #u_37 = np.append(np.append(U_37, UR)[::-1], UL)[::-1]
        #u_36 = np.append(np.append(U_36, UR)[::-1], UL)[::-1]
    return u_40#, u_39, u_38, u_37, u_36
    
def Plot():
    u = Calculator()
    u = u[::-1]*4.47058
    x = condition[:, 1]*1000000.
    plt.plot(x, u)
    plt.xlabel('micrometers depth')
    plt.ylabel('argon concentration ppm')
    plt.title('1D system state')
    plt.grid(True)
    #plt.savefig("F1D_result.png")
    plt.autoscale(enable=True, axis='y')
    plt.show()
    return 'sucessfully plotted'

print Plot()