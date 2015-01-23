from random import randint, random
from math import exp
from numpy import zeros, size, sum
import numpy as np
from pylab import ion, draw, imshow, plot, show

b = 1
L = 300
T = 1000000
J = 1
H = 0

def setup():
	g = zeros([L,L], float)
	for i in range(L):
		for j in range(L):
			g[i,j] = randint(0,1)
			g[i,j] -= 0.5
			g[i,j] *= 2.5
			g[i,j] = int(g[i,j])

	#print g
	#imshow(g, interpolation="nearest", cmap='hot')
	#show()
	return g

def E(grid):
	U = 0.0
	U -= J*np.sum( grid[1:L-1,1:L-1]*grid[0:L-2,1:L-1]+ grid[1:L-1,1:L-1]*grid[2:L,1:L-1] + grid[1:L-1,1:L-1]*grid[1:L-1,0:L-2] + grid[1:L-1,1:L-1]*grid[1:L-1,2:L] )
	#for i in range(1,L-1):
#		for j in range(1,L-1):#
#			c = grid[i,j]
#			U -= J*c*grid[i+1,j]
#			U -= J*c*grid[i-1,j]
#			U -= J*c*grid[i,j+1]
#			U -= J*c*grid[i,j-1]
#			U -= H*grid[i,j]
	return U

def main():
	ion()
	g = setup()
	#print E(g)
	for t in range(T):
		U0 = E(g)
		x = randint(1,L-1)
		y = randint(1,L-1)
		g1 = g.copy()
		g1[x,y] *= -1
		U1 = E(g1)
		if U1 < U0:
			g = g1.copy()
		elif random() < exp(-b*(U1-U0)):
			g = g1
		if t%(T/100) == 0:
			imshow(g, interpolation="nearest", cmap='winter')
			draw()
main()
