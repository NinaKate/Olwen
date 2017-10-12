from cpt import *
from math import *
from numpy import array


class Friedmann :
	w = 0.
	def __init__(self,w):
		self.w = w
	def __call__(self,p):
		t = p[0]
		r = p[1] #this is actually ln(R)
		H = p[2] 
		Hdot = -3/2 * (1+self.w) * H**2
		flow = [1,H,Hdot]
		return flow

def main ():
	w = float(input("Enter equation of state parameter w: "))
	fried = Friedmann(w)
	tau = float(input(" Enter step size dt: "))
	accuracy = float(input(" Enter desired accuracy for adaptive integration: "))
	H0 = 7.357e-11 #H0 local in inverse years
	#Initialize Vector
	p = [0.0]*3
	
	p[0] = 2./3. * 1/H0 #I'm ignoring the w dependance here for now? 
	p[1] = 0.0 #We get R(today)=1, so ln(1)
	p[2] = H0 

	#* Loop over desired number of steps with given time step
    #    and numerical method
	nStep = int(input( "Enter number of time steps: " ))

	t_plot = []
	R_plot = []
	H_plot = []
	dt_min = tau
	dt_max = tau
    
	for  iStep in xrange(nStep) :

        #if ( xv[0] > T ) :
        #    break

        #* Record ln(R) and H for plotting
		
		try:
			R = math.exp(p[1])
		except OverflowError:
			print ("Okay, you've gotten an R that is too big for me, so I'm stopping here, since ",p[1]," is too big.")
			break
		t_plot.append( p[0] )
		R_plot.append( R )
		H_plot.append( p[2] )

     
		tau = RK4_adaptive_step(p, tau, fried, accuracy)
		dt_min = min(tau, dt_min)
		dt_max = max(tau, dt_max)
	import matplotlib
	matplotlib.rcParams['legend.fancybox'] = True
	import matplotlib.pyplot as plt

	plt.scatter( t_plot, R_plot )

	plt.show()


if __name__ == "__main__" :
	main()
