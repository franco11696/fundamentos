plot(x, x, 'b.', x, x2, 'rd', x, x3, 'g^')import matplotlib.pyplot as plt
f = open ('log.txt','r')
log_matrix=f.read().split('\n')
x=list()
y=list()
t=list()
yaw=list()
v_lineal=list()
v_ang=list()

for log_vector in log_matrix:
	log_lines=log_vector.split('\t')
	try:
		t.append(float(log_lines[0]))
		x.append(float(log_lines[1]))
		y.append(float(log_lines[2]))
		v_lineal.append(float(log_lines[4]))
		v_ang.append(float(log_lines[5]))
		yaw.append(float(log_lines[3]))
	except:
		pass

plt.subplot(1, 3, 1)
plt.title("Camino")
plt.plot(x,y)
plt.annotate('Local Max', xy =(x[200],y[200]),
                xytext =(3, 1.8),
                arrowprops = dict(facecolor ='green',
                                  shrink = 0.05),)
plt.subplot(1, 3, 2)
plt.title("Trayectoria")
l=plt.plot(t,x,t,y,t,yaw)
plt.legend((l), ('trayectoria X', 'trayectoria Y', 'orientación'),shadow=True)
plt.subplot(1, 3, 3)
plt.title("Camino")
l1=plt.plot(t,v_lineal,t,v_ang)
plt.legend((l1), ('velocidad lineal', 'velocidad angular'),shadow=True)

plt.show()

