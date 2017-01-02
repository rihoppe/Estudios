
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
pdf_pages = PdfPages("tarea1_todostodos.pdf")
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

#parte 1 


	#graficos personas/peso
	"""
	#hombres
	#promedio
	promedio_m = np.mean(machos)
	#mediana
	mediana_m = np.median(machos)
	#moda
	moda_m=modas(machos)
	#grafico
	bin_m=np.arange(min(machos),max(machos)+3,3)
	fig=plt.figure(dpi=100)
	plt.hist(machos,bin_m,color="w",edgecolor="b")
	media="media = "+str(promedio_m)
	moda="moda = "+str(moda_m)
	mediana="mediana = "+str(mediana_m)
	plt.axvline(promedio_m,color="r",linestyle="dashed",linewidth=1.5,label=media)
	plt.axvline(moda_m,color="g",linestyle=":",linewidth=1.5,label=moda)
	plt.axvline(mediana_m,color="black",linestyle="-.",linewidth=1.5,label=mediana)
	titulo= "numero de valores= " +str(len(machos)) +"   bin = 3 kg"
	subtitulo="datos de los hombres de "+ str(grupo) 
	plt.title(titulo)
	plt.suptitle(subtitulo)
	plt.xlabel("peso")
	plt.ylabel("personas")
	plt.axis([48,105,0,15])
	legend=plt.legend(loc="upper right",prop={"size":"x-small"})
	pdf_pages.savefig()

	"""
	"""
	#mujeres

	#promedio
	promedio_h= np.mean(hembras)
	#mediana
	mediana_h = np.median(hembras)
	#moda
	moda_h=modas(hembras)
	#grafico
	bin_h=np.arange(min(hembras),max(hembras)+3,3)
	fig=plt.figure(dpi=100)
	plt.hist(hembras,bin_h,color="w",edgecolor="m")
	media="media = "+str(promedio_h)
	moda="moda = "+str(moda_h)
	mediana="mediana = "+str(mediana_h)
	plt.axvline(promedio_h,color="b",linestyle="dashed",linewidth=1.5,label=media)
	plt.axvline(moda_h,color="g",linestyle=":",linewidth=1.5,label=moda)
	plt.axvline(mediana_h,color="black",linestyle="-.",linewidth=1.5,label=mediana)
	titulo= "numero de valores= " +str(len(hembras)) +"   bin = 3 kg"
	subtitulo="datos de las mujeres de "+ str(grupo) 
	plt.title(titulo)
	plt.suptitle(subtitulo)
	plt.xlabel("peso")
	plt.ylabel("personas")
	plt.axis([39,103,0,15])
	legend=plt.legend(loc="upper right",prop={"size":"x-small"})
	pdf_pages.savefig()

	"""
total=hombrestotal+mujerestotal
print(len(mujerestotal))
print(len(hombrestotal))


#parte 2



"""
#grafico hombres total

des=np.std(total)
#promedio
promedio_mt= np.mean(total)
#mediana
mediana_mt = np.median(total)
#moda
moda_mt=modas(total)+1.5
#grafico
bin_mt=np.arange(min(total),max(total)+3,3)
fig=plt.figure(dpi=100)
fit=norm.pdf(total,np.mean(total),np.std(total))
plt.plot(total,fit,linestyle="--",linewidth=1)
plt.hist(total,bin_mt,color="w",edgecolor="r")
media="media = "+str(promedio_mt)
moda="moda = "+str(moda_mt)
mediana="mediana = "+str(mediana_mt)
plt.axvline(promedio_mt,color="b",linestyle="dashed",linewidth=1.5,label=media)
plt.axvline(moda_mt,color="g",linestyle=":",linewidth=1.5,label=moda)
plt.axvline(mediana_mt,color="black",linestyle="-.",linewidth=1.5,label=mediana)
plt.xlabel("peso")
plt.ylabel("personas")
plt.axis([39,111,0,250]) 
plt.suptitle("datos de todas las personas")
title="numero de valores= " +str(len(total)) +"   bin = 3 kg"
plt.title(title)
legend=plt.legend(loc="upper right",prop={"size":"x-small"})
des=np.std(total)
dese=str(des)
plt.text(92,190,"sigma ="+dese[0:5],fontsize=10)
plt.text(81,125,"media+sigma",fontsize=7,color="m",rotation="vertical")
plt.text(54,125,"media-sigma",fontsize=7,color="m",rotation="vertical")
plt.text(41,125,"media-2sigma",fontsize=7,color="m",rotation="vertical")
plt.text(94.5,125,"media+2sigma",fontsize=7,color="m",rotation="vertical")
plt.text(107,125,"media+3sigma",fontsize=7,color="m",rotation="vertical")
#plt.text(42,125,"media-3sigma",fontsize=7,color="m",rotation="vertical")
for i in range(1,4):
	label1= str(promedio_mt)+"+"+ str(i)
	plt.axvline(promedio_mt+des*i,color="m",linestyle="-",linewidth=1)
	label2= str(promedio_mt)+"-"+ str(i) 
	plt.axvline(promedio_mt-des*i,color="m",linestyle="-",linewidth=1)
pdf_pages.savefig()
"""

#parte 3

"""
#tomo las variables
promedio_mt= np.mean(total)
des=np.std(total)
#creo los intervalos [-inf,f,d,b,a,c,e,inf]
a=promedio_mt+des
b=promedio_mt-des
c=promedio_mt+2*des
d=promedio_mt-2*des
e=promedio_mt+3*des
f=promedio_mt-3*des
tres=0
dos=0
uno=0

for i in range(len(total)):
	if total[i]>=f:
		if total[i]>=d:
			if total[i]>=b:
				if total[i]>=a:
					if total[i]>=c:
						if total[i]>=e:
#		[inf,f,d,b,a,c,e,inf]					
							print("mayor que promedio+3sigma")
						else:
							tres=tres+1
					else:
						dos=dos+1
				else:
					uno=uno+1
			else:
				dos=dos+1
		else:
			tres=tres+1
	print("menor que promedio-3sigma")
tres=tres+dos+uno
dos=dos+uno
print("3:"+str(tres)+"  2:"+str(dos)+"  1:"+str(uno))
print(len(total))
"""

