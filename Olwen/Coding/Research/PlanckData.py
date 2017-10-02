#!/usr/bin/python

#
# Set up plotting package
#
import numpy as np
from scipy import interpolate
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'
interplevel = 4

Title="Planck 2015 + BICEP/Keck (BK14) Polarization"

#
# Subroutine to do interpolated contour plotting.
#
def PlotInterpContour(x,y,z,interp,levels,colors=((0.957,0.459,0.580),(0.957,0.067,0.286)),fill=True,linestyles='solid',linewidths=3,labels=True,debug=False,manual=False):
	xi = np.linspace(x.min(),x.max(),len(x)*interp)
	yi = np.linspace(y.min(),y.max(),len(y)*interp)
	sp = interpolate.RectBivariateSpline(x,y,z)
	zi = sp(xi,yi).transpose()
	cp = plt.contour(xi,yi,zi,levels=levels,colors=('black','gray'),linestyles=linestyles,linewidths=linewidths)

	if labels:
		plt.clabel(cp,[levels[0]],fmt='95%%',fontsize=16,manual=manual)
		plt.clabel(cp,[levels[1]],fmt='68%%',fontsize=16,manual=manual)

	if debug:
		plt.pcolor(xi,yi,zi) # Color gradient plot
		plt.contour(x,y,z.transpose(),levels=levels,colors=('red','red')) # Non-interpolated
	elif fill:
		plt.contourf(xi,yi,zi,levels=levels,colors=colors)

#
# Read in chains from PLanck + Lensing 
#
Label1 = 'Planck TT/TE/EE+lowTEB + BK14'
Label2 = 'unused'
param1 = 'r' 
param2 = 'ns' 
basename = './PlanckBK14/PlanckBK14'
param1fname = basename + '_2D_' + param2 +'_' + param1 + '_x'
param2fname = basename + '_2D_' + param2 +'_' + param1 + '_y'
ptsfname = basename + '_2D_' + param2 +'_' + param1
contfname = basename + '_2D_' + param2 +'_' + param1 + '_cont'

print ('Reading 2D points data...')
ptsf = open(ptsfname, 'r')
ptsstr = [line for line in ptsf] 
ptsarr = np.array([[float(s) for s in p.split()] for p in ptsstr]) 
print ('Done.\n')

print ('Reading 2D contour data...')
contf = open(contfname, 'r')
contstr = [line.split() for line in contf][0]
contarr = np.array([float(s) for s in contstr]) 
print ('Done.\n')

print ('Reading likelihood data for param' + param1)
param1f = open(param1fname, 'r')
param1str = [line for line in param1f]
r = param1arr = np.array([[float(s) for s in p.split()] for p in param1str])
print ('Done.\n')

print ('Reading likelihood data for param' + param2)
param2f = open(param2fname, 'r')
param2str = [line for line in param2f]
n = param2arr = np.array([[float(s) for s in p.split()] for p in param2str])
print ('Done.\n')

#
# Trick: Extend likelihood matrix to extremely low r-values by resetting first element in r
# from zero to a small number. 
# 
r[0] = 0.00001

#
# Plot 2-D contours of likelihood.
#
# The x-coordinate must be param2
# The y-coordinate must be param1
#
# If you want to reverse x and y, you must pass ptsarr.transpose() to PlotInterpContour!
#
ACTSPTColors=((0.957,0.459,0.580),(0.957,0.067,0.286))
plt.figure(1)
x = np.array([n[i][0] for i in range(len(n))])
y = np.array([r[i][0] for i in range(len(r))])
levs = np.array([contarr[1],contarr[0],10*ptsarr.max()])

PlotInterpContour(x,y,ptsarr,interplevel,levs,debug=False,fill=True,colors=ACTSPTColors,linewidths=0,labels=False)
PlotInterpContour(x,y,ptsarr,interplevel,levs,fill=False,linestyles='solid',linewidths=1,debug=False,labels=False,)


plt.title(Title)




