#stepheat_animation_2

import numpy as np
import matplotlib.pylab as plt
import matplotlib.animation as animation
from scipy import special as special

def run_animate(timestep):
    global a
    global b
    if timestep > nt:
        return None
    else:
        print timestep
    a = np.append(a,x[timestep])
    b = np.append(b,y[timestep])
    graph.set_xdata(a)
    graph.set_ydata(b)
    return graph,

x = np.linspace(0,100,num=100)
u = np.empty(len(x)); u.fill(0.5)
w = -np.random.rand(len(x))/25.0
y = np.add(u,w)
a = np.empty(len(x))
b = np.empty(len(x))
nt = len(x)
fig1 = plt.figure()
graph, = plt.plot(a, b)#change plotsize
plt.xlabel('Time, %39Ar')
plt.ylabel('40Ar/39Ar')
plt.title('Evenly Distributed')
plt.xlim(0,100)
plt.ylim(0,1)
ani = animation.FuncAnimation(fig1, run_animate)
#plt.show()
mywriter = animation.FFMpegWriter()
ani.save('step_heat_flat.mp4', writer=mywriter, fps=30)
exit()

#save(filename, writer=None, fps=None, dpi=None, codec=None, bitrate=None, extra_args=None, metadata=None, extra_anim=None, savefig_kwargs=None)