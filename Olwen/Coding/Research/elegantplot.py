import math
import numpy as np
import matplotlib.pyplot as plt



def read_data(filename) :
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
        last = len(z)-1
        Nmin = int(round(z[0]))
        Nmax = int(round(z[last]))
    return x,y,Nmin,Nmax,last

[x1,y1,Nmin1,Nmax1,last] = read_data('Squared0.dat')
fig, ax = plt.subplots()
import PlanckData
ax.semilogy(x1,y1,label=r'$\theta^2$ potential')
ax.text(x1[0],y1[0],Nmin1,size=12,rotation=0,fontweight='roman')
ax.text(x1[last],y1[last],Nmax1,size=12,rotation=0,fontweight='roman')

[x2,y2,Nmin2,Nmax2,last] = read_data('oneminus40.dat')
ax.semilogy(x2,y2,label=r'$1-\theta^4$ potential')
ax.text(x2[0],y2[0],Nmin2,size=12,rotation=0,fontweight='roman')
ax.text(x2[last],y2[last],Nmax2,size=12,rotation=0,fontweight='roman')

[x3,y3,Nmin3,Nmax3,last] = read_data('oneminus60.dat')
ax.semilogy(x3,y3,label=r'$1-\theta^6$ potential')
ax.text(x3[0],y3[0],Nmin3,size=12,rotation=0,fontweight='roman')
ax.text(x3[last],y3[last],Nmax3,size=12,rotation=0,fontweight='roman')

[x4,y4,Nmin4,Nmax4,last] = read_data('oneminus80.dat')
ax.semilogy(x4,y4,label=r'$1-\theta^8$ potential')
ax.text(x4[0],y4[0],Nmin4,size=12,rotation=0,fontweight='roman')
ax.text(x4[last],y4[last],Nmax4,size=12,rotation=0,fontweight='roman')

[x5,y5,Nmin5,Nmax5,last] = read_data('Starobinsky0.dat')
ax.semilogy(x5,y5,label='Starobinsky Potential')
ax.text(x5[0],y5[0],Nmin5,size=12,rotation=0,fontweight='roman')
ax.text(x5[last],y5[last],Nmax5,size=12,rotation=0,fontweight='roman')
[x5,y5,Nmin5,Nmax5,last] = read_data('Starobinskyw2.dat')
ax.semilogy(x5,y5,label='Starobinsky Potential')
ax.text(x5[0],y5[0],Nmin5,size=12,rotation=0,fontweight='roman')
ax.text(x5[last],y5[last],Nmax5,size=12,rotation=0,fontweight='roman')

[x6,y6,Nmin6,Nmax6,last] = read_data('twothirds0.dat')
ax.semilogy(x6,y6,label=r'$\theta^{2/3}$ potential')
ax.text(x6[0],y6[0],Nmin6,size=12,rotation=0,fontweight='roman')
ax.text(x6[last],y6[last],Nmax6,size=12,rotation=0,fontweight='roman')
ax.axis([0.935,0.985,.00005,.5])
ax.legend(loc=0,numpoints=1);
ax.set_xlabel('$n_s$',size=24)
ax.set_ylabel('$r_{0.05}$',size=24)
ax.set_title('',size=16)
plt.show()

