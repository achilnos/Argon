#F1D_Plot.py
#this script is designed to plot the results from the calculation. I might want to put it inside the calculation loop after I know that it works. 

from pylab import *
from F1D_Initial_Condition import condition

x = condition[:, 1]
u = condition[:, 0]
plot(x, u)
xlabel('distance (x)')
ylabel('Concentration (u)')
title('Test Plot')
grid(True)
#savefig("test.png")
show()