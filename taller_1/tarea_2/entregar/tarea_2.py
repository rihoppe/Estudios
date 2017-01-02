import pyfits
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import scipy as sp
import math
import os


parte_1 = False
parte_1_5 = False
parte_2 = False
datos = True
parte_3 = True
err = False
parte_4=True
NGC6441 = True
King_7= False

if parte_1==True:

	imagen_555 = pyfits.open('hst_9835_02_acs_hrc_f555w_drz.fits')
	imagen_814 = pyfits.open('hst_9835_02_acs_hrc_f814w_drz.fits')
	#imagen_555.info()
	datos_555 = imagen_555['sci'].data
	datos_814 = imagen_814['sci'].data
	peso_555 = imagen_555['WHT'].data
	peso_814 = imagen_814['WHT'].data
	
	imagen_555['sci'].writeto('sci_555_data.fits')
	imagen_814['sci'].writeto('sci_814_data.fits')
	imagen_555['WHT'].writeto('wht_555_data.fits')
	imagen_814['WHT'].writeto('wht_814_data.fits')	
	
if parte_1_5==True:
	imagen_814 = pyfits.open('hst_9835_02_acs_hrc_f814w_drz.fits')
	datos_814 = imagen_814['sci'].data
	peso_814 = imagen_814['WHT'].data
	#image_data = fits.getdata(datos_814)
	plt.imshow(datos_814, cmap='gray',clim=(0.0, 25.0))
	plt.show()
	plt.imshow(peso_814, cmap='gray')
	#plt.colorbar()
	plt.show()
	
	print(datos_814)
if parte_2 == True:
	ima = pyfits.open('wht_555_data.fits')
	ima.info()
	os.system('sex sci_814_data.fits,sci_555_data.fits -CATALOG_NAME=datos_555.cat')
	os.system('sex sci_814_data.fits,sci_814_data.fits -CATALOG_NAME=datos_814.cat')
	os.system('sex king_7_r_500.fits,king_7_g_500.fits -CATALOG_NAME=datos_king_7_g.cat')
	os.system('sex king_7_r_500.fits,king_7_r_500.fits -CATALOG_NAME=datos_king_7_r.cat')
	
if datos == True:
	datos_r = open('datos_king_7_r.cat','r')
	datos_g = open('datos_king_7_g.cat','r')
	datos_555 = open('datos_555.cat','r')
	datos_814 = open('datos_814.cat','r')
	contenido_r = datos_r.readlines()
	contenido_g = datos_g.readlines()
	contenido_555 = datos_555.readlines()
	contenido_814 = datos_814.readlines()
	contenido_555 = contenido_555[8:]
	contenido_814 = contenido_814[8:]
	contenido_g = contenido_g[8:]
	contenido_r =contenido_r[8:]
	def separar(x):
		for i in range(len(x)):
			x[i] = x[i].split(' ')
			w=[]
			a=0
			for t in range(len(x[i])):
				if x[i][t]=='':
					a+=1
				else:
					w.append(x[i][t])
			x[i] = w
			w=[]
			x[i][7]=x[i][7][:-1]
	
	
	separar(contenido_555)
	separar(contenido_814)
	separar(contenido_g)
	separar(contenido_r)
	
	
	mag_555 = []
	mag_814 = []
	err_mag_555 = []
	err_mag_814 = []
	for i in range(len(contenido_555)):
		if int(contenido_555[i][7])<5:
			if float(contenido_555[i][4])<=2:
				if float(contenido_814[i][4])<=2:
					mag_555.append(contenido_555 [i][3])
					mag_814.append(contenido_814[i][3])
					err_mag_555.append(float(contenido_555 [i][4]))
					err_mag_814.append(float(contenido_814 [i][4]))

	mag_g = []
	mag_r = []
	err_mag_r = []
	err_mag_g = []
	for i in range(len(contenido_g)):
		if int(contenido_g[i][7])<5:
			if float(contenido_g[i][4])<=2:
				if float(contenido_r[i][4])<=2:	
					mag_g.append(float(contenido_g[i][3])+20)
					mag_r.append(float(contenido_r[i][3])+20)
					err_mag_r.append(float(contenido_r [i][4]))
					err_mag_g.append(float(contenido_g [i][4]))
	mag_g_r = []
	for i in range(len(mag_g)):
		mag_g_r.append(float(mag_g[i])-float(mag_r[i]))
	mag_555_814= []
	for i in range(len(mag_555)):
		mag_555_814.append(-float(mag_814[i])+float(mag_555[i]))
	
	todos_los_errores = err_mag_555+err_mag_814+err_mag_g+err_mag_r

if parte_3==True:
	if King_7==True:
		fig_1 = plt.figure(1)
		#plt.subplot(111)
		plt.plot(mag_g_r,mag_g,'ro',label='estrellas King 7',mew=0.6,mec='black',ms=3.5)
		plt.axis([0, 4.5, 10, 25])
		#plt.set_xlim((0,4.5))
		#plt.set_ylim((10,25))
		plt.xlabel('g-r', color='black')
		plt.ylabel('r', color='black')
		plt.gca().invert_yaxis()
		plt.savefig("image_1.png")
	if NGC6441==True:
		fig_2 = plt.figure(2)
		#plt.subplot(111)
		plt.plot(mag_555_814,mag_814,'bo',label='estrellas NGC6441',mew=0.6,mec='black',ms=3.5)
		plt.axis([-1.5, 3, 12, 23])
		#plt.set_xlim((-1.5,3))
		#plt.set_ylim((12,23))
		plt.xlabel('F555w-F814w', color='black')
		plt.ylabel('F814w', color='black')
		plt.gca().invert_yaxis()
		plt.savefig("image_2.png")
	
	
if err == True:
	fig_3 = plt.figure(3)
	#ax_6 = fig_4.add_subplot(111)
	plt.plot(mag_555,err_mag_555,'ro',mew=0.6,mec='black',ms=3.5,label='filtro F555W')
	plt.plot(mag_814,err_mag_814,'go',mew=0.6,mec='black',ms=3.5,label='filtro F814W')
	plt.plot(mag_g,err_mag_g,'bo',mew=0.6,mec='black',ms=3.5,label='filtro g')
	plt.plot(mag_r,err_mag_r,'co',mew=0.6,mec='black',ms=3.5,label='filtro r')
	plt.legend(loc='upper left')
	plt.set_ylim((0,2))
	plt.set_xlim((13,23))	
	plt.set_xlabel('Magnitud')
	plt.set_ylabel('Error')
	plt.savefig("image_err.png")

if parte_4==True:
	fig_4 = plt.figure(4)
	plt.rcParams['figure.figsize']=(12.5,10)
	plt.hexbin(mag_555_814, mag_814,label='estrellas NGC6441',gridsize=65,mincnt=1)
	plt.gca().invert_yaxis()
	plt.axis([-1.5, 3, 12, 23])
	cbar=plt.colorbar()
	plt.gca().invert_yaxis()
	cbar.set_label('Cantidad de estrellas')
	plt.xlabel('F555W-F814W')
	plt.ylabel('F814W')
	plt.savefig("image_distribucion_NGC6441.png")
	
	"""
	fig_5 = plt.figure(5)
	plt.rcParams['figure.figsize']=(12.5,10)
	plt.hexbin(mag_g_r, mag_r,label='estrellas King 7',gridsize=25,mincnt=1)
	plt.gca().invert_yaxis()
	plt.axis([0, 4.5, 10, 25])
	cbar=plt.colorbar()
	plt.gca().invert_yaxis()
	cbar.set_label('Cantidad de estrellas')
	plt.xlabel('g-r')
	plt.ylabel('r')
	plt.savefig("image_distribucion_king_7.png")
	"""
	log_err_mag_r = []
	log_err_mag_814 = []
	for i in range(len(err_mag_814)):
		log_err_mag_814.append(np.log10(err_mag_814[i]))
	for i in range(len(err_mag_r)):
		log_err_mag_r.append(np.log10(err_mag_r[i]))
	fig_6 = plt.figure(6)
	plt.subplot(122)
	plt.rcParams['figure.figsize']=(12.5,30)
	plt.hexbin(mag_555_814,mag_814,C=log_err_mag_814,gridsize=65,mincnt=1,cmap=plt.get_cmap('seismic'))
	plt.axis([-1.5, 3, 12, 23])
	plt.gca().invert_yaxis()
	cbar=plt.colorbar()
	cbar.set_label('Error en la medicion de la magnitud filtro F814W (escala logaritmica en base 10)')
	plt.xlabel('F555W-F814W')
	plt.ylabel('F814W')
	#plt.savefig("image_distribucion_NGC6441_errores.png")
	
	#fig_7 = plt.figure(7)
	plt.subplot(121)
	plt.rcParams['figure.figsize']=(12.5,30)
	plt.scatter(mag_g_r,mag_r,c=log_err_mag_r)
	plt.axis([0, 4.5, 10, 23])
	plt.gca().invert_yaxis()
	cbar=plt.colorbar()
	cbar.set_label('Error en la medicion de la magnitud filtro r (escala logaritmica en base 10)')
	plt.xlabel('g-r')
	plt.ylabel('r')
	#plt.savefig("image_distribucion_King_7_errores.png")
	plt.savefig("image_distribucion_errores.png")
plt.show()


