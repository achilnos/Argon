#Plot.py
#plots a specific timestep from a text file
from scipy import shape
import numpy as np
from numpy import loadtxt
from F1D_Initial_Condition import condition
import matplotlib.pylab as plt

Arforty = np.loadtxt('Ar40','float',)
Arthirtysix = np.loadtxt('Ar36','float',)

def enrich_cor(Ar40, Ar36, x):
    #afrac is the initial fraction of 36Ar in the argon enriched couple at the begining of the experiment. Currently using atmospheric argon values. 
    afrac = 0.00337
    #bfrac is the initial fraction of 40Ar in the argon enriched couple at the begining of the experiment. Currently using atmospheric argon values. 
    bfrac = 0.996
    #Cin is the intial cocentration of argon per unit length in the enriched diffusion couple. In this formulation this is in parts per million. Using 350 ppm
    #Cin = 350.0
    #print 'Cin is ', Cin
    #Rin is the ratio of 36 to 40 Ar (initial)
    Rin = afrac/bfrac
    #print 'Rin is ', Rin
    #Cain is the initial concentration of argon 36 in the DC (ppm). 
    #Cain = Cin*afrac
    #print 'Cain is ', Cain
    #Cbin is the initial concentration of argon 40 in the DC (ppm). 
    #Cbin = Cin*bfrac
    #print 'Cbin is ', Cbin
    #Caev is the evolved conentration of argon 36 at some point in x and t during the experiment.
    Faev = Ar36*afrac
    #print 'Faev is ', Faev
    #print 'Faev shape is', shape(Faev)
    #Caev is the evolved conentration of argon 36 at some point in x and t during the experiment.
    Fbev = Ar40*bfrac
    #print 'Fbev is ', Fbev
    #print 'Fbev shape is', shape(Fbev)
    #Rev is the evolved ratio of 36Ar to 40Ar along the x axis at a particular timstep.
    Rev = Faev/Fbev#invalid value encountered in divide
    #print 'Rev is ', Rev
    #e is the enrichment (del) relative to atmospheric in per mil. 
    permil = (Rev/Rin-1)/Rin*1000.0
    #print 'e is ', e
    return permil

def Plot():    
    a = Arforty[3000,:]
    b = Arthirtysix[3000,:]
    Ar40 = a[1:len(a)]
    Ar36 = b[1:len(b)]    
    c = condition[:, 1]
    x = c[1:len(b)]
    e = enrich_cor(Ar40, Ar36, x)
    #plt.plot(x, Ar40, 'b-', x, Ar36, 'r-')
    plt.plot(x, e)
    plt.xlabel('distance (x)')
    plt.ylabel('Enrichment 36Ar (permil)')
    plt.title('Ar isotope enrichment')
    plt.grid(True)
    #plt.savefig("F1D_result.png")
    plt.show()

Plot()
