#librerias
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
#creacion del documento
os.chdir("/home/rai/Desktop/intro. al analisis de datos/personas")
datoss=os.listdir("/home/rai/Desktop/intro. al analisis de datos/personas")
pdf_pages = PdfPages("tarea1.pdf")
fig=plt.figure(figsize=(8.27,11.69),dpi=100)
po=0
for c,l in zip(range(23),range(221,225)):
	print(str(c) +"-"+ str(l))
	if po==2:
		po=0
		if l==2:
			pdf_pages.savefig()
	#variables utilizadas
	hombres=[]
	mujeres=[]
	#toma de datos y agrupacion por hombres y mujeres
 	print (str(c) +" - "+ datoss[c])
	grupo=datoss[c]
	dato=open(grupo,"r")
	contenido= dato.readlines()
	for h in range(51,101):
		hombres.append(contenido[h])
	for i in range(50):
		mujeres.append(contenido[i])
 		if len(mujeres[i])==5:
  			mujeres[i]=int(mujeres[i][0:3])
 		if len(hombres[i])==5:
  			hombres[i]=int(hombres[i][0:3])
	
 		else:
  			mujeres[i]=int(mujeres[i][0:2])
  			hombres[i]=int(hombres[i][0:2]) 
		print(hombres)
		print(mujeres)
		ax=fig.add_subplot(l)
		#primer grafico personas/peso para hombres y mujeres
		ax.hist(hombres,12)
		ax.xlabel("peso")
		ax.ylabel("personas")
		ax.axis([50,110,0,16])
	po=po+1
pdf_pages.close()

