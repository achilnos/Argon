#Image_reader.py

#matrix with primary and secondary diagonals filled. 

import numpy as np
import pylab as pl
from scipy.optimize import curve_fit

class F:
  
  def __call__(self, x, a, b, c):
     return a * np.exp(x + b) + c
     



def data_read():
    A = []
    with open('Spinel xmap_3 copy.txt') as f:
        for j in xrange(31):
            f.next()
        for line in f:
            A.append([])
            for word in line.split('\t'):
                intensity = float(word)
                A[-1].append(intensity)    
    #print "Dimension: %d x %d" % (len(A), len(A[0]))
    return A

def data_read_2():
    A = []
    with open('Spinel xmap_5 copy.txt') as f:
        for j in xrange(31):
            f.next()
        for line in f:
            A.append([])
            for word in line.split('\t'):
                intensity = float(word)
                A[-1].append(intensity)    
    #print "Dimension: %d x %d" % (len(A), len(A[0]))
    return A

def check_value():
    A = data_read()
    B = data_read_2()
    threshold = 50 #sets a minimum intensity in each pixel (relative to the abundance of the element) to be recognized. 
    pixels = []
    width = []
    mainthick = 40 #sets a minimum thickness for the spinel crystal to be recognized as the main spinel fragment. 
    for i in range(len(A)):
        fragment_num = 1 #this variable keeps track of the number of recognized fragments of spinel. 
        crys_slice = [0] #this string holds ints coresponding to the horizontal position of each recognized pixel with a recognized equivalent in the opposing matrix (for the other element) in order or recognition (left to right)
        gap_slice = [] #this strings holds ints corresponding to the horizontal position of each pixel in the most recent gap between spinel crystals. 
        gap_thresh = 100
        for j in range(len(A[i])):
            if A[i][j] > threshold and B[i][j] > threshold:
                crys_slice.append(j)
                print "thershold met"
            else:
                gap_slice.append(j)
                print "threshold fails"
            if len(gap_slice) >= 5 and len(crys_slice) <= gap_thresh/4:
                crys_slice = [0]
                print "gap detected"
                fragment_num = fragment_num + 1
            else:
                mainthick = len(crys_slice)
                gap_thresh = mainthick
        #end the string "c" if it ewncounters
        if len(crys_slice) >= mainthick/4:
            
            wide = max(crys_slice) - min(crys_slice)#this is wrong. what is the problem? 
        else:
            wide = 0 #what does this do?
        width.append((i, wide))
        pixels.append((i, len(crys_slice)))
    #print 'number of pixels is ', pixels,'                                      ', 'width is ', width
    return width, pixels
#improve this code by making the threshold alorithum select for only certain ratio (scan for crystals, in this case spinel, which should be a specific ratio of Mg singla to Al signal)
#improve this code by haveing a thershold for adjacent pixel (ten?) that must be exceeded to counts as a beginning or an end. 

def plotter():
    f = F()
    width, pixels = check_value()
    a, b = zip(*width)
    c, d = zip(*pixels)
    e = pl.plot(a, b, label = "width")
    #f = pl.plot(c, d, label = "spinel")
    #popt, pcov = curve_fit(f.__call__, a, b)
    #g = pl.plot(a, f(a, *popt), 'k-', label = 'fit')
    pl.legend(loc='upper left')
    pl.ylabel('Relative amount of Spinel detected')
    pl.xlabel('Distance from TC end')
    pl.savefig('NW1_spinel')
    pl.show()

plotter()