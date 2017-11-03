from naclmet import *
import numpy as np
import matplotlib.pyplot as plt
from mplot3d import Axes3D
from math import *
import time
name="Na4Cl4"       # for output files
nNa = 4
nCl = 4
n = nNa + nCl
a = 0.24
rt2 = pow(2,0.5)
#rt2 = 1.4

#This configuration gives me the octagon:
#a =  0.2
#r_Na = [  [ 0, 0, 0 ], [ 2*a, 0, 0] ,[0,2*a,0],[2*a,2*a,0]]
#r_Cl = [  [ a, 0, 0 ], [ -a, a, 0] ,[a,2*a,0],[2*a,a,0]]


#this combo gives the bowed rectangle
''''
a = 0.24
r_Na = [  [ 0, 0, 0 ], [ a, a, 0] ,[2*a,0,0],[3*a,a,0]]
r_Cl = [  [ 0, a, 0 ], [ a, 0, 0] ,[2*a,a,0],[3*a,0,0]]
'''


#and this gets me the cube:
'''
a= 0.2
r_Na = [  [ 0, 0, 0 ], [ 2*a, 2*a, 0] ,[0,2*a,2*a],[2*a,0,2*a]]
r_Cl = [  [ 2*a, 0, 0 ], [ 0, 2*a, 0] ,[0,0,2*a],[2*a,2*a,2*a]]
'''

#This gives me (I think) one of the weird ones:
a=0.2
r_Na = [  [ 0, 0, 0 ], [ a, 2*a, 0] ,[a,0,a],[0,a,a]]
r_Cl = [  [ 2*a, 0, 0 ], [ 0, a, 0] ,[-a,a,a],[0,0,-a]]

# Initialize the cluster, add guesses at the
# minimum arrangement.
cluster = Cluster()
cluster1 = Cluster()
for i in xrange(nNa) :
    r = Vector(r_Na[i])
    cluster.add(Na(r))
    cluster1.add(Na(r))

for i in xrange(nCl) :
    r = Vector(r_Cl[i])
    cluster.add(Cl(r))
    cluster1.add(Cl(r))

print " " + name + " cluster"
print " Initial potential energy = " + str( cluster.potential_energy() )
[x1,y1,z1] = cluster.convert()
# Minimize the function
accuracy = 1e-6

res = cluster.minimize( accuracy )
pe = res[1]
iterations = res[4]
[x2,y2,z2] = cluster.convert()
start_time = time.clock()
metpot = cluster1.MetropolisMinimize(2000,1000)

print " CPU time =", time.clock() - start_time, "sec"
# Print out resulting files, and also
# plot the values in matplotlib
#print " Minimized potential energy = " + str(pe) + " eV"
#print " Binding energy of cluster  = " + str( pe / 2.0 ) + " eV"
#print " Number of function calls = " + str( iterations )
print " Minimized potential energy with Metropolis = " + str(metpot) + " eV"
print " Binding energy of cluster  = " + str( metpot / 2.0 ) + " eV"
file_name = name + ".data"
outfile = open( file_name, 'w' )
for i in xrange( nNa + nCl - 1) :
    for j in range(i+1,nNa+nCl) :
        rij = cluster.ion(i).r - cluster.ion(j).r
        dr = sqrt( np.dot(rij,rij) )
        s =  "(" + cluster.ion(i).name + ")-(" + cluster.ion(j).name + ")"
        print " " + s + " r_" + str(i) + str(j) + " = " + str( dr ) + " nm"

outfile.write( str(cluster) )
outfile.close()

fig = plt.figure()
#ax = fig.add_subplot(3,1,1, projection='3d')
ax = fig.add_subplot(2,1,1, projection='3d')
[x,y,z] = cluster1.convert()
ax.scatter( x,y,z )
#ax2 =fig.add_subplot(3,1,2, projection='3d')
#ax2.scatter(x1,y1,z1)
#ax3 =fig.add_subplot(3,1,3, projection='3d')
ax3 =fig.add_subplot(2,1,2, projection='3d')
ax3.scatter(x2,y2,z2)
plt.show()

