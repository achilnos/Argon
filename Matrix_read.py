# Program idea: a program that detects spinel and measures it. First, must be able to read the value of each pixel. Second must decide whether or not to save the value of the pixel or not based on a threshold (must be greater than some value for both the magnesium value and the aluminium value). A good way to do this is to: a) read each image into a matrix, b) combine these into a matrix of two element objects (two element strings... tuples?), c) write a code that can take an these string objects and decide whether they are above the threshold. If they are, then the program should d) record the coordinates of the object in the larger matrix (by making a different matrix of ones in those spots and zeros elsewhere, or by making a string of tuples, and subtracting the first object from the last). The trickyest part of the program will be figuring out how to set a good edge requirment, but I can worry about that later. 

#to build this program, start with a trial matrix that represents a simpler version of what the data would look like. I can even just start with the 1 0 matrix that I would end up with in (d). I can start with a matrix with two parralell rows of zeros. 

#matrix with primary and secondary diagonals filled. 

import numpy as np
import types as ty
import linecache as ln
import string

def matrix_gen():#generates a matrix with higher values toward the center.
    m = 9
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
    return H   

matrix_gen()

def data_read():
    x = np.empty(1047) # need this to be the right length
    with open('Spinel xmap_1 copy.txt') as f:
        for i in xrange(33):
            f.next()
            y = ln.getline('Spinel xmap_1 copy.txt', i)
        for line in f:
            x = ln.getline('Spinel xmap_1 copy.txt', line)
            #x = x.translate(None, 't')
            #remove non numbers and convert numbes to float!
            print x
            x = np.vstack((y, x))
    with open('Spinel xmap_1 copy.txt') as f:
        for i in xrange(33):
            f.next()
            y = ln.getline('Spinel xmap_1 copy.txt', i)
            print y
        for line in f:
            z = ln.getline('Spinel xmap_1 copy.txt', line)
            #z = z.translate(None, 't')
            #remove non numbers and convert numbes to float!
            print z
            z = np.array(z)
            z = np.vstack((y, z))
    #3print 'len(x) is ', len(x),# 'len(z) is ', len(z)
    #print 'x is ', x, 'z is ', z
    return x, z

def combine():
    a, b = data_read()
    #print a, b
    #c = np.dstack((a, b))
    #print c
    
combine()
#data_read()
