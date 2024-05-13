import matplotlib.pyplot as plt
import numpy as np
import sys

r=0
def inter(x,y): #x=tempo / y=espaço
	m1 = []
	m2 = []
	for i in x:
	        m1.append([i**2])
	for i2 in y:
	        m2.append([i2])
	A = np.array(m1)
	C=A.T@np.array(m2)
	AI=(np.linalg.inv(A.T@A))
	a = float(round(((AI@C)[0][0]),5))
	return a

pm = []
ct=0
for i in range(1,int(sys.argv[2])+1):
	try:
		p_dt = open("data%s.txt"%str(i))
	except:
		break
	zz=[]
	t=[]
	c=0
	j=0
	passo=0.005+0.002 #0.002 tempo de leitura do sensor
	for dt in p_dt.readlines():
		if r==0 and dt.replace('\n','').replace('\r', '')!="":
			r=float(dt.replace('\n','').replace('\r', ''))
		try:
			dt = float(dt.replace('\n', '').replace('\r', ''))/100-r/100
			if dt<0:
				dt=0
			if len(zz) < int(sys.argv[1]) and float(dt) < 0.6:
				zz.append(dt)
				if ct == 0:
					pm.append(dt)
		except:
			pass

	for i in range(0,len(zz)):
		t.append(float(round(c, 3)))
		c=c+passo
		if ct!= 0:
			try:
				pab = (pm[j]+zz[j])/2
				pm[j] = pab
			except:
				pass
		j=j+1

	p_dt.close()
	plt.scatter(np.array(t), np.array(zz), color='black', s=4)
	ct=1
	r=0

x = np.array(t)
a = inter(t,pm)
g=2*a

plt.plot(x,a*x**2,color="red", linewidth=3.5, label='z(t)')
plt.figtext(0.75, 0.75, r'g = (%s) $\frac{m}{s²}$'%(round(g, 2)))

plt.xlabel('t (s)')
plt.ylabel('z (m)')
plt.grid(True)
plt.title("Experimento Extra | d=0.99")
plt.axis([0,0.4,0,0.3])
plt.legend(loc='upper right')
plt.show()
