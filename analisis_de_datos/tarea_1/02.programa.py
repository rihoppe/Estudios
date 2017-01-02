#librerias
import os
import numpy as np
import matplotlib.pyplot as plt
#variables utilizadas
hombres=[]
mujeres=[]
#toma de datos y agrupacion por hombres y mujeres
os.chdir("/home/rai/Desktop/intro. al analisis de datos/datos personas")
datosp=os.listdir("/home/rai/Desktop/intro. al analisis de datos/datos personas")
for c in range(len(datosp)):
 print (str(c) +" - "+ datosp[c])
grupo=datosp[c]
dato=open(grupo,"r")
contenido= dato.readlines()
for h in range(51,101):
 hombres.append(contenido[h])
for i in range(50):
 mujeres.append(contenido[i])
 if len(hombres[i])==5:
  print(mujeres[i])
  mujeres[i]=int(mujeres[i][0:3])
  hombres[i]=int(hombres[i][0:3])
 else:
  mujeres[i]=int(mujeres[i][0:2])
  hombres[i]=int(hombres[i][0:2])

#primer grafico personas/peso para hombres y mujeres
plt.hist(hombres,12)
plt.xlabel("peso")
plt.ylabel("personas")
plt.axis([50,110,0,16])
plt.show()

 

