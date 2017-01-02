from __future__ import division
import math
import os
import numpy as np
import matplotlib.pylab as plt
from matplotlib.backends.backend_pdf import PdfPages
import scipy.integrate as integrate
from scipy.integrate import quad
from scipy.special import gamma,beta 
from scipy.stats import pearsonr
from math import *

#chi2 ralidad vs realidad
parte1 = False
#student poblaciones hombres y mujeres
parte2 = False
#student AC y DC
parte3 = False
#correlacion edad
parte4 = True
#correlacion hora
parte5 = False
#correlacion final
parte6 = False

os.chdir(
"/home/rai/Desktop/intro. al analisis de datos/tarea 2")
Dcal=os.listdir(
"/home/rai/Desktop/intro. al analisis de datos/tarea 2/datos absolutos2")
Dcal=sorted(Dcal)

#toma de datos
def obpesos(n,tipo,tipo2="",tipo3="",agregado=""):
	l=[]
	os.chdir(
	"/home/rai/Desktop/intro. al analisis de datos/tarea 2/datos absolutos2")
	dato=open(Dcal[n],"r")
	contenido= dato.readlines()
	os.chdir(
	"/home/rai/Desktop/intro. al analisis de datos/tarea 2")
	for i in range(len(contenido)):
		P=contenido[i].split(" ")
		if tipo3=="":
			if tipo2=="":
				if P.count(tipo)==1:
					if agregado=="edad":
						y=[float(P[4]),P[5],P[1]]
						l.append(y)
					elif agregado=="hora":
						y=[float(P[4]),P[5],P[6]]
						l.append(y)
					else:
						l.append(float(P[4]))
			else:
				if P.count(tipo2)==1:
					if P.count(tipo)==1:
						if agregado=="edad":
							y=[float(P[4]),P[5],P[1]]
							l.append(y)
						elif agregado=="hora":
							y=[float(P[4]),P[5],P[6]]
							l.append(y)
						else:
							l.append(float(P[4]))
		
		else:
			if P.count(tipo3)==1:
				if P.count(tipo)==1:
					if P.count(tipo2)==1:
						if agregado=="edad":
							y=[float(P[4]),P[5],P[1]]
							l.append(y)
						elif agregado=="hora":
							y=[float(P[4]),P[5],P[6]]
							l.append(y)
						else:
							l.append(float(P[4]))
				
	return l

def todostipo(tipo,tipo2="",tipo3=""):
	l=[]
	for i in range(len(Dcal)):
		a=obpesos(i,tipo,tipo2,tipo3)
		if len(a)!=0:
			for e in range(len(a)):
				l.append(float(a[e]))
	return l
	
def histograma(n,sexo):
	indice=histmaxdat(sexo)
	datos=obpesos(n,"E",sexo)
	datos2=obpesos(indice,"E",sexo)
	if min(datos)>=min(datos2):
		mini=min(datos2)
	else:
		mini=min(datos)
	if max(datos)>=max(datos2):
		maxi=max(datos)
	else:
		maxi=max(datos2)
	bin1=np.arange(mini,maxi+2.5,2.5)
	fig=plt.figure(dpi=100)
	n1,ho1,he1=plt.hist(datos,bin1,color="w",edgecolor="r")
	n2,ho2,he2=plt.hist(datos2,bin1,color="w",edgecolor="b",alpha=0.70)
	#plt.show()
	u=0
	for e in range(len(n1)):
		if (n2[e]+n1[e])!=0:
			d=((n1[e]-n2[e])**2)/(n2[e]+n1[e])
			u=u+d
	u=round(u,2)

	print("chi2="+str(u)+ "   numero de bines= "+str(len(n1)))
	print("bines 2"+str(len(n2)))


def histmaxdat(sexo):
	os.chdir(
	"/home/rai/Desktop/intro. al analisis de datos/tarea 2/datos absolutos")
	Dcal=os.listdir(
	"/home/rai/Desktop/intro. al analisis de datos/tarea 2/datos absolutos")
	Dcal=sorted(Dcal)
	a=[]
	b=[]
	for i in range (len(Dcal)):
		m=obpesos(i,"E",sexo)
		a.append(len(m))
	return a.index(max(a))
if parte1==True:
	a=input("1-hombres  2-mujeres  ")-1
	b=["M","F"]
	sexo=b[a]
	for i in range(8):
		if i!=histmaxdat(sexo):
			print(i+1)
			print("hist comparado 2:"+str(histmaxdat(sexo)+1))
			histograma(i,sexo)
def student(n,sexo,tipo=""):
	indice=histmaxdat(sexo)
	datos=obpesos(n,"E",sexo)
	datos2=obpesos(indice,"E",sexo)
	prom1=np.mean(datos)
	prom2=np.mean(datos2)
	S=obS(n,sexo,tipo)
	if prom2>prom1:
		t=(prom2-prom1)/S
	else:
		t=(prom1-prom2)/S
	return t
	
def obS(n,sexo,tipo2=""):
	indice=histmaxdat(sexo)
	datos=obpesos(n,"E",sexo,tipo2)
	datos2=obpesos(indice,"E",sexo,tipo2)
	prom1=np.mean(datos)
	prom2=np.mean(datos2)
	a=0
	for i in range(len(datos)):
		o=(datos[i]-prom1)**2
		a+=o
	b=0
	for g in range(len(datos2)):
		u=(datos2[g]-prom2)**2
		b+=u
	x=len(datos)
	y=len(datos2)
	print("grado de libertad "+str(x+y-2))
	s=math.sqrt(((a+b)/(x+y-2))*((1/x)+(1/y)))
	return s
	
def teni_chi(x,v):
	def func(x):
		y=v/2
		return (x**(y-1)*exp(-x/2))/(2**(y)*gamma(y))
	return integrate(func,x,np.inf)[0]
def oblib(i,sexo):
	indice=histmaxdat(sexo)
	datos=obpesos(i,"E",sexo)
	datos2=obpesos(indice,"E",sexo)
	x=len(datos)
	y=len(datos2)
	return x+y-2
	
def tdis(t,v):
	def func(x,v):
		y=v
		return (1+(x**2)/y)**(y/2+1/2)
	a=(1/v**0.5)
	b=(1/beta(1/2,v/2))
	c=integrate(func,-t,t)[0]
	return a*b*c	
	#return (1/v**0.5)*(1/beta(1/2,v/2))*integrate(func,-t,t)[0]
	
if parte2==True:
	a=input("1-hombres  2-mujeres  ")-1
	b=["M","F"]
	sexo=b[a]
	for i in range(8):
		if i!=histmaxdat(sexo):
			print(1+i)
			print("hist comparado 2:"+str(histmaxdat(sexo)+1))
			t=student(i,sexo)
			print(t)
			v=oblib(i,sexo)
			#print(tdis(t,v))
def p3_student(sexo):
	datos=todostipo(sexo,"AC","E")
	datos2=todostipo(sexo,"DC","E")
	prom1=np.mean(datos)
	prom2=np.mean(datos2)
	S=p3_obS(sexo)
	if prom2>prom1:
		t=(prom2-prom1)/S
	else:
		t=(prom1-prom2)/S
	return t
	
def p3_obS(sexo):
	datos=todostipo(sexo,"AC")
	datos2=todostipo(sexo,"DC")
	prom1=np.mean(datos)
	prom2=np.mean(datos2)
	a=0
	for i in range(len(datos)):
		o=(datos[i]-prom1)**2
		a+=o
	b=0
	for g in range(len(datos2)):
		u=(datos2[g]-prom2)**2
		b+=u
	x=len(datos)
	y=len(datos2)
	print("grado de libertad "+str(x+y-2))
	s=math.sqrt(((a+b)/(x+y-2))*((1/x)+(1/y)))
	return s
	
if parte3==True:
	ho=input("1-hombres  2-mujeres  ")-1
	he=["M","F"]
	sexo=he[ho]
	print(p3_student(sexo))

def obRMS(x,y,a,b):
	
	RMS2=0
	for i in range(len(x)):
		c=y[i]-(a*x[i]+b)
		RMS2+=(c**2)
	RMS=RMS2/len(x)
	return np.sqrt(RMS)
			
def pearson(x,y):
		largo=len(x)
		a=0
		l=0
		n=0
		j=0
		pe=0
		po=0
		for i in range(largo):		
			m=x[i]*y[i]
			l+=x[i]
			n+=y[i]
			j=x[i]**2
			r=y[i]**2
			a+=m
			po+=j
			pe+=r
		a=largo*a
		b=n*l
		c=np.sqrt((largo*po)-(l**2))
		d=np.sqrt((largo*pe)-(n**2))
		return (a-b)/(b*c)

if parte4==True:
	ho=input("1-hombres  2-mujeres  ")-1
	he=["M","F"]
	sexo=he[ho]
	x1=[]
	y1=[]
	err1=[]
	y2=[]
	x2=[]
	err2=[]
	for i in range(8):
		a=obpesos(i,sexo,"E","","edad")
		for e in range(len(a)):
			x1.append(float(a[e][2]))
			y1.append(float(a[e][0]))
			err1.append(float(a[e][1]))
	x=np.array(x1)
	y=np.array(y1)
	a,b=np.polyfit(x,y,1)
	RMS=obRMS(x1,y1,a,b)
	plt.figure()
	xarray=np.arange(12,73,0.1)
	polyfit=xarray*a+b
	yarray1=(xarray*a+b)+RMS
	yarray10=(xarray*a+b)-RMS
	yarray2=(xarray*a+b)+2*RMS
	yarray20=(xarray*a+b)-2*RMS
	yarray3=(xarray*a+b)+3*RMS
	yarray30=(xarray*a+b)-3*RMS
	plt.plot(xarray,polyfit,"g--")
	plt.plot(xarray,yarray1,"r--")
	plt.plot(xarray,yarray10,"r--")
	plt.plot(xarray,yarray2,"r--",alpha=0.8)
	plt.plot(xarray,yarray20,"r--",alpha=0.8)
	plt.plot(xarray,yarray3,"r--",alpha=0.6)
	plt.plot(xarray,yarray30,"r--",alpha=0.6)
	plt.plot(x1,y1,"bo")
	if sexo=="M":
		plt.axis([12,73,38,130])
	else:
		plt.axis([12,65,30,100])
	#plt.show()
	
	#segunda iteracion para quitar outlayers
	for i in range(len(y1)):
		if y1[i]<=(a*x1[i]+b+3*RMS):
			y2.append(y1[i])
			x2.append(x1[i])
			err2.append(err1[i])
	x=np.array(x2)
	y=np.array(y2)
	a,b=np.polyfit(x,y,1)
	RMS=obRMS(x2,y2,a,b)
	plt.figure()
	xarray=np.arange(12,73,0.1)
	polyfit=xarray*a+b
	yarray1=(xarray*a+b)+RMS
	yarray10=(xarray*a+b)-RMS
	yarray2=(xarray*a+b)+2*RMS
	yarray20=(xarray*a+b)-2*RMS
	yarray3=(xarray*a+b)+3*RMS
	yarray30=(xarray*a+b)-3*RMS
	plt.plot(xarray,polyfit,"g--")
	plt.plot(xarray,yarray1,"r--")
	plt.plot(xarray,yarray10,"r--")
	plt.plot(xarray,yarray2,"r--",alpha=0.8)
	plt.plot(xarray,yarray20,"r--",alpha=0.8)
	plt.plot(xarray,yarray3,"r--",alpha=0.6)
	plt.plot(xarray,yarray30,"r--",alpha=0.6)
	plt.plot(x2,y2,"bo")
	plt.errorbar(x2,y2,yerr=err2,fmt=".k",elinewidth=0.4,ecolor="black",color="b")
	plt.xlabel("Edad")
	plt.ylabel("Pesos")
	if sexo=="M":
		plt.axis([12,73,38,130])
		titulo="Edad vs Pesos: Hombres"
	else:
		plt.axis([12,65,30,100])	
		titulo="Edad vs Pesos: Mujeres"
	print("la recta: "+str(round(a,2))+"*x + "+str(round(b,2)))
	print("pearson:"+str(pearson(x2,y2)))
	print("pearson de scipy:  "+str(pearsonr(x,y)[0])+"  "+
	str(pearsonr(x,y)[1]))
	plt.title(titulo)
	plt.show()
if parte5==True:
	ho=input("1-hombres  2-mujeres  ")-1
	he=["M","F"]
	sexo=he[ho]
	x1=[]
	y1=[]
	err1=[]
	x2=[]
	y2=[]
	err2=[]
	for i in range(8):
		a=obpesos(i,sexo,"E","","hora")
		for e in range(len(a)):
			holiwi=a[e][2]
			if holiwi>=13:
				x1.append(float(a[e][2]))
				y1.append(float(a[e][0]))
				err1.append(float(a[e][1]))
	x=np.array(x1)
	y=np.array(y1)
	a,b=np.polyfit(x,y,1)
	RMS=obRMS(x1,y1,a,b)
	plt.figure()
	xarray=np.arange(12.5,16,0.1)
	polyfit=xarray*a+b
	yarray1=(xarray*a+b)+RMS
	yarray10=(xarray*a+b)-RMS
	yarray2=(xarray*a+b)+2*RMS
	yarray20=(xarray*a+b)-2*RMS
	yarray3=(xarray*a+b)+3*RMS
	yarray30=(xarray*a+b)-3*RMS
	plt.plot(xarray,polyfit,"g--")
	plt.plot(xarray,yarray1,"r--")
	plt.plot(xarray,yarray10,"r--")
	plt.plot(xarray,yarray2,"r--",alpha=0.8)
	plt.plot(xarray,yarray20,"r--",alpha=0.8)
	plt.plot(xarray,yarray3,"r--",alpha=0.6)
	plt.plot(xarray,yarray30,"r--",alpha=0.6)
	plt.plot(x1,y1,"bo")
	if sexo=="M":
		plt.axis([12.7,15.2,40,130])
	else:
		plt.axis([12.7,15.2,37,85])
	#plt.show()
	
	#segunda iteracion para quitar outlayers
	for i in range(len(y1)):
		if y1[i]<=(a*x1[i]+b+3*RMS):
			y2.append(y1[i])
			x2.append(x1[i])
			err2.append(err1[i])
	x=np.array(x2)
	y=np.array(y2)
	a,b=np.polyfit(x,y,1)
	RMS=obRMS(x2,y2,a,b)
	plt.figure()
	xarray=np.arange(12,73,0.1)
	polyfit=xarray*a+b
	yarray1=(xarray*a+b)+RMS
	yarray10=(xarray*a+b)-RMS
	yarray2=(xarray*a+b)+2*RMS
	yarray20=(xarray*a+b)-2*RMS
	yarray3=(xarray*a+b)+3*RMS
	yarray30=(xarray*a+b)-3*RMS
	plt.plot(xarray,polyfit,"g--")
	plt.plot(xarray,yarray1,"r--")
	plt.plot(xarray,yarray10,"r--")
	plt.plot(xarray,yarray2,"r--",alpha=0.8)
	plt.plot(xarray,yarray20,"r--",alpha=0.8)
	plt.plot(xarray,yarray3,"r--",alpha=0.6)
	plt.plot(xarray,yarray30,"r--",alpha=0.6)
	plt.plot(x2,y2,"bo")
	plt.errorbar(x2,y2,yerr=err2,fmt=".k",elinewidth=0.4,ecolor="black",color="b")
	plt.xlabel("Hora")
	plt.ylabel("Pesos")
	if sexo=="M":
		titulo="Hora vs Pesos: Hombres"
		plt.axis([12.7,15.2,40,130])
	else:
		plt.axis([12.7,15.2,37,85])
		titulo="Hora vs Pesos: Mujeres"
	print("la recta: "+str(round(a,2))+"*x + "+str(round(b,2)))
	print("pearson:"+str(pearson(x2,y2)))
	print("pearson de scipy:  "+str(pearsonr(x,y)[0])+"  "+
	str(pearsonr(x,y)[1]))
	plt.title(titulo)
	plt.show()


