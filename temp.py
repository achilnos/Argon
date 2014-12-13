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
    print vis, vis_sec
    
KIF_Mag()