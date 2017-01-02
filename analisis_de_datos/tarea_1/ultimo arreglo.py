import math
import matplotlib.mlab as mlab
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from scipy.stats import norm
import scipy.integrate as integrate
mujerestotal=[]
hombrestotal=[]
def gaussiana(x,des,promedio_mt):
	return(1/math.sqrt(2*math.pi*math.pow(des,2)))*math.exp((-0.5*math.pow(x-promedio_mt,2))/math.pow(des,2))

os.chdir("/home/rai/Desktop/intro. al analisis de datos/tarea 1")
pdf_pages = PdfPages("chi-2.pdf")
wos=[]
datosp=os.listdir("/home/rai/Desktop/intro. al analisis de datos/tarea 1/personas")
print(datosp)
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
	bin_m=np.arange(min(machos),max(machos)+3,3)
	fig=plt.figure(dpi=100)
	n,ho,he=plt.hist(machos,bin_m,color="w",edgecolor="b")
	prom_ma=round(np.mean(machos),2)
	prom_hem=round(np.mean(hembras),2)
	des_ma=round(np.std(machos),2)
	des_hem=round(np.std(hembras),2)
	"""
	d=[machos,hembras]
	a=np.linspace(min(d[0]),max(d[0]),1000)
	temp=0
	dx=a[1]-a[0]
	for i in range(len(a)):
		temp+=gaussiana(a[i],prom_ma,des_ma)
	"""
	cd=[]
	u=0
	for e in range(len(n)):
		a=min(machos)+3*e
		b=min(machos)+3*(e+1)
		p_3=integrate.quad(gaussiana,a,b,args=(des_ma,prom_ma))
		cd.append(p_3[0]*len(machos))
	for d in range(len(n)):
		d=math.pow(int(n[e])-cd[e],2)/cd[e]
		u=u+d
	u=round(u,2)	
	
	print(str(prom_ma)+"    "+str(des_ma)+"    "+str(u))
	wos.append(["hombres",prom_ma,des_ma,u])
	###
	bin_m=np.arange(min(hembras),max(hembras)+3,3)
	fig=plt.figure(dpi=100)
	n,ho,he=plt.hist(hembras,bin_m,color="w",edgecolor="b")

	cd=[]
	u=0
	for e in range(len(n)):
		a=min(hembras)+3*e
		b=min(hembras)+3*(e+1)
		p_3=integrate.quad(gaussiana,a,b,args=(des_hem,prom_hem))
		cd.append(p_3[0]*len(mujeres))
	for d in range(len(n)):
		d=math.pow(int(n[e])-cd[e],2)/cd[e]
		u=u+d
	u=round(u,2)
	print(str(prom_hem)+"    "+str(des_hem)+"   "+str(u))
	wos.append(["mujeres",prom_hem,des_hem,u])
total=hombrestotal+mujerestotal
promt_ma=round(np.mean(hombrestotal),2)
promt_hem=round(np.mean(mujerestotal),2)
dest_ma=round(np.std(hombrestotal),2)
dest_hem=round(np.std(mujerestotal),2)
promt_t=round(np.mean(total),2)
dest_t=round(np.std(total),2)
wos.append(["total hombres",promt_ma,dest_ma,"1220.34"])
wos.append(["total mujeres",promt_hem,dest_hem,"1088.96"])
wos.append(["total",promt_t,dest_t,"3014.45"])


fig=plt.figure(figsize = (14,16))
col_labels=['datos de:',"promedio",'desviacion','chi-2']

row_labels=['Maximiliano B','Maximiliano B','Jenny G','Jenny G','Reimundo H',
'Reimundo H','Macarena P','Macarena P','Alvaro T','Alvaro T',
'Hugo Z','Hugo Z','Devika M','Devika M','Paulina Z','Paulina Z',
'Cristobal Mora.','Cristobal Mora.','Vania R','Vania R','Javiera N',
'Javiera N','Avelyn G','Avelyn G','Javiera D','Javiera D','Cristobal Moya',
'Cristobal Moya','Vicente S','Vicente S','Joaquin A',"Joaquin A",'Makarena G',
'Makarena G','Matias B','Matias B','Ignacia P','Ignacia P',
'Martina K','Martina K','Esteban B','Esteban B',
'Carolina C','Carolina C','Ileana C','Ileana C','Carolina O','Carolina O',
'Jose P','Jose P','Fabian P','Fabian P','Matias R',
'Matias R','Francisca E','Francisca E','Conjunto','Conjunto','Conjunto']
table_vals=wos
the_table = plt.table(cellText=table_vals,
			rowLabels=row_labels,
			colLabels=col_labels,
			loc="center")
plt.box()			
ax1 = plt.axes()
ax1.get_xaxis().tick_bottom()
ax1.axes.get_yaxis().set_visible(False)
pdf_pages.savefig()
pdf_pages.close()
