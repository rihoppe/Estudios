#librerias
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
#variables utilizadas
hombres=[]
machos=[]
hombrestotal=[]
hembras=[]
mujeres=[]
mujerestotal=[]
#toma de datos y agrupacion por hombres y mujeres
os.chdir("/home/rai/Desktop/intro. al analisis de datos")
datosp=os.listdir("/home/rai/Desktop/intro. al analisis de datos/personas")
pdf_pages = PdfPages("tarea1_hombres.pdf")
for c in range(len(datosp)):
	print (str(c) +" - "+ datosp[c])
	grupo=datosp[c]
	os.chdir("/home/rai/Desktop/intro. al analisis de datos/personas")
	dato=open(grupo,"r")
	contenido= dato.readlines()
	os.chdir("/home/rai/Desktop/intro. al analisis de datos")
	for h in range(51,101):
		hombres.append(str(contenido[h]))
	for g in range(50):
		mujeres.append(str(contenido[g]))

	for i in range(50):
		if len(str(hombres[i]))==5 or len(str(hombres[i]))==3:
			machos.append(int(hombres[i][0:3]))
		else:
		 machos.append(int(hombres[i][0:2]))
		if len(str(mujeres[i]))==5 or len(str(mujeres[i]))==3:
			hembras.append(int(mujeres[i][0:3]))
		else:
	 	 hembras.append(int(mujeres[i][0:2]))
	mujerestotal=mujerestotal+hembras
	hombrestotal=hombrestotal+machos
	fig=plt.figure(figsize=(8.27/2,11.69/2),dpi=100)
	#primer grafico personas/peso para hombres y mujeres
	plt.hist(machos,bins=13)
	plt.xlabel("peso")
	plt.ylabel("personas")
	plt.axis([45,110,0,14])
	pdf_pages.savefig()
	hombres=[]
	machos=[]
	hembras=[]
	mujeres=[]
suma=0
total=hombrestotal+mujerestotal
for i in range(len(hombrestotal)):
	suma=suma+hombrestotal[i]
promedio_t=suma/len(hombrestotal)
bin_t=np.arange(min(hombrestotal),max(hombrestotal)+3,3)
fig=plt.figure(figsize=(8.27/2,11.69/2),dpi=100)
plt.hist(hombrestotal,bin_t,color="w",edgecolor="r")
media="media = "+str(promedio_t)
desviacion="desviacion = "+str(50)
mediana="mediana = "+str(60)
plt.axvline(promedio_t,color="b",linestyle="dashed",linewidth=1.5,label=media)
plt.axvline(50,color="g",linestyle=":",linewidth=1.5,label=desviacion)
plt.axvline(60,color="black",linestyle="-.",linewidth=1.5,label=mediana)
plt.suptitle("datos de todos los hombres")
plt.xlabel("peso")
plt.ylabel("personas")
plt.axis([45,105,0,180])
legend=plt.legend(loc="upper right",prop={"size":"x-small"})
pdf_pages.savefig()
#plt.show() 
pdf_pages.close()
