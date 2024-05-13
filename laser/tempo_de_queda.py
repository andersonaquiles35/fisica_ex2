import matplotlib.pyplot as plt
import subprocess as s
import numpy as np
import sys
import os

dist = (87/100)
def data_uno():
	try:
		lim = int(sys.argv[1])
	except:
		print ("Coloque um inteiro como argumento para contagem\nExemplo: python3 %s 3\n"%(sys.argv[0]))
		exit()

	cont = -1
	out_a = ''
	while True:
		t = []
		out = s.run('cat data.txt',shell=True, capture_output=True, text=True).stdout.split('\n')
		for i in out:
			try:
				i=float(i)/1000
				if (float(i)) > 0.25:
					t.append(float(i))
			except:
				pass
		if len(t) >= lim:
			break
		elif len(t) != cont:
			os.system("figlet %s"%(len(t)))
			cont = len(t)
			out_a = out
	print(len(t))
	return sorted(t)

def static(list):
	sl = 0
	for i in list:
		sl+=i
	media = sl/(len(list))
	n=0
	for i in list:
		n += (i-media)**2
	dp=(n/(len(list)))**(1/2)
	ic=dp/(len(list))**(1/2)
	return [media, dp, ic]

def gaussiana(x,a,u):
        y = (2.718**((-1/2)*(((x-u)/a)**2)))/((2*3.14*((a)**2))**(1/2))
        return y

t = data_uno()
tempo = np.array(t)

media = static(t)[0]      # μ
desvio = static(t)[1]     # σ
incerteza = static(t)[2]  # σ/((N)**(1/2))

x=np.arange(t[0],t[-1],0.001)

g = (2*float(dist))/(float(media)**2) #gravidade local
#g = (2*(float(dist))-4*(float(ds)))/(float(media)**2)
print(g)
dg = 4*media**(-3)*incerteza #incerteza da gravidade
if dg < 0:
	dg = dg*(-1)

plt.subplot(1,2,1)
plt.figtext(0.375, 0.80, 'μ = %ss'%(round(media, 3)))
plt.figtext(0.373, 0.75, '|σ| = %s'%(round(desvio, 3)))
plt.figtext(0.371, 0.70, r'|$\frac{σ}{\sqrt{N}}$| = %s'%(round(incerteza, 3)))
plt.hist(tempo, bins=15, density=False, rwidth=0.9)
plt.xlabel('Tempo de Queda (s)')
plt.ylabel('Frequência')

plt.subplot(1,2,2)
plt.plot(x, gaussiana(x,desvio,media), color="black", linewidth=2.8, label='Gaussiana', alpha=0.9)
plt.plot(np.array([media, media]), np.array([0,gaussiana(media,desvio,media)]), '--', color='black')
plt.plot(np.array([media, desvio+media]), np.array([gaussiana(desvio+media,desvio,media),gaussiana(desvio+media,desvio,media)]), '--', color='black')

if len(str(round(g, 2))+str(round(dg, 2))) != 9:
	plt.figtext(0.84, 0.73, r'g = (%s$\pm$%s) $\frac{m}{s²}$'%(round(g, 2), round(dg, 2)))
else:
	plt.figtext(0.825, 0.73, r'g = (%s$\pm$%s) $\frac{m}{s²}$'%(round(g, 2), round(dg, 2)))

plt.hist(tempo, bins=15, density=True, rwidth=0.9)
plt.xlabel('Tempo de Queda (s)')
plt.ylabel('Densidade de Probabilidade (%)')
plt.legend(loc='upper right')

plt.subplots_adjust(left=0.067, right=0.967, bottom=0.1, top=0.85, wspace=0.3)
plt.suptitle("Tempo de Queda (87.0cm)", fontsize=20)

plt.show()
