import math
import numpy as np
import matplotlib.pyplot as plt
import PlanckData


def read_data(filename,potlabel) :
    with open(filename,'r') as file:
    lines = file.readlines()
    x = []
    y = []
    z = []
    for line in lines :
        if line != '\n' :
            words = line.split()
            ix, iy, iz = [float(s) for s in words]
            x.append( ix )
            y.append( iy )
            z.append( iz )
    plt.semilogy(x,y,label=potlabel)
    last = len(z)-1
    Nmin = int(round(z[0]))
    Nmax = int(round(z[last]))
    plt.text(x[0],y[0],Nmin,size=12,rotation=0,fontweight='roman')
    plt.text(x[last],y[last],Nmax,size=12,rotation=0,fontweight='roman')
with open('Squared0.dat','r') as file1:
    lines = file1.readlines()
    x1 = []
    y1 = []
    z1 = []
    for line in lines :
        if line != '\n' :
            words = line.split()
            ix, iy, iz = [float(s) for s in words]
            x1.append( ix )
            y1.append( iy )
            z1.append( iz )
    plt.semilogy(x1,y1,label=r'$\theta^2$ potential')
    last = len(z1)-1
    Nmin1 = int(round(z1[0]))
    Nmax1 = int(round(z1[last]))
    plt.text(x1[0],y1[0],Nmin1,size=12,rotation=0,fontweight='roman')
    plt.text(x1[last],y1[last],Nmax1,size=12,rotation=0,fontweight='roman')
with open('oneminus40.dat','r') as file2:
    lines = file2.readlines()
    x2 = []
    y2 = []
    z2 = []
    for line in lines :
        if line != '\n' :
            words = line.split()
            ix, iy, iz = [float(s) for s in words]
            x2.append( ix )
            y2.append( iy )
            z2.append( iz )
    plt.semilogy(x2,y2,label=r'$1-\theta^4$ potential')
    last = len(z2)-1
    Nmin2 = int(round(z2[0]))
    Nmax2 = int(round(z2[last]))
    plt.text(x2[0],y2[0],Nmin2,size=12,rotation=0,fontweight='roman')
    plt.text(x2[last],y2[last],Nmax2,size=12,rotation=0,fontweight='roman')

with open('oneminus60.dat','r') as file3:
    lines = file3.readlines()
    x3 = []
    y3 = []
    z3 = []
    for line in lines :
        if line != '\n' :
            words = line.split()
            ix, iy, iz = [float(s) for s in words]
            x3.append( ix )
            y3.append( iy )
            z3.append( iz )

    plt.semilogy(x3,y3,label=r'$1-\theta^6$ potential')
    last = len(z3)-1
    Nmin3 = int(round(z3[0]))
    Nmax3 = int(round(z3[last]))
    plt.text(x3[0],y3[0],Nmin3,size=12,rotation=0,fontweight='roman')
    plt.text(x3[last],y3[last],Nmax3,size=12,rotation=0,fontweight='roman')
with open('oneminus80.dat','r') as file4:
    lines = file4.readlines()
    x4 = []
    y4 = []
    for line in lines :
        if line != '\n' :
            words = line.split()
            ix, iy, iz = [float(s) for s in words]
            x4.append( ix )
            y4.append( iy )
    plt.semilogy(x4,y4,label=r'$1-\theta^8$ potential')
with open('Starobinsky0.dat','r') as file5:
    lines = file5.readlines()
    x5 = []
    y5 = []
    for line in lines :
        if line != '\n' :
            words = line.split()
            ix, iy, iz = [float(s) for s in words]
            x5.append( ix )
            y5.append( iy )
    plt.semilogy(x5,y5,label="Starobinsky potential")
with open('twothirds0.dat','r') as file6:
    lines = file6.readlines()
    x6 = []
    y6 = []
    for line in lines :
        if line != '\n' :
            words = line.split()
            ix, iy, iz = [float(s) for s in words]
            x6.append( ix )
            y6.append( iy )
    plt.semilogy(x6,y6,label=r'$\theta^{2/3}$ potential')

#with open('Starobinsky.dat','r') as file7:
#    lines = file7.readlines()
#    x7 = []
#    y7 = []
#    for line in lines :
#        if line != '\n' :
#            words = line.split()
#            ix, iy = [float(s) for s in words]
#            x7.append( ix )
#            y7.append( iy )
#    plt.semilogy(x7,y7,label="checking potential")
plt.legend(loc=2)

plt.show()
