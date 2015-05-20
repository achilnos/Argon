#F1D_Ar_Mass

from scipy import shape
import numpy as np
from numpy import loadtxt
import matplotlib.pylab as plt
from F1D_Parameters import dx
from F1D_Initial_Condition import condition

def Ar_con(Ar40, Ar36, x):
    afrac = 0.00337 
    bfrac = 0.996
    Cin = 350.0
    Cain = Cin*afrac
    Cbin = Cin*bfrac
    Caev = Ar36*Cain
    Cbev = Ar40*Cbin
    return Caev, Cbev

#numpy.trapz(y, x=None, dx=1.0, axis=-1)

def Ar_mass():
    Arforty = np.loadtxt('Ar40','float',)
    Arthirtysix = np.loadtxt('Ar36','float',)
    a = Arforty[13672,:]
    b = Arthirtysix[13672,:]
    Ar40 = a[1:len(a)]
    Ar36 = b[1:len(b)]
    c = condition[:, 1]
    x = c[1:len(b)]
    r = 0.0025
    e = 4
    f = 2
    Caev, Cbev = Ar_con(Ar40, Ar36, x)
    Mass36 = np.pi*r**2*np.trapz(Caev[len(Caev)/e:len(Caev)/f])/39.948#correct for isotope...
    Mass40 = np.pi*r**2*np.trapz(Cbev[len(Caev)/e:len(Caev)/f])/39.948
    print 'the amount of 36Ar in a subsection from ', 1./e, 'to ', 1./f,' is ', Mass36, ' mM', 'the amount of 36Ar in a subsection from ', 1./e, 'to ', 1./f,' is ', Mass40, ' mM'
    
Ar_mass()
