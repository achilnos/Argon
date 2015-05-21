#diff_2d_rectangular
#usegiff maker.me is nessearay. 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.cm as cm
import matplotlib.image as mpimg


def Calculator(t, threshold, length, width, x, y, d):
    z_vals = np.empty([width,length])    
    a = np.linspace(1.,width,len(x))
    b = np.hstack((a,a[::-1]))
    print b
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
    return z_vals    

def save_image(time_axis, initial_time, threshold, maximum_value, minimum_value):
    t = 0
    while t < threshold-initial_time:
        num = str(t)
        image_name = 'timestep' + num
        print image_name
        fig1 = plt.figure()
        system_state = time_axis[:,:,t]
        img = plt.imshow(system_state,interpolation='nearest')
        plt.autoscale(img)
        plt.pcolor(system_state, vmin=minimum_value, vmax=maximum_value)
        plt.colorbar()
        t = t + 1
        plt.savefig(image_name, bbox_inches='tight')
        
def Plot():    
    threshold = 200
    length = 50
    width = 50
    d = 7.9
    x = np.linspace(-width,width,2*width)
    y = np.linspace(-length,length,2*length)
    t = 199
    time_axis = Calculator(t, threshold, length, width, x, y, d)
    while t < threshold:
        t = t+1
        system_state = Calculator(t, threshold, length, width, x, y, d)
        time_axis = np.dstack((time_axis,system_state))
    t = 80
    maximum_value = np.amax(time_axis)
    minimum_value = np.amin(time_axis)    
    save_image(time_axis, initial_time, threshold, maximum_value, minimum_value)
    #plt.show()

Plot()