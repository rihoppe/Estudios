#librerias, directorio y pdf 
import os
import numpy as np
import matplotlib.pylab as plt
from matplotlib.backends.backend_pdf import PdfPages

pdftabla=False
mostrarayb=False
creardatosabsolutos=True
graficosayb=False

os.chdir("/home/rai/Desktop/intro. al analisis de datos/tarea 2")
#Dcal=lista con los nombres de los archivos con los datos
Dcal=os.listdir("/home/rai/Desktop/intro. al analisis de datos/tarea 2/calibraciones")
Dcal=sorted(Dcal)
pdf_pages = PdfPages("tablagrande.pdf")



#obtencion de datos:
""" od(n):
od(n) toma al archivo numero n de la lista Dcal y forma una lista A
con un numero B de elementos igual al numero de personas, donde cada
elemento B es una lista con los pesos de la persona i 
"""
def od(n):
	dat=[]
	os.chdir("/home/rai/Desktop/intro. al analisis de datos/tarea 2/calibraciones")
	dato=open(Dcal[n],"r")
	os.chdir("/home/rai/Desktop/intro. al analisis de datos/tarea 2")
	contenido= dato.readlines()
	for i in range(4,len(contenido)-1):
		P=contenido[i].split("\t")
		P.pop(0)
		for e in range(len(P)):
			P[e]=P[e].replace("\n","")
			if P[e]=="":
				P.pop(e)
		for c in range(len(P)):
			P[c]=round(float(P[c]),2)
		dat.append(P)
	return dat


#tabla grande:

#desviaciones:
""" odes(archivo,persona):
odes toma el archivo n (con n igual a la variable archivo) y el numero
de la persona en cuestion, para dar como resultado la deviacion 
de esa persona en el archivo
"""
def odes(archivo,persona):
	a=od(archivo)
	if len(a[persona])==3:
		po=round(np.mean(a[persona]),2)
		des=np.sqrt((((a[persona][0]-po)**2)+((a[persona][1]-po)**2)+((a[persona][2]-po)**2))/3)
		return des

	elif len(a[persona])==2:
		des=(((a[persona][0])-(a[persona][1]))**2)/32
		return des

def odes2(archivo,persona):
	a=odes(archivo,persona)
	if a<0.05:
		return 0.05
	else:
		return a
"""
archivo= input("archivo:  ")
persona=input("persona:  ")
print(odes(archivo,persona))
"""
k=[]
t=[]
j=[]
#datos de la tabla:
""" creacion de la tabla:
creo una lista A que sera llevada a la tabla
con cada elemento i de A siendo una lista que contiene
el peso promedio de la persona i y su desviacion en cada balanza
"""
for p in range(32):
	for i in range(len(Dcal)):
		c=od(i)
		for f in range(len(c[p])):
			j.append(c[p][f])
		k.append(round(np.mean(j),2))
		j=[]
		l=str(odes(i,p))
		k.append(l[0:5])	
	t.append(k)
	k=[]
for y in range(len(t)):
	t[y][3]=0.05

suma=0
it=[]
for g in range(16):
	for ef in range(len(t)):
		suma+=round(float(t[ef][g]),2)
	prom=round(suma/len(t),2)
	suma=0
	it.append(prom)
for o in range(len(it)):
	it[o]=round(it[o],2)
t.append(it)

""" desprom:
creo una lista desprom donde se encuentran las desviaciones promedio
de cada balanza
"""
desprom=[]
for i in range(1,9):
	if t[32][2*i-1]<0.05:
		desprom.append(0.05)
	else:
		desprom.append(t[32][2*i-1])
pesprom=[]
for i in range(8):
	pesprom.append(t[32][2*i])
t[32][1]=str(0.05)+"*"
t[32][3]=str(0.05)+"*"
t[32][7]=str(0.05)+"*"
t[32][9]=str(0.05)+"*"
t[32][11]=str(0.05)+"*"
t[32][13]=str(0.05)+"*"
#creacion de la tabla:
col_labels=['peso B-1',"des B-1",'peso B-2','des B-2',
'peso B-3','des B-3','peso B-4','des B-4','peso B-5','des B-5',
'peso B-6','des B-6','peso B-7','des B-7','peso B-8','des B-8']

row_labels=['P-1','P-2','P-3','P-4','P-5','P-6','P-7','P-8','P-9','P-10',
'P-11','P-12','P-13','P-14','P-15','P-16','P-17','P-18','P-19','P-20','P-21',
'P-22','P-23','P-24','P-25','P-26','P-27','P-28',
'P-29','P-30','P-31',"P-32","promedios"]
if pdftabla==True:
	fig=plt.figure()
	the_table = plt.table(cellText=t,
				rowLabels=row_labels,
				colLabels=col_labels,
				loc="center")	
	#borrando los ejes:
	plt.box()			
	ax1 = plt.axes()
	ax1.get_xaxis().tick_bottom()
	ax1.axes.get_yaxis().set_visible(False)
	ax1.axes.get_xaxis().set_visible(False)
	pdf_pages.savefig()
	pdf_pages.close()
	#plt.show()


#metodo cuadrados minimos

#funcion para obtener delta
def delta (balanza,desprom,t):
	n=32
	a=0
	b=0
	c=0
	s=(desprom[balanza])**2
	for i in range(32):
		rae=(1/(s))
		a+=rae
	op=[0,2,4,6,8,10,12,14]
	for i in range(32):
		re=(t[i][op[6]]**2)/(s)
		b+=re
	for i in range(32):
		ra=(t[i][op[6]]/(s))
		c+=ra
	c=c**2
	return a*b-c
	
#funcion para obtener a
def oba(balanza,desprom,t):
	n=32
	op=[0,2,4,6,8,10,12,14]
	s=(desprom[balanza])**2
	a=n*(1/(s))
	b=0
	for i in range(32):
		ri=((t[i][op[balanza]]*t[i][op[6]])/(s))
		b+=ri
	c=0
	for i in range(32):
		re=(t[i][op[6]])/(s)
		c+=re
	d=0
	for i in range(32):
		ra=(t[i][op[balanza]]/(s))
		d+=ra
	return (((a*b)-(c*d))/delta(balanza,desprom,t))

#funcion para obtener b:
def obb(balanza,desprom,t):
	n=32
	op=[0,2,4,6,8,10,12,14]
	s=(desprom[balanza])**2
	a=0
	for i in range(32):
		re=(t[i][op[6]]**2)/(s)
		a+=re
	b=0
	for i in range(32):
		ra=(t[i][op[balanza]]/(s))
		b+=ra
	c=0
	for i in range(32):
		ru=(t[i][op[6]])/(s)
		c+=ru
	d=0
	for i in range(32):
		ri=((t[i][op[balanza]]*t[i][op[6]])/(s))
		d+=ri
	return (a*b-(c*d))/delta(balanza,desprom,t)

#funcion para obtener error de a:
def oberra(balanza,desprom,t):
	n=32
	op=[0,2,4,6,8,10,12,14]
	s=(desprom[balanza])**2
	a=n*(1/(s))
	return a/delta(balanza,desprom,t)

#funcion para obtener error de b:
def oberrb(balanza,desprom,t):
	n=32
	op=[0,2,4,6,8,10,12,14]
	s=(desprom[balanza])**2
	a=0
	for i in range(32):
		re=(t[i][op[6]]**2)/(s)
		a+=re
	return a/delta(balanza,desprom,t)

#funcion para obtener una lista con a,b y sus respectivos errores:
""" obtodo:
obtodo pide el numero de la balanza con la que se esta trabajando
(numero del archivo), desprom(lista con las desviaciones promedio de cada
balanza) y t(datos de la tabla(*ver explicacion linea 74)) y entrega
una lista con a,b y sus respectivos errores
"""
def obtodo(balanza,desprom,t):
	a=round(oba(balanza,desprom,t),4)
	b=round(obb(balanza,desprom,t),4)
	c=oberra(balanza,desprom,t)
	d=oberrb(balanza,desprom,t)
	l=[a,b,c,d]
	return l

if graficosayb==True:
	for i in range(8):
		if i!=6:
			plt.figure()
			xidentidad=np.arange(40,110,0.1)
			yidentidad=xidentidad
			plt.plot(xidentidad,yidentidad,"b--")
			oo=od(i)
			o7=od(6)
			x=[]
			y=[]
			for g in range(32):
				xp=o7[g][0]
				yp=np.mean(oo[g])
				x.append(xp)
				y.append(yp)
			plt.plot(x,y,"ro")
			x_ayb=np.arange(40,110,0.1)
			ayb=obtodo(i,desprom,t)
			y_ayb=ayb[0]*x_ayb+ayb[1]
			plt.plot(x_ayb,y_ayb,"g")
			plt.axis([40,110,40,110])
			titulo="grupo "+str(i+1)
			plt.title(titulo)
			plt.xlabel("pesos balanza 7")
			ylabeler="pesos balanza "+str(i+1)
			plt.ylabel(ylabeler)
			plt.text(50,80,"recta definida por a y b")
			plt.text(50,77,"identidad")
			plt.plot(49,82,"gs")
			plt.plot(49,78,"bs")
			plt.show()

def obRMS(balanza,desprom,t):
	datos=obtodo(balanza,desprom,t)
	oi=od(balanza)
	o7=od(6)
	x=[]
	y=[]
	for g in range(32):
		xp=o7[g][0]
		yp=np.mean(oi[g])
		x.append(xp)
		y.append(yp)
	RMS2=0
	for i in range(32):
		a=datos[0]*x[i]+datos[1]
		b=((y[i]-a)**2)/32
		RMS2+=b
	return np.sqrt(RMS2)

def obCC(balanza,desprom,t):
	n=32
	oi=od(balanza)
	o7=od(6)
	x=[]
	y=[]
	for g in range(32):
		xp=o7[g][0]
		yp=np.mean(oi[g])
		x.append(xp)
		y.append(yp)
	a=0
	b=0
	c=0
	d=0
	for i in range(32):
		xe=x[i]*y[i]
		a+=xe
		b+=x[i]
		c+=y[i]
		d+=(x[i]**2)
	e=b**2
	B=(n*a-b*c)/(n*d-e)
	d=0
	for i in range(32):
		d+=(y[i]**2)
	e=c**2
	B2=(n*a-b*c)/(n*d-e)
	return B*B2

if mostrarayb==True:
	for i in range(8):
		if i!=6:
			print(str(i+1))	
			print(obtodo(i,desprom,t))
			print("RMS= "+str(obRMS(i,desprom,t)))
			print(obCC(i,desprom,t))
#paso a la escala absoluta:
#toma de datos:
os.chdir("/home/rai/Desktop/intro. al analisis de datos/tarea 2")
absoluta=open("calibracion_GAMA_0.dat","r")
content= absoluta.readlines()
lis=content[9:]
lista=[]
for i in range(len(lis)):
	lis[i]=lis[i].replace("\n","")
	dda=lis[i].split(" ")
	lista.append(dda)

""" explicacion de los pasos siguientes:
con las siguientes funciones consegui las diferencias entre los pesos 
obtenidos y teoricos para luego en exel formar un grafico con
las ecuaciones de laque me permitirian llegar a la escala absoluta
"""
def pesoteorico(linea,lista):
	#[N x (1.8 +/- 0.01) litro x 1 kg/litro]
	teo=(int(lista[linea][0]))*1.8
	return teo
def difpeso(lista):
	t=[]
	for i in range(len(lista)):
		a=(float(lista[i][1]))-(float(lista[i][2]))
		b=pesoteorico(i,lista)
		t.append(round(a-b,2))
	return t
"""
for i in range(len(difpeso(lista))):
	print(difpeso(lista)[i])
"""
"""
procedo a crear una funcion que al entregarle un peso de una balanza i
me entrege su equivalente en la balanza 7
"""
def bal7(pesoi,balanza,desprom,t):
	a=obtodo(balanza,desprom,t)
	x=(pesoi-a[1])/(a[0])
	return x
"""
defino funcion que toma datos de la balanza 7 y 
llega a la escala absoluta
"""
def absol(pesob7):
		return pesob7+((0.0173*pesob7)+0.3692)
		
""" pesofinal:
defino funcion que envie los pesos desde una balanza i hasta
la escala absoluta
"""
def pesofinal(pesoi,balanza,desprom,t):
	x=bal7(pesoi,balanza,desprom,t)
	return absol(x)
#creacion de archivos con pesos escala absoluta
os.chdir("/home/rai/Desktop/intro. al analisis de datos/tarea 2/datos absolutos")
Dcal2=os.listdir("/home/rai/Desktop/intro. al analisis de datos/tarea 2/datos")
Dcal2=sorted(Dcal2)

""" creacion absolutos.dat
a continuacion creo los archivos .dat con los datos de
las escalas absolutas
"""
def desvi(pesa):
	if pesa!=6:
		return round(np.sqrt((desprom[pesa]**2)+(desprom[6])),2)
	else:
		return desprom[6]
	
if creardatosabsolutos==True:
	for i in range(8):
		os.chdir("/home/rai/Desktop/intro. al analisis de datos/tarea 2/datos")
		dato=open(Dcal2[i],"r")
		contenido= dato.readlines()
		os.chdir("/home/rai/Desktop/intro. al analisis de datos/tarea 2/datos absolutos")
		nombre="datos_absolutos_"+str(i+1)+".dat"
		f=open(nombre, 'w')
		for e in range(len(contenido)):
			P=contenido[e].split(" ")
			if i!=6:
				P[4]=round(pesofinal(float(P[4]),i,desprom,t),2)
				P.append(desvi(i))
				a=P[7]
				P[7]=P[6]
				P[6]=P[5]
				P[5]=a
				h=(str(P[0])+" "+str(P[1])+" "+str(P[2])+" "+str(P[3])+" "+
				str(P[4])+" "+str(P[5])+" "+str(P[6])+" "+str(P[7]))
				f.write(h)
			else:
				P[4]=round(absol(float(P[4])),2)
				P.append(desvi(6))
				a=P[7]
				P[7]=P[6]
				P[6]=P[5]
				P[5]=a
				h=(str(P[0])+" "+str(P[1])+" "+str(P[2])+" "+str(P[3])+" "+
				str(P[4])+" "+str(P[5])+" "+str(P[6])+" "+str(P[7]))
				f.write(h)
		f.close()

