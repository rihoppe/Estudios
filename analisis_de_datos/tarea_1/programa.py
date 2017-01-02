#librerias
import numpy as np
import matplotlib.pyplot as plt
#variables utilizadas
hombres=[]
mujeres=[]
pesoM=[]
pesoF=[]
pe=0
#toma de datos y agrupacion por hombres y mujeres
grupo=raw_input("elija un archivo ")
dato=open(grupo,"r")
contenido= dato.readlines()
for i in range(len(contenido)):
 if contenido[i].count("F") == 1:
  mujeres.append(contenido[i])
  pe=pe+1
 else:
  hombres.append(contenido[i])
for a in range(pe):
   mujeres[a]=mujeres[a].split(" ")
   pesoF.append(int(mujeres[a][4]))
for b in range(len(contenido)-pe):
   hombres[b]=hombres[b].split(" ")
   pesoM.append(int(hombres[b][4]))
#######


#primer grafico personas/peso para hombres y mujeres
plt.hist(pesoM,7)
plt.xlabel("peso")
plt.ylabel("personas")
plt.axis([50,110,0,11])
plt.show()

 

