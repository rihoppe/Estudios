import pyfits
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import scipy as sp
import math
import os
#import polar_plots
import pylab as m
import mpl_toolkits
print mpl_toolkits.__file__
#import importlib
print matplotlib.__path__

datos = open('result.csv','r')
contenido = datos.readlines()

for i in range(len(contenido)):
	contenido[i] = contenido[i].split(',')
	contenido[i][8]=contenido[i][8][:-1]
print contenido[1]

#[id , ra, dec, Redshift, Redshift Err, Mag_g, Mag_r, Mag_g_Err, Mag_r_Err ]

ra = []
dec = []
redshift = []
redshift_err = []
mag_g = []
mag_r = []
mag_g_err = []
mag_r_err = []
color = []
color_err = []
for i in range(len(contenido)):
	if i!=0:
		if float(contenido[i][1])>=100 and float(contenido[i][1])<=270:
			ra.append(float(contenido[i][1]))
			dec.append(float(contenido[i][2]))
			redshift.append(float(contenido[i][3]))
			redshift_err.append(float(contenido[i][4]))
			mag_g.append(float(contenido[i][5]))
			#print(contenido[i][5])
			mag_r.append(float(contenido[i][6]))
			mag_g_err.append(float(contenido[i][7]))
			mag_r_err.append(float(contenido[i][8]))
for i in range(len(mag_g)):
		color.append(float(mag_g[i])-float(mag_r[i]))
		#print(float(mag_g[i])-float(mag_r[i]))
		color_err.append(np.sqrt(float(mag_g_err[i])**2+float(mag_r_err[i])**2))
#print(color)	
for i in range(len(ra)):
	ra[i]=float(ra[i])*np.pi/180
	
ax = plt.subplot(111, projection='polar')
#ax.plot(ra, redshift,'ro')
ax.grid(True)
#plt.show()

angles=[90,180]
radii=[0.2,0.4,0.6,0.8,1]
m.polar(ra, redshift,'ro')
m.thetagrids(angles, labels=None, frac = 1.1)
m.rgrids(radii, labels=None, angle=22.5)
plt.show()
#polar_plots.holi()
