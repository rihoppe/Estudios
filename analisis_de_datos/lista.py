import os

os.chdir(
"/home/rai/Desktop/analisis_de_datos/tarea_4")
Dcal=os.listdir(
"/home/rai/Desktop/analisis_de_datos/tarea_4")
archivo=open("1","w")
for i in range(len(Dcal)):
	archivo.write(str(Dcal[i])+ "")
