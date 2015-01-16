# Metropolis
Metropolis Algorithm

define f(x,y) to be a function spanning x = [0,1]  y = [0,1] for the potential energy distribution.

In the example: 
    
    f(x,y) = sin(2*pi*x)*sin(2*pi*y)
    
Giving:

![alt tag](https://raw.githubusercontent.com/twhughes/Metropolis/master/Initial.png)

for T time steps, a particle will do a random walk through the potential, accepting changes in energy with probability exp(-b(dU))
where b = 1/(kT) and dU is the change in energy associated with moving to new grid point.

After a long enough time, the plot of how much time the particle has spent in each location will converge (as shown):

![alt tag](https://raw.githubusercontent.com/twhughes/Metropolis/master/Final.png)

