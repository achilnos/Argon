#diff_2D_square.py
#the purpose of this program is to produce an animation of diffusion into a 2D rectangluar object. Uses a rectangular boudary that must staify the direlect boundary condition. Next version may use circilar scaling to extend to a cylinder. 
#note: 1*10**-12 meters squared per second equals 1 micrometers squared per second. Recommend this model treats each grid cell as 1 micrometer and keep diffusion in micrometers squared per second.  
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.cm as cm
import matplotlib.image as mpimg

#currently, it appears that the resulting array from the caluclation must be normalized to a fixed value at the edge!

incriment = 100

def Calculator(t, threshold, length, width, x, y, d, scaling_vector):
    z_vals = np.empty([width,length])    
    a = np.linspace(1.,width,len(x))
    b = np.hstack((a,a[::-1]))
    circlescaling = np.linspace(1,width,len(x))
    count_length = -len(y)
    uo = 10
    d = d#*10.**-12
    for y_val in range(len(y)-1):    
        this_y = y[y_val]
        count_width = -len(x)
        for x_val in range(len(x)-1):
            this_x = x[x_val]
            z_vals[this_x,this_y] = (uo/np.sqrt(4.*np.pi*d*t))*(np.exp(np.square(this_x)/(4.*d*t)-np.square(width)/(4.*d*t)) + np.exp(np.square(this_y)/(4.*d*t)-np.square(length)/(4.*d*t)))
            count_width = count_width+1
        count_length = count_length+1 
    z_vals = (z_vals.T*scaling_vector).T#scaling to account for effect of surface curvature
    z_vals = np.vstack([np.flipud(z_vals), z_vals])#duplication step to save time
    z_vals = np.hstack([np.fliplr(z_vals), z_vals])#duplication step to save time
    return z_vals

def save_image(time_axis, initial_time, threshold, maximum_value, minimum_value, start_time, length, width):
    slice = 1#sets start value to select timesteps to make into images. 
    shape_time = np.shape(time_axis)#set end value for last timestep to be made into an image. 
    while slice <  shape_time[2]:
        num = str(slice + start_time)
        image_name = 'square_' + num
        print image_name, 'has been saved'
        fig1 = plt.figure()
        system_state = time_axis[:,:,slice]
        img = plt.imshow(system_state,interpolation='nearest')        
        plt.xlim([0,length*2])
        plt.ylim([0,width*2])
        plt.pcolor(system_state, vmin=minimum_value, vmax=maximum_value)
        plt.colorbar()
        slice = slice + 1 
        plt.savefig(image_name, bbox_inches='tight')
        plt.close()
        
def Plot():    
    threshold = 5000
    length = 100
    width = 100  
    scaling_vector =  np.empty(width)
    r = 0
    while r < width - 1:
        r = r + 1
        scaling_vector[r] = 1.
    d = 1.86#micrometers squared per second. Based on TZMW8
    x = np.linspace(-width,width,2*width)
    y = np.linspace(-length,length,2*length)
    start_time = 0
    t = start_time
    time_axis = Calculator(t, threshold, length, width, x, y, d, scaling_vector)
    while t < threshold:
        t = t + incriment
        print 'timestep ', t
        system_state = Calculator(t, threshold, length, width, x, y, d, scaling_vector)
        time_axis = np.dstack((time_axis,system_state))
    maximum_value = np.amax(time_axis)
    minimum_value = np.amin(time_axis)    
    save_image(time_axis, t, threshold, maximum_value, minimum_value, start_time, length, width)#what is intial time? 

Plot()