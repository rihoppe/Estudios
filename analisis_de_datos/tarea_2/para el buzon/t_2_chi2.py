import math
import os
import numpy as np
import matplotlib.pylab as plt
from matplotlib.backends.backend_pdf import PdfPages
import scipy.integrate as integrate
os.chdir(
"/home/rai/Desktop/intro. al analisis de datos/tarea 2")
Dcal=os.listdir(
"/home/rai/Desktop/intro. al analisis de datos/tarea 2/datos absolutos")
Dcal=sorted(Dcal)

#toma de datos
def obpesos(n,tipo,tipo2=""):
	l=[]
	os.chdir(
	"/home/rai/Desktop/intro. al analisis de datos/tarea 2/datos absolutos")
	dato=open(Dcal[n],"r")
	contenido= dato.readlines()
	os.chdir(
	"/home/rai/Desktop/intro. al analisis de datos/tarea 2")
	for i in range(len(contenido)):
		P=contenido[i].split(" ")
		if tipo2=="":
			if P.count(tipo)==1:
				l.append(float(P[4]))
		else:
			if P.count(tipo)==1:
				if P.count(tipo2)==1:
					l.append(float(P[4]))
				
	return l

def todostipo(tipo,tipo2=""):
	l=[]
	for i in range(len(Dcal)):
		a=obpesos(i,tipo,tipo2)
		if len(a)!=0:
			for e in range(len(a)):
				l.append(float(a[e]))
	return l
hombres=todostipo("M","E")
mujeres=todostipo("F","E")
hombres1=obpesos(0,"M","E")
mujeres1=obpesos(0,"F","E")
hombres2=obpesos(1,"M","E")
mujeres2=obpesos(1,"F","E")
hombres3=obpesos(2,"M","E")
mujeres3=obpesos(2,"F","E")
hombres4=obpesos(3,"M","E")
mujeres4=obpesos(3,"F","E")
hombres5=obpesos(4,"M","E")
mujeres5=obpesos(4,"F","E")
hombres6=obpesos(5,"M","E")
mujeres6=obpesos(5,"F","E")
hombres7=obpesos(6,"M","E")
mujeres7=obpesos(6,"F","E")
hombres8=obpesos(7,"M","E")
mujeres8=obpesos(7,"F","E")


#creacion de los histogramas
def gaussiana(x,mu,sigma):
	return(1/math.sqrt(2*math.pi*math.pow(sigma,2)))*math.exp((-0.5*math.pow(x-mu,2))/math.pow(sigma,2))



def histograma(datos):
	des=np.std(datos)
	promedio= np.mean(datos)
	binn=np.arange(min(datos),max(datos)+2.5,2.5)
	fig=plt.figure(dpi=100)
	n,ho,he=plt.hist(datos,binn,color="w",edgecolor="r")
	#plt.show()
	#gauss
	p=promedio
	j=[]
	cd=[]
	for e in range(len(n)):
		a=min(datos)+2.5*e
		b=min(datos)+2.5*(e+1)
		p_3=integrate.quad(gaussiana,a,b,args=(p,des))
		cd.append(p_3[0]*len(datos))
	for i in range(len(cd)):
		d=cd[i]
		for c in range(cd[i]):
			j.append(min(datos)+1+2.5*i)
	ne,her,hir=plt.hist(j,binn,color="w",edgecolor="b",alpha = 0.65)
	#plt.show()
	u=0
	for e in range(len(n)):
		d=math.pow(int(n[e])-cd[e],2)/cd[e]
		u=u+d
	u=round(u,2)
	print("promedio= "+str(round(p,2))+"  desviacion= "+
	str(round(des,2))+"  chi2="+str(u)+ "   numero de datos= "+str(len(datos)))
"""
print("todos hombres")
histograma(hombres)
print("todos mujeres")
histograma(mujeres)
print("hobres grupo 1")
histograma(hombres1)
print("mujeres grupo 1")
histograma(mujeres1)
print("hobres grupo 2")
histograma(hombres2)
print("mujeres grupo 2")
histograma(mujeres2)
print("hobres grupo 3")
histograma(hombres3)
print("mujeres grupo 3")
histograma(mujeres3)
print("hobres grupo 4")
histograma(hombres4)
print("mujeres grupo 4")
histograma(mujeres4)
print("hobres grupo 5")
histograma(hombres5)
print("mujeres grupo 5")
histograma(mujeres5)
print("hobres grupo 6")
histograma(hombres6)
print("mujeres grupo 6")
histograma(mujeres6)
print("hobres grupo 7")
histograma(hombres7)
print("mujeres grupo 7")
histograma(mujeres7)
print("hobres grupo 8")
histograma(hombres8)
print("mujeres grupo 8")
histograma(mujeres8)
"""
def errores(datos):
	a=np.std(datos)
	b=np.sqrt(len(datos))	
	return a/(np.sqrt(1500))
#pregunta 5

hac=todostipo("AC","M")
fac=todostipo("AC","F")
hdc=todostipo("DC","M")
fdc=todostipo("DC","F")
print("promedio hombres AD:" +str(np.mean(hac)))
print("error hombres AD:" +str(errores(hac)))
print("promedio mujeres AD:" +str(np.mean(fac)))
print("error hombres DC:"+str(errores(fac)))
print("promedio hombres DC:" +str(np.mean(hdc)))
print("error mujeres AD:"+str(errores(hdc)))
print("promedio mujeres DC:" +str(np.mean(fdc)))
print("error mujeres DC:"+str(errores(fdc)))

