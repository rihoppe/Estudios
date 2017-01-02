reg = open('g_500(wut).reg')
datos = reg.readlines()
print(datos[0:2])
w = []
r = open('estrellas.reg','w')
#for i in range(2):
for i in range(len(datos)):
	a = datos[i].split(" ")
	print (a)
	b=round(float(a[1]),0)
	c=round(float(a[2]),0)
	print (int(b),int(c))
	d = ' '+str(int(b))+' '+str(int(c))+' '+str(a[3])
	w.append(d)
	r.write(d)
r.close()

