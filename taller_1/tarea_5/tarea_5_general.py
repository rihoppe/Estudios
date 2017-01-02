import numpy as np
import scipy.constants as constants
import matplotlib.pyplot as plt
import os
import pyfits


def espectro(nombre,x_i,x_f,y_c,delta_y,alrededor):
	"""Obtencion de datos"""
	imagen_nova = pyfits.open(nombre)
	nova = imagen_nova['Primary'].data
	"""obtencion del espectro"""
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

	"""graficos"""
	return plt.plot(x,y), plt.axhline(ruido+3*std_ruido,linewidth=2, color='r',label='',ls='--')
	
def plot_imagen(nombre):
	imagen = pyfits.open(nombre)
	datos = imagen['Primary'].data
	return plt.imshow(datos, cmap='gray',clim=(0.0, 6000.0))

def plot_doble(nombre,x_i,x_f,y_c,delta_y,alrededor):
	plt.figure(1)
	plt.subplot(211)	
	plot_imagen(nombre)
	plt.subplot(212)
	espectro(nombre,x_i,x_f,y_c,delta_y,alrededor)
	plt.show()

def plot_triple(nombre,x_i,x_f,y_c,delta_y,alrededor,x_i_2,x_f_2):
	plt.figure(1)
	plt.subplot(221)	
	plot_imagen(nombre)
	plt.subplot(222)
	espectro(nombre,x_i,x_f,y_c,delta_y,alrededor)
	plt.subplot(223)
	espectro(nombre,x_i_2,x_f_2,y_c,delta_y,alrededor)
	plt.show()
def plot_doble_2(nombre,x_i,x_f,y_c,delta_y,alrededor,x_i_2,x_f_2):
    plt.figure(1)
    plt.subplot(211)
    espectro(nombre,x_i,x_f,y_c,delta_y,alrededor)
    plt.subplot(212)
    espectro(nombre,x_i_2,x_f_2,y_c,delta_y,alrededor)
"""Nova"""

#plot_doble('04_NovaSMC_60s.fits',500,1200,750,15,10)
#plot_doble('04_NovaSMC_60s.fits',500,900,750,15,10)
#plot_triple('04_NovaSMC_60s.fits',500,1200,750,15,10,550,900)

os.chdir('/home/rai/Desktop/taller_1/tarea_5/fits')

"""NuTuc"""
#plot_doble('03_NuTuc_0p2s_b2.FIT',200,1000,500,10,10)

"""GamCap"""
#plot_doble('06_gamcap_0p2s_b2.FIT',700,1300,860,15,15)
#plot_doble('06_gamcap_0p2s_b2.FIT',750,1000,860,15,15)
#plot_triple('06_gamcap_0p2s_b2.FIT',700,1300,860,15,15,750,1000)

"""mupsa"""
#plot_doble('09_mupsa_0p2s_b2.FIT',500,1100,870,15,15)

"""epspsa"""
#plot_doble('12_epspsa_0p2s_b2.FIT',800,1300,335,10,10)

"""zetcap"""
plot_doble('27_34zetcap_0p2s_b2.FIT',800,1300,335,10,10)

"""obtecion de la escala"""
"""
x_i, x_f, y_c, delta_y, alrededor = 500, 1200, 750, 15, 10
imagen_nova = pyfits.open('04_NovaSMC_60s.fits')
nova = imagen_nova['Primary'].data
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
xy = []
xy_2 = []
for i in range(len(x)):
	xy.append([y[i],x[i]])
	if x[i]>900:
		xy_2.append([y[i],x[i]])
print max(xy)
print max(xy_2)
"""
print 'holi'
