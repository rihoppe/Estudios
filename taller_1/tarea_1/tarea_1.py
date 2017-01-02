import pyfits
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import math

parte_1 = False
parte_2 = True
parte_3 = False
parte_4 = True
parte_5 = False

if parte_1 == True:
	#obtengo los datos del espectro
	imagen_1 = pyfits.open('spDR2-008.fit')
	data = imagen_1['PRIMARY'].data
	c0 = imagen_1[0].header['coeff0']
	c1 = imagen_1[0].header['coeff1']
	
	#arreglo la escala
	lista_1=[]
	for i in range(len(data[0])):
		lista_1.append(10.**(c0+c1*i))
	
	fig_1 = plt.figure()
	ax_1 = fig_1.add_subplot(111)
	ax_2 = ax_1.twinx()
	#fig_1, ax_1 = plt.subplots()
	ax_1.plot(lista_1,data[0],label='espectro de la estrella')
	imagen_1.close()
	
	
	#obtengo los datos de las curvas de transmision
	g = open('g.dat','r')
	r = open('r.dat','r')
	contenido_g = g.readlines()
	contenido_r = r.readlines()
	x_r = []
	x_g = []
	y_r = []
	y_g = []
	for i in range(len(contenido_g[7:-1])):
		conten_g = contenido_g[7:-1]
		G=conten_g[i].split("  ")
		#print(G)
		x_g.append(G[1])
		y_g.append(float(G[2][1:]))
		#print(y_g)
		
	for h in range(len(contenido_r[7:-1])):
		conten_r = contenido_r[7:-1]
		R=conten_r[h].split("  ")
		#print(R)
		x_r.append(R[1])
		y_r.append(float(R[2][1:]))
		#print(y_r)
	ax_2.plot(x_g,y_g,'--g',label='linea de transmicion filtro g')
	ax_2.plot(x_r,y_r,'--r',label='linea de transmicion filtro r')
	#plt.show()

	def planck(l,T):
		l = l/(10.**10.) #m/s
		c = 299792458.
		h = 6.62606957/(10.**34.)
		k = 1.3806488/(10.**23.)
		a = 2.*h*c**2.
		b = h*c/(l*k*T)
		I = a/((l**5)*(np.exp(b)-1.))
		return I/73000000000
	
	A = np.linspace(3700,9400,10000)
	
	w=[]
	for i in range(len(A)):
		w.append(planck(A[i],5350))
	ax_1.plot(A,w,'black',label='cuerpo negro')
	#plot()
	ax_1.set_xlim((3700,9300))
	ax_1.set_ylim((0,280))
	ax_2.set_ylim((0,0.58))
	ax_1.legend(loc='upper left',bbox_to_anchor=(.59, .22),prop=dict(size=10))
	ax_2.legend(loc='lower right',prop=dict(size=10))
	ax_2.set_ylabel('Intencidad de las lineas de transmicion', color='r')
	ax_1.set_xlabel('Longitud de onda', color='black')
	ax_1.set_ylabel('Intencidad', color='black')
	for tl in ax_2.get_yticklabels():
		tl.set_color('r')
	plt.title('Espectro')
	#plt.grid(True)
	plt.savefig('cuerpo_negro.jpg')
	plt.show()
	

estrellas = open('estrellas.reg')
pos_estrellas = estrellas.readlines()
pos_estrellas_x = []
pos_estrellas_y = []
for i in range(len(pos_estrellas)):
	c = pos_estrellas[i].split(" ")
	pos_estrellas_x.append(c[1])
	pos_estrellas_y.append(c[2])

imagen_g = pyfits.open('king 7_g_500.fits')
imagen_r = pyfits.open('king 7_r_500.fits')
#imagen_g.info()
datos_g = imagen_g['primary'].data
datos_r = imagen_r['primary'].data



if parte_2==True:
	#apertura 1
	cuentas_g_1=[]
	cuentas_r_1=[]
	for i in range(len(pos_estrellas_y)):
		k = int(pos_estrellas_y[i])
		j = int(pos_estrellas_x[i])
		cuentas_g_1.append(datos_g[k][j])
		cuentas_r_1.append(datos_r[k][j])
		
	#apertura 3
	cuentas_g_2=[]
	cuentas_r_2=[]
	for i in range(len(pos_estrellas_y)):
		conteo_r=0
		conteo_g=0
		k = int(pos_estrellas_y[i])-1
		j = int(pos_estrellas_x[i])-1
		for l in range(3):
			for u in range(3):
				conteo_g+=datos_g[k+l][j+u]
				conteo_r+=datos_r[k+l][j+u]
		cuentas_g_2.append(conteo_g)
		#print('holi')
		#print(cuentas_g_2)
		cuentas_r_2.append(conteo_r)
		
	#apertura 5
	cuentas_g_3=[]
	cuentas_r_3=[]
	for i in range(len(pos_estrellas_y)):
		conteo_r=0
		conteo_g=0
		k = int(pos_estrellas_y[i])-2
		j = int(pos_estrellas_x[i])-2
		for l in range(5):
			for u in range(5):
				conteo_g+=datos_g[k+l][j+u]
				conteo_r+=datos_r[k+l][j+u]
		cuentas_g_3.append(conteo_g)
		cuentas_r_3.append(conteo_r)
	#apertura 7
	cuentas_g_4=[]
	cuentas_r_4=[]
	for i in range(len(pos_estrellas_y)):
		conteo_r=0
		conteo_g=0
		k = int(pos_estrellas_y[i])-3
		j = int(pos_estrellas_x[i])-3
		for l in range(7):
			for u in range(7):
				conteo_g+=datos_g[k+l][j+u]
				conteo_r+=datos_r[k+l][j+u]
		cuentas_g_4.append(conteo_g)
		cuentas_r_4.append(conteo_r)

if parte_3==True:
	cielo_g=[]
	cielo_r=[]
	for i in range(len(datos_g[0])):
		for h in range(len(datos_g[0])):
			if datos_g[i][h]<=0.1:
				cielo_g.append(datos_g[i][h])
			if datos_r[i][h]<=0.1:
				cielo_r.append(datos_r[i][h])
	prom_cielo_g = np.mean(cielo_g)
	print(prom_cielo_g)
	prom_cielo_r = np.mean(cielo_r)
	print(prom_cielo_r)
prom_cielo_g = 0.0129214070166
prom_cielo_r = 0.0205248301537
for i in range(len(cuentas_g_1)):
	cuentas_g_1[i]=cuentas_g_1[i]-prom_cielo_g
	cuentas_g_2[i]=cuentas_g_2[i]-prom_cielo_g
	cuentas_g_3[i]=cuentas_g_3[i]-prom_cielo_g
	cuentas_g_4[i]=cuentas_g_4[i]-prom_cielo_g
for i in range(len(cuentas_r_1)):
	cuentas_r_1[i]=cuentas_r_1[i]-prom_cielo_r
	cuentas_r_2[i]=cuentas_r_2[i]-prom_cielo_r
	cuentas_r_3[i]=cuentas_r_3[i]-prom_cielo_r
	cuentas_r_4[i]=cuentas_r_4[i]-prom_cielo_r

def magnitud(cuentas):
	return (-2.5*np.log10(cuentas)+20)
def plotear(datos_g,datos_r,n):
	eje_x =[]
	eje_y =[]
	for i in range(len(datos_g)):
		eje_x.append(magnitud(datos_g[i])-magnitud(datos_r[i]))
		eje_y.append(magnitud(datos_r[i]))
	plt.plot(eje_x,eje_y,'ro',label='estrellas cumulo King 7')
	#plt.set_xlim((0,3))
	#plt.set_ylim((0,25))
	#plt.legend(loc='upper left',bbox_to_anchor=(.59, .22),prop=dict(size=10))
	plt.xlabel('G-R', color='black')
	plt.ylabel('Magnitud r', color='black')
	ja='grafico_'+str(n)
	plt.gca().invert_yaxis()
	plt.legend(loc='upper left')
	plt.savefig(ja)
	plt.show()
if parte_4==True:
	plotear(cuentas_g_1,cuentas_r_1,1)
	plotear(cuentas_g_2,cuentas_r_2,2)
	plotear(cuentas_g_3,cuentas_r_3,3)
	plotear(cuentas_g_4,cuentas_r_4,4)

if parte_5 == True:
	archivo_1=open("datos_apertura_7x7.txt",'w')
	archivo_1.write('posx/ posy/ magnitud_g/ cielo_g/ magnitud_r/ cielo_r/ G-R/ \n')
	for i in range(len(pos_estrellas_x)):
		s = pos_estrellas_x[i]
		d = pos_estrellas_y[i]
		ya = cuentas_g_4[i]
		ye = round(magnitud(ya),3)
		yi = round(prom_cielo_g,3)
		ta = cuentas_r_4[i]
		te = round(magnitud(ta),3)
		ti = round(prom_cielo_r,3)
		tu = round(ye-te,3)
		l=str(s)+'\t'+str(d)+'\t'+str(ye)+'\t'+str(yi)+'\t'+str(te)+'\t'+str(ti)+'\t'+str(tu)+'\n'
		archivo_1.write(l)


