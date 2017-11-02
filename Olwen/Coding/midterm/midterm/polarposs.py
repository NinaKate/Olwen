from cpt import *
from math import *
import time

class Poisson :
    def __init__ (self, L=60):
        self.L = L                   # number of interior points in x and y
        self.omega = 1.88177         # over-relaxation parameter for L = 50
        self.N = L + 2               # interior plus two boundary points
        N=self.N
        self.V = Matrix(N, N)    # potential to be found
        self.rho = Matrix(N, N)  # given charge density
        self.VNew = Matrix(N, N) # new potential after each step
        self.hx = 30.0 / (L + 1)       # lattice spacing assuming size in x=30
        self.hy = 30.0/ (L+1)            #lattice spacing in y for y size =30
        self.q = -10.0                # point charge for particle trajectory
        self.cent= N / 2                    # center of lattice
        self.V0 = 1
        self.Fx = Matrix(N,N)
        self.Fy = Matrix(N,N)
    def equipot(self):
        for i in range(1, self.L+1):
            x = (i-self.cent)*hx
            for j in range(1, self.L+1):
                y = (j-self.cent)*hy
                r = math.sqrt(x**2+y**2)
                if (r-10.0)**2 <0.1:
                    VNew[j][i] = 5.0
                if (r-5.0)**2 <0.1:
                    VNew[j][i] = -3.0
    def Jacobi(self):# Jacobi algorithm for a single iterative step
        VNew = self.VNew
        
        V    = self.V         #avoid lots of typing
        rho  = self.rho
        V0 = self.V0
        for i in range(1, self.L+1):
            for j in range(1, self.L+1):
                VNew[i][j] = 0.25 * (V[i-1][j] + V[i+1][j] +
                                     V[i][j-1] + V[i][j+1] )
        for i in range(1, self.L+1):
            x = (i-self.cent)*self.hx
            for j in range(1, self.L+1):
                y = (j-self.cent)*self.hy
                r = math.sqrt(x**2+y**2)
                if (r-10.0)**2 <0.01:
                    VNew[j][i] = 5.0
                if (r-5.0)**2 <0.01:
                    VNew[j][i] = -3.0



    def GaussSeidel(self):          # Gauss-Seidel algorithm for one iterative step
        L = self.L
        VNew = self.VNew
        V    = self.V         #avoid lots of typing
        rho  = self.rho
        
        
        # copy V to VNew
        for i in range(1, self.L+1):
            for j in range(1, self.L+1):
                VNew[i][j] =  V[i][j]
    
        # perform Gauss-Seidel update
        for i in range(1, self.L+1):
            for j in range(1, self.L+1):
                VNew[i][j] = 0.25 * (VNew[i-1][j] + VNew[i+1][j] +
                                     VNew[i][j-1] + VNew[i][j+1])

    def SuccessiveOverRelaxation(self):
        L = self.L
        VNew = self.VNew
        V    = self.V         #avoid lots of typing
        rho  = self.rho
        omega= self.omega
        
        # update even sites in red-black scheme
        for i in range(1, self.L+1):
            for j in range(1, self.L+1):
                if (i + j) % 2 == 0:
                    VNew[i][j] = (1 - omega) * V[i][j] + omega / 4 * (
                                                                      V[i-1][j] + V[i+1][j] + V[i][j-1] +
                                                                      V[i][j+1])
    
        # update odd sites in red-black scheme
        for i in range(1, self.L+1):
            for j in range(1, self.L+1):
                if (i + j) % 2 != 0:
                    VNew[i][j] = (1 - omega) * V[i][j] + omega / 4 * (
                                                                      VNew[i-1][j] + VNew[i+1][j] + VNew[i][j-1] +
                                                                      VNew[i][j+1] )

    def relativeError(self):
        L = self.L
        VNew = self.VNew
        V    = self.V         #avoid lots of typing
        rho  = self.rho
        omega= self.omega
        
        error = 0
        n = 0
        for i in range(1, self.L+1):
            for j in range(1, self.L+1):
                if VNew[i][j] != 0 and VNew[i][j] != V[i][j]:
                    error += abs(1 - V[i][j] / VNew[i][j])
                    n += 1
        if n != 0:
            error /= n
            return error

    def NumDeriv(self):
        V=self.V
        hx = self.hx
        hy = self.hy
        Fx = self.Fx
        Fy = self.Fy
        for i in range(1, self.L+1):
            for j in range(1, self.L+1):
                Fx[i][j] = -self.q*(V[i][j+1]-V[i][j-1])/(2*hx)
                Fy[i][j] = -self.q*(V[i+1][j]-V[i-1][j])/(2*hy)
                    
    def trajflow(self,p) :
        t = p[0]
        x = p[1]
        y = p[2]
        vx = p[3]
        vy = p[4]
        j = int(x/self.hx+1)
        i = int(y/self.hy+1)
        ax = self.Fx[i][j]
        ay = self.Fy[i][j]
        flow = [1,vx,vy,ax,ay]
        return flow






print " Iterative solution of Poisson's equation"
print " ----------------------------------------"
L = int(input(" Enter number of interior points in x or y: "))
poisson = Poisson(L=L)
accuracy = float(input(" Enter desired accuracy in solution: "))
choice = int( input(" Enter choice of algorithm, Jacobi (0), Gauss-Seidel (1) or Successive overrelaxation (2): ") )

start_time = time.clock()

steps = 0

while True:
    if choice == 0 :
        poisson.Jacobi()
    elif choice == 1 :
        poisson.GaussSeidel()
    else :
        poisson.SuccessiveOverRelaxation()
    if poisson.relativeError() < accuracy:
        break
    for i in range(1, poisson.L+1):
        for j in range(1, poisson.L+1):
            poisson.V[i][j] = poisson.VNew[i][j]
    steps += 1

print " Number of steps =", steps
print " CPU time =", time.clock() - start_time, "sec"
poisson.NumDeriv()
#
# Convert x, y, V(x,y) to a surface plot
#from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from matplotlib.mlab import griddata
import matplotlib.pyplot as plt
import numpy as np
# Define the axes
x = np.arange(0, poisson.hx*(poisson.L+2), poisson.hx)
y = np.arange(0, poisson.hy*(poisson.L+2), poisson.hy)
# Get the grid
#X, Y = np.meshgrid(x, y)
# Set Z to the poisson V[i][j]
Z = np.array( poisson.V )
cutaway = []
for i in range (0, poisson.L+2):
    cutaway.append(Z[i][poisson.cent])

##And now let there be a trajectory
##initialize p vector, format [t,x,y,vx,vy]
#xv = [0.0]*5
#xv[0] = 0.0
#xv[1] = 0.0
#xv[2] = 0.0
#xv[3] = 0.5
#xv[4] = 0.5
#tau = float(input(" Enter step size dt: "))
#method = input( "Choose a numerical method : RK4 (0), or Adaptive RK4 (1): ")
#accuracy = float(input(" Enter desired accuracy for adaptive integration: "))
##* Loop over desired number of steps with given time step
##    and numerical method
#nStep = input( "Enter number of time steps: " )
#
#t_plot = []
#x_plot = []
#y_plot = []
#dt_min = tau
#dt_max = tau
#
#for  iStep in xrange(nStep) :
#
#    #if ( xv[0] > T ) :
#    #    break
#
#    #* Record angle and time for plotting
#    t_plot.append( xv[0] )
#    x_plot.append( xv[1] )
#    y_plot.append( xv[2] )
#
#    if  method == 0  :
#        RK4_step( xv, tau, poisson.trajflow )
#    elif method == 1 :
#        tau = RK4_adaptive_step(xv, tau, poisson.trajflow, accuracy)
#        dt_min = min(tau, dt_min)
#        dt_max = max(tau, dt_max)
#import matplotlib
#matplotlib.rcParams['legend.fancybox'] = True
#import matplotlib.pyplot as plt

#plt.scatter( x_plot, y_plot )



fig = plt.figure()
plt.plot(x,cutaway)
#ax = fig.gca(projection='3d')
#traj = ax.scatter(x_plot,y_plot)
#scat = ax.plot_surface( X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,linewidth=0, antialiased=False )
#traj = ax.scatter(x_plot,y_plot)
plt.show()
#

