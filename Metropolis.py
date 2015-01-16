from random import random, randint
from numpy import zeros
from pylab import imshow, show, ion, ioff, draw, scatter, plot
from math import pi, sin, exp

T=300000000
Nx = 100
Ny = 100
b = 1
Temp = 1

def initialize():
	U = zeros([Nx,Ny], float)
	for i in range(Nx):
		for j in range(Ny):
			U[i,j] = f(float(i)/Nx,float(j)/Ny)

	return U

def f(x,y):
	return sin(2*pi*x)*sin(2*pi*y)

def update(d,x,y):
	if d==0 and x+1 < Nx-1:
		return x+1,y
	elif d==1 and x-1 > 1:
		return x-1,y
	elif d==2 and y+1 < Ny-1:
		return x,y+1
	elif d==3 and y-1 > 1:
		return x,y-1
	else:
		return x,y

		
def main():
	traveled = zeros([Nx,Ny], int)
	U =	initialize()
	x = randint(1,Nx-2)
	y = randint(1,Nx-2)
	x = Nx//2
	y = Ny//2
	xtraj = []
	ytraj = []
	for t in range(T):
		print float(t)/T*100
		xtraj.append(x)
		ytraj.append(y)	
		traveled[x,y] += 1	
		d = randint(0,3)
		x1,y1 = update(d,x,y)
		U0 = U[x,y]
		U1 = U[x1,y1]
		p = exp(b*Temp*(U0-U1))
		if random() < p:
			x,y = x1,y1
	#imshow(U)
	#show()
	imshow(traveled)
	#plot(xtraj,ytraj)
	show()

main()
