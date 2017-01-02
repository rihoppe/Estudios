import numpy as np
import scipy.constants as constants
import matplotlib.pyplot as plt
import os
import pyfits

imagen_nova = pyfits.open('04_NovaSMC_60s.fits')
#imagen_nova.info()
nova = imagen_nova['Primary'].data
plt.imshow(nova, cmap='gray',clim=(0.0, 6000.0))
#plt.plot(1000,1000,'ro')
plt.show()
"""print nova[y][x]"""

print np.std(nova)
print np.mean(nova)
"""datos a usar"""	
x_i = 500
x_f = 1200
y_c = 750
delta_y = 15

"""promedios"""
y_i = y_c-delta_y
y_f = y_c+delta_y
y = []
x = []

for g in range(x_f-x_i):
	conteo = []
	for i in range(y_f-y_i):
	 conteo.append(nova[y_i+i][x_i+g])
	y.append(np.mean(conteo))
	x.append(x_i+g)
	
"""calculo del ruido"""
alrededor = 10
conteo_2 = []
x_i_2, x_f_2 = x_i-alrededor, x_f+alrededor
y_i_2, y_f_2 = y_i-alrededor, y_f+alrededor
for g in range(x_f_2-x_i_2):
	for i in range(y_f_2-y_i_2):
		if x_i_2+g>x_i and x_i_2+g<x_f and y_i_2+i>y_i and y_i_2+i<y_f :
			pass
		else:
			conteo_2.append(nova[y_i_2+i][x_i_2+g])
ruido = np.mean(conteo_2)
std_ruido = np.std(conteo_2)
print ruido, std_ruido	
"""graficos"""
plt.plot(x,y)
plt.axhline(ruido+3*std_ruido,linewidth=2, color='r',label='',ls='--')
plt.show()

