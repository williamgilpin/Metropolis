from random import random, randint
from numpy import zeros
from numpy.linalg import eig
from pylab import imshow, show, ion, ioff, draw, scatter, plot
from math import pi, sin, exp, sqrt

T = 10000000
Nx = 100
Ny = 100
b = 1
Temp = 1

def initialize():
	U = zeros([Nx,Ny], float)
	for i in range(Nx):
		for j in range(Ny):
			U[i,j] = f(float(i)/Nx,float(j)/Ny)
	#imshow(U)
	#show()
	return U

def f(x,y):
	r = sqrt((x-.5)**2 + (y-.5)**2)
	#return sin(12*pi*r)
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

def getZone(x,y):
	if x >= Nx//2 and y >= Ny//2:
		return 0
	elif x >= Nx//2 and y < Ny//2:
		return 1
	elif x < Nx//2 and y >= Ny//2:
		return 2
	elif x < Nx//2 and y < Ny//2:
		return 3

def constructMSM(zonelist):
	C = countMatrix(zonelist)
	C = symC(C)
	C = normalize(C)
	return C

def countMatrix(zonelist):
	C = zeros([4,4])
	for i in range(1,len(zonelist)-1):
		indexI = zonelist[i]
		indexJ = zonelist[i+1]
		C[indexI,indexJ] += 1
	return C

def symC(C):
	#symmaterize C
	Csym = zeros([4,4], float)
	for i in range(4):
		for j in range(4):
			Csym[i,j] = 0.5*(C[i,j] + C[j,i])
	return Csym

def normalize(C):
	for i in range(4):
		s = 0.0
		for j in range(4):
			s += C[i,j]
		C[i,:] /= s
	return C

def mainSim():
	traveled = zeros([Nx,Ny], int)
	U =	initialize()
	x = randint(1,Nx-2)
	y = randint(1,Nx-2)
	x = Nx//2
	y = Ny//2
	xtraj = []
	ytraj = []
	zonelist = []
	ion()
	for t in range(T):
		if t%(T/10) == 0:
	#		imshow(traveled, interpolation="nearest")
	#		draw()
			print float(t)/T*100
		zone = getZone(x,y)
		zonelist.append(zone)
		xtraj.append(x)
		ytraj.append(y)	
		traveled[x,y] += 1	
		d = randint(0,3)
		x1,y1 = update(d,x,y)
		U0 = U[x,y]
		U1 = U[x1,y1]
		p = exp(b*(U0-U1))
		if random() < p:
			x,y = x1,y1
	ioff()
	C = constructMSM(zonelist)
	return C

def mainMSM(C):
	w,v = eig(C)
	print w
	for V in v:
		plot(V)
	show()

def main():
	C = mainSim()
	mainMSM(C)
main()
