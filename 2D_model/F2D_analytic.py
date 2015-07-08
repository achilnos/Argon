#diff_2d_rectangular
#the purpose of this program is to produce an animation of diffusion into a 2D rectangluar object. Uses a rectangular boudary that must staify the direlect boundary condition. Next version may use circilar scaling to extend to a cylinder. 
#usegiff maker.me is nessearay. 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.cm as cm
import matplotlib.image as mpimg

incriment = 50

def Calculator(t, threshold, length, width, x, y, d, scaling_vector):
    z_vals = np.empty([width,length])    
    a = np.linspace(1.,width,len(x))#what is a?
    b = np.hstack((a,a[::-1]))#what is b?
    circlescaling = np.linspace(1,width,len(x))
    count_length = -len(y)
    uo = 1
    for y_val in range(len(y)-1):    
        this_y = y[y_val]
        count_width = -len(x)
        for x_val in range(len(x)-1):
            this_x = x[x_val]
            z_vals[this_x,this_y] = (uo/np.sqrt(4.*np.pi*d*t))*(np.exp(np.square(this_x)/(4.*d*t)-np.square(width)/(4.*d*t)) + np.exp(np.square(this_y)/(4.*d*t)-np.square(length)/(4.*d*t)))
            count_width = count_width+1
        count_length = count_length+1 
    #z_vals = z_vals#scaling step to account for surface curvature
    z_vals = (z_vals.T*scaling_vector).T
    z_vals = np.vstack([np.flipud(z_vals), z_vals])#duplication step to save time
    z_vals = np.hstack([np.fliplr(z_vals), z_vals])#duplication step to save time
    return z_vals

def save_image(time_axis, initial_time, threshold, maximum_value, minimum_value, start_time):
    startslice = 400 - start_time
    t = startslice
    endslice = 10000 - start_time
    while t < endslice + 1:
        num = str(t + start_time)
        image_name = 'long' + num
        print image_name, 'has been saved'
        fig1 = plt.figure()
        system_state = time_axis[:,:,t]
        img = plt.imshow(system_state,interpolation='nearest')        
        plt.xlim([0,200])
        plt.ylim([0,200])
        plt.pcolor(system_state, vmin=minimum_value, vmax=maximum_value)
        plt.colorbar()
        t = t + incriment - 1
        plt.savefig(image_name, bbox_inches='tight')
        plt.close()
        
def Plot():    
    threshold = 10000
    length = 50
    width = 3500  
    scaling_vector =  np.empty(width)
    r = 0
    while r < width - 1:
        r = r + 1
        scaling_vector[r] = 1./np.float(width)
    d = 7.9
    x = np.linspace(-width,width,2*width)
    y = np.linspace(-length,length,2*length)
    start_time = 0
    t = start_time
    time_axis = Calculator(t, threshold, length, width, x, y, d, scaling_vector)
    #print 'time_axis shape is ', np.shape(time_axis)
    while t < threshold:
        t = t + incriment - 1
        print 'timestep ', t
        system_state = Calculator(t, threshold, length, width, x, y, d, scaling_vector)
        time_axis = np.dstack((time_axis,system_state))
        #print 'time_axis shape is... ', np.shape(time_axis)
    maximum_value = np.amax(time_axis)
    minimum_value = np.amin(time_axis)    
    save_image(time_axis, t, threshold, maximum_value, minimum_value, start_time)#what is intial time? 
    #plt.show()

Plot()