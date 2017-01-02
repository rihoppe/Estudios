import numpy as np
import scipy.constants as constants
import random
import matplotlib.pyplot as plt

def ob_m_abs(m_ap,dist):
	return m_ap+5-(5*dist)
def ob_z(dist): #no usar
	c = 3*(10**5)
	h = 70.
	print c
	return dist*h/(c)
m_ap = []
x = []
y = []
z = []
for i in range(100):
	m_ap.append(random.uniform(-22,-19))
	x.append(random.uniform(-3000,3000))
	y.append(random.uniform(-3000,3000))
	z.append(random.uniform(-3000,3000))
dist = []

print len(x),len(y),len(z)
for i in range(len(x)):
	dist.append(((x[i]**2)+(y[i]**2)+(z[i]**2))**(1/2))
print len(dist)
m_abs = []
for i in range(len(m_ap)):
	m_abs.append(ob_m_abs(m_ap[i],dist[i]))

tan_theta = []
for i in range(len(x)):
	tan_theta.append(y[i] / x[i])
theta = []
for i in range(len(tan_theta)):
	theta.append(np.arctan(tan_theta[i]))

print theta
ax = plt.subplot(111, projection='polar')
ax.scatter(theta, dist, 'ro')
ax.grid(True)
plt.show()
	
"""
print m_ap
print len(m_ap)
"""
