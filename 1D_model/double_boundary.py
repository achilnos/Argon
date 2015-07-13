#representing 1D diffusion from two opposite sides. 

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.cm as cm
import matplotlib.image as mpimg

#currently, it appears that the resulting array from the caluclation must be normalized to a fixed value at the edge!

incriment = 40000

def Calculator(t, threshold, width, x, d):
    y_vals = np.empty([width*2])    
    uo = 10
    d = d#*10.**-12
    for x_val in range(len(x)-1):
        this_x = x[x_val]
        y_vals[this_x] = (uo/np.sqrt(4.*np.pi*d*t))*(np.exp(np.square(np.float(this_x)-np.float(width))/(4.*d*t)))
    return y_vals

def save_image(time_axis, initial_time, threshold, maximum_value, minimum_value, start_time, width):
    slice = 1#sets start value to select timesteps to make into images. 
    shape_time = np.shape(time_axis)#set end value for last timestep to be made into an image. 
    while slice <  shape_time[1]:
        num = str(slice + start_time)
        image_name = 'fig_double_' + num
        print image_name, 'has been saved'
        fig1 = plt.figure()
        system_state = time_axis[:,slice]
        plt.plot(np.linspace(0,len(system_state),len(system_state)), system_state)#need to change command to reflect new data format.        
        plt.xlim([0,width*4])
        plt.ylim([0,0.1])
        slice = slice + 1 
        plt.savefig(image_name, bbox_inches='tight')
        plt.close()
        
def Plot():    
    threshold = 1000000000
    width = 100  
    d = 1.86#micrometers squared per second. Based on TZMW8
    x = np.linspace(0,width*2,width*2)
    start_time = 1
    t = start_time
    time_axis = Calculator(t, threshold, width, x, d)
    while t < threshold:
        t = t + incriment
        print 'timestep ', t
        system_state = Calculator(t, threshold, width, x, d)
        time_axis = np.vstack((time_axis,system_state))
    maximum_value = np.amax(time_axis)
    minimum_value = np.amin(time_axis)    
    save_image(time_axis, t, threshold, maximum_value, minimum_value, start_time, width)
    
Plot()