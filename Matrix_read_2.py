#Matrix_read_other.py

#matrix with primary and secondary diagonals filled. 

import numpy as np
import pylab as pl

def matrix_gen():#generates a matrix with higher values toward the center.
    m = 4
    H = np.zeros((m, m))
    for n in range(1, m):
        ha = (m - n)/2
        va = ha
        hb = m - n - ha
        vb = hb
        A = np.zeros((n, ha))
        B = np.random.rand(n,n)
        C = np.zeros((n, hb))
        D = np.hstack((A, B, C))
        E = np.zeros((va, m))
        F = np.zeros((vb, m))
        G = np.vstack((E, D, F))
        H = np.add(G, H)
    return H, m

#def data_read():
#    A = []
#    with open('Spinel xmap_3 copy.txt') as f:
#        for j in xrange(31):
#            f.next()
#        for line in f:
#            A.append([])
#            for word in line.split('\t'):
#                intensity = float(word)
#                A[-1].append(intensity)    
#    #print "Dimension: %d x %d" % (len(A), len(A[0]))
#    return A
#
#def data_read_2():
#    A = []
#    with open('Spinel xmap_5 copy.txt') as f:
#        for j in xrange(31):
#            f.next()
#        for line in f:
#            A.append([])
#            for word in line.split('\t'):
#                intensity = float(word)
#                A[-1].append(intensity)    
#    #print "Dimension: %d x %d" % (len(A), len(A[0]))
#    return A

def matrix_gen():#generates a matrix with higher values toward the center.
    m = 4
    H = np.zeros((m, m))
    for n in range(1, m):
        ha = (m - n)/2
        va = ha
        hb = m - n - ha
        vb = hb
        A = np.zeros((n, ha))
        B = np.random.rand(n,n)
        C = np.zeros((n, hb))
        D = np.hstack((A, B, C))
        E = np.zeros((va, m))
        F = np.zeros((vb, m))
        G = np.vstack((E, D, F))
        H = np.add(G, H)
    return H, m

def check_value():
    A = data_read()
    B = data_read_2()
    threshold = 0.1
    pixels = list()
    width = list()
    for i in range(len(A)):
        a = A[i]
        b = B[i]
        c = list()         
        for j in range(len(a)):
            if a[j] > threshold:
                if b[j] > threshold:
                    c.append(j)
        if len(c) > 2:
            
            wide = c[-1] - c[0]#this is wrong. what is the problem? 
        else:
            wide = 10
        width.append((i, wide))
        pixels.append((i, len(c)))
    #print 'number of pixels is ', pixels,'                                      ', 'width is ', width
    return width, pixels
#improve this code by making the threshold alorithum select for only certain ratio (scan for crystals, in this case spinel, which should be a specific ratio of Mg singla to Al signal)

def plotter():
    width, pixels = check_value()
    a, b = zip(*width)
    c, d = zip(*pixels)
    #e = pl.plot(a, b, label = "width")
    f = pl.plot(c, d, label = "spinel abundance")
    pl.legend(loc='upper left')
    pl.show()

plotter()
