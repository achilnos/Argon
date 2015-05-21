from scipy import misc as sc
from scipy import special as sp
import numpy as np


#test
#the purpose of the snipit is to test the syntax of my forumation for the analytic solution to the diffusion equation in cylinder (radial component, so polar) to m = 6. The accuracy of this solution is limited by the number of terms used in the series. Since the first six values of beta are availible, I will use a sixth order approximation, which should be pretty accurate. lambda is not ideal because of use of infinite series. 
#I think that kappa is the diffusivity
# to integrate r, use a vertical vector containing the values for are in the grid, and sum comlum wise while conserving rows. 

def J_fun(x, alpha, threshold):
    m = 0
    series = []
    while m < threshold:
        y = np.power(-1,m)/(sc.factorial(m)*sp.gamma(m+alpha+1))*np.power(x/2,2*m+alpha)
        m = m + 1
        series = np.hstack((series, y))
    return np.sum(series) 

def radial(n, t, a, beta, T, threshold_j):
    r = 0.05
    print t
    radial_state = []
    while r < a:
        y = np.sum(np.exp(-np.power(beta[n],2)*T)*(J_fun(r*beta[n]/a, 0, threshold_j))/(beta[n]*J_fun(beta[n], 1, threshold_j)))
        radial_state = np.append(radial_state,y)
        r = r + 0.1
    return radial_state

def solution(t,threshold_t):
    kappa = 1 #diffusivity coefficent
    a = 10 #radius at the surface of the cylinder
    grid_num = 10
    beta = np.array([2.4048, 5.5201, 8.6537, 11.7915, 14.9309, 18.0711])
    threshold_j = 20
    threshold_f = len(beta)
    x = 2
    n = 0
    series = np.empty([threshold_f,100])
    T = (kappa*t)/np.power(a,2)
    while n < threshold_f:
        k = radial(n, t, a, beta, T, threshold_j)
        n = n + 1
        series = np.vstack((series, k.T))
    return series

#print 'solution shape is', np.shape(solution(1, 200))#time is passed to function here

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
    initial_time = 195
    t = initial_time
    time_axis = solution(t)
    while t < threshold:
        t = t+1
        system_state = solution(t)
        time_axis = np.dstack((time_axis,system_state))
    t = 80
    maximum_value = np.amax(time_axis)
    minimum_value = np.amin(time_axis)    
    save_image(time_axis, initial_time, threshold, maximum_value, minimum_value)        

    #plt.show()

#Plot()

#next get vector for all r. Attached to the timelooping function constructed for the 2d model. 
