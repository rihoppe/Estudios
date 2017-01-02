#librerias
import math
import matplotlib.mlab as mlab
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from scipy.stats import norm
import scipy.integrate as integrate
#variables utilizadas
hombrestotal=[]
mujerestotal=[]
#funciones
def modas(l):
	repeticiones=0
	for i in l:
		apariciones=l.count(i)
		if apariciones>repeticiones:
			repeticiones=apariciones
	modas=[]
	for i in l:
		apariciones=l.count(i)
		if apariciones==repeticiones and i not in modas:
			modas.append(i)
	return int(modas[0])
#recoleccion de datos
os.chdir("/home/rai/Desktop/intro. al analisis de datos/tarea 1")
datosp=os.listdir("/home/rai/Desktop/intro. al analisis de datos/tarea 1/personas")
#pdf_pages = PdfPages("tarea1_p4mujeres.pdf")
for c in range(len(datosp)):
	hombres=[]
	machos=[]
	hembras=[]
	mujeres=[]
	print (str(c) +" - "+ datosp[c])
	grupo=datosp[c]
	os.chdir("/home/rai/Desktop/intro. al analisis de datos/tarea 1/personas")
	dato=open(grupo,"r")
	contenido= dato.readlines()
	os.chdir("/home/rai/Desktop/intro. al analisis de datos/tarea 1")
	for t in range(len(contenido)):
		if contenido[t]=="\n":
			div=t
	for h in range(div+1,len(contenido)):
		if str(contenido[h])!="XXX\n":
			hombres.append(str(contenido[h]))
	for g in range(div):
		if str(contenido[g])!="XXX\n":
			mujeres.append(str(contenido[g]))
			

	for i in range(len(hombres)):
		a= int(hombres[i][0:2])
		if a<30:
			machos.append(int(hombres[i][0:3]))
		else:
			machos.append(int(hombres[i][0:2]))
	for i in range(len(mujeres)):
		b= int(mujeres[i][0:2])
		if b<30:
			hembras.append(int(mujeres[i][0:3]))
		else:
	 		hembras.append(int(mujeres[i][0:2]))
	mujerestotal=mujerestotal+hembras
	hombrestotal=hombrestotal+machos

total=hombrestotal+mujerestotal

# pregunta 4 histogramas


#grafico hombres total
des=np.std(mujerestotal)
dese=str(des)
#promedio
promedio_mt= np.mean(mujerestotal)
#mediana
mediana_mt = np.median(mujerestotal)
#moda
moda_mt=modas(mujerestotal)

#grafico
bin_mt=np.arange(min(mujerestotal),max(mujerestotal)+3,3)
fig=plt.figure(dpi=100)

#histograma
n,ho,he=plt.hist(mujerestotal,bin_mt,color="w",edgecolor="r")
#gauss
p=promedio_mt
x=np.linspace(min(mujerestotal),max(mujerestotal),1000)
y=len(mujerestotal)*np.exp(-np.power(x-p,2)/(2*np.power(des,2)))/(np.sqrt(2*math.pi*des))
plt.plot(x,y,color="b")
#decoracion
media="media = "+str(promedio_mt)
moda="moda = "+str(moda_mt)
mediana="mediana = "+str(mediana_mt)
plt.axvline(promedio_mt,color="b",linestyle="dashed",linewidth=1.5,label=media)
plt.axvline(moda_mt,color="g",linestyle=":",linewidth=1.5,label=moda)
plt.axvline(mediana_mt,color="black",linestyle="-.",linewidth=1.5,label=mediana)
plt.xlabel("peso")
plt.ylabel("personas")
plt.axis([30,110,0,220]) 
plt.suptitle("datos de todos las mujeres")
title="numero de valores= " +str(len(total)) +"   bin = 3 kg"
plt.title(title)
legend=plt.legend(loc="upper right",prop={"size":"x-small"})

plt.text(95,130,"sigma ="+dese[0:5],fontsize=10)
plt.text(70.5,140,"media+sigma",fontsize=7,color="m",rotation="vertical")
plt.text(80,140,"media+2sigma",fontsize=7,color="m",rotation="vertical")
plt.text(90,140,"media+3sigma",fontsize=7,color="m",rotation="vertical")
plt.text(39,140,"media-2sigma",fontsize=7,color="m",rotation="vertical")
plt.text(49,140,"media-1sigma",fontsize=7,color="m",rotation="vertical")
plt.text(32,140,"media-3sigma",fontsize=7,color="m",rotation="vertical")


for i in range(1,4):
	plt.axvline(p+des*i,color="m",linestyle="-",linewidth=0.5)
	plt.axvline(p-des*i,color="m",linestyle="-",linewidth=0.5)
#pdf_pages.savefig()

#pdf_pages.close()

#pregunta 4 calculo de chi2
"""
t=input("0-hombrestotal  1-mujerestotal   2-total")
u=[hombrestotal,mujerestotal,total]
promedio_mt= np.mean(u[t])
des=np.std(u[t])
def integrand(x,des,promedio_mt):
	return (1/math.sqrt(2*math.pi*math.pow(des,2)))*math.exp((-0.5*math.pow(x-promedio_mt,2))/math.pow(des,2))
c=[]
e=0
for i in range(22):
	a=42+4*i
	b=45+4*i
	p_3=integrate.quad(integrand,a,b,args=(des,promedio_mt))
	c.append(p_3[0]*len(u[t]))
if t==1:
	m=[34,103,142,200,179,173,145,123,92,66,29,26,29]
	for i in range(len(m)):
		d=math.pow(m[i]-c[i],2)/c[i]
		e=e+d
if t==0:
	m=[10,7,19,73,73,95,138,193,155,126,95,69,69,60,24,21]
	for i in range(len(m)):
		d=math.pow(m[i]-c[i],2)/c[i]
		e=e+d
if t==2:
	m=[35,115,146,215,212,242,227,223,273,231,177,150,173,96,58,77,58]
	for i in range(len(m)):
		d=math.pow(m[i]-c[i],2)/c[i]
		e=e+d
print(e)
"""
def gaussiana(x,mu,sigma):
	return(1/math.sqrt(2*math.pi*math.pow(des,2)))*math.exp((-0.5*math.pow(x-promedio_mt,2))/math.pow(des,2))

for i in range(22):
	a=42+4*i
	b=45+4*i
	p_3=integrate.quad(gaussiana,a,b,args=(des,promedio_mt))
print (n)
