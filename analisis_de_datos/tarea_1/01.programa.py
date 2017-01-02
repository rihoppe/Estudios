#librerias
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
#variables utilizadas
hombres=[]
machos=[]
hembras=[]
mujeres=[]
#toma de datos y agrupacion por hombres y mujeres
os.chdir("/home/rai/Desktop/intro. al analisis de datos/personas")
datosp=os.listdir("/home/rai/Desktop/intro. al analisis de datos/personas")
for w in range(len(datosp)):
	print (str(w) +" - "+ datosp[w])
grupo=datosp[int(input("elija el archivo: "))]
pdf_pages = PdfPages(grupo-".dat"+".pdf")
#pdf_pages = PdfPages("tarea1.pdf")
#for c in range(len(datosp)):
#	print (str(c) +" - "+ datosp[c])
#	grupo=datosp[c]
	dato=open(grupo,"r")
	contenido= dato.readlines()
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
	fig=plt.figure(figsize=(8.27,11.69),dpi=100)
	#primer grafico personas/peso para hombres y mujeres
	bin=input("elija bin: ",10)
	xi=input("elija x inicial: ",50)
	xf=input("elija x final: ",110)
	yi=input("elija y inicial: ",0)
	yf=input("elija y final: ",16)
	plt.hist(machos,bin)
	plt.xlabel("peso")
	plt.ylabel("personas")
	plt.axis([xi,xf,yi,yf])
	#plt.show()
	pdf_pages.savefig()
pdf_pages.close()
 

