from cpt import *
from math import *
from numpy import *


class Friedmann :
	w = 0.
	def __init__(self,w):
		self.w = w
	def __call__(self,p):
		t = p[0]
		r = p[1] #this is actually ln(R)
		H = p[2] 
		Hdot = -3.* (1.+self.w) * H**2. /2.
		flow = [1.,H,Hdot]
		return flow

def main ():
	w0 = 0.0
	w1 = 1.0
	w3 = -1./3.
	
	fried1 = Friedmann(w1)
	fried0 = Friedmann(w0)
	fried3 = Friedmann(w3)
	tau0 = 10.0
	tau1 = 10.0
	tau3 = 10.0
	accuracy = 1e-5
	H0 = 7.357e-11 #H0 local in inverse years
	#Initialize Vector
	p0 = [0.0]*3
	p1 = [0.0]*3 #I need one of these per case
	p3 = [0.0]*3
	
	p0[0] = 2./3.* 1/H0  
	p0[1] = 0.0 #We get R(today)=1, so ln(1)=0
	p0[2] = H0 
	
	p1[0] = 2./(3.*(1+w1)) * 1/H0  
	p1[1] = 0.0 #We get R(today)=1, so ln(1)=0
	p1[2] = H0 
		
	p3[0] = 2./(3.*(1+w3)) * 1/H0  
	p3[1] = 0.0 #We get R(today)=1, so ln(1)=0
	p3[2] = H0 

	#* Loop over desired number of steps with given time step
    #    and numerical method
	nStep = 1000

	t_plot0 = []
	R_plot0 = []
	H_plot0 = []

	t_plot1 = []
	R_plot1 = []
	H_plot1 = []

	t_plot3 = []
	R_plot3 = []
	H_plot3 = []
	dt_min0 = tau0
	dt_max0 = tau0
	dt_min1 = tau1
	dt_max1 = tau1
	dt_min3 = tau3
	dt_max3 = tau3
	for  iStep in xrange(nStep) :

        #if ( xv[0] > T ) :
        #    break

        #* Record ln(R) and H for plotting
		
		#try:
		R0 = math.exp(p0[1])
		R1 = math.exp(p1[1])
		R3 = math.exp(p3[1])
		#except OverflowError:
		#	print ("Okay, you've gotten an R that is too big for me, so I'm stopping here, since ",p[1]," is too big.")
		#	break
		t_plot0.append( p0[0] )
		R_plot0.append( R0 )
		H_plot0.append( p0[2] )
		
		t_plot1.append( p1[0] )
		R_plot1.append( R1 )
		H_plot1.append( p1[2] )
		
		t_plot3.append( p3[0] )
		R_plot3.append( R3 )
		H_plot3.append( p3[2] )
     
		tau0 = RK4_adaptive_step(p0, tau0, fried0, accuracy)
		dt_min0 = min(tau0, dt_min0)
		dt_max0 = max(tau0, dt_max0)

		tau1 = RK4_adaptive_step(p1, tau1, fried1, accuracy)
		dt_min1 = min(tau1, dt_min1)
		dt_max1 = max(tau1, dt_max1)
		tau3 = RK4_adaptive_step(p3, tau3, fried3, accuracy)
		dt_min3 = min(tau3, dt_min3)
		dt_max3 = max(tau3, dt_max3)
	import matplotlib
	matplotlib.rcParams['legend.fancybox'] = True
	import matplotlib.pyplot as plt
	
	
	plt.subplot(1,3,1)
	plt.scatter( t_plot1, R_plot1,label='w=1 case')
	plt.xlabel("time (years)")
	plt.ylabel("Universe scale factor (R)")
	plt.title("w=1 case")
	plt.subplot(1,3,2)
	plt.scatter( t_plot0, R_plot0,label='w=0 case')
	plt.xlabel("time (years)")
	plt.ylabel("Universe scale factor (R)")
	plt.title("w=0 case")
	
	plt.subplot(1,3,3)
	plt.scatter( t_plot3, R_plot3,label='w=3 case')
	plt.xlabel("time (years)")
	plt.ylabel("Universe scale factor (R)")
	plt.title("w=-1/3 case")

	plt.show()


if __name__ == "__main__" :
	main()
